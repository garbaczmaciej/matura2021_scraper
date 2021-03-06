from tabula import read_pdf
import pandas as pd

from config import Config


def is_int(string: str) -> bool:
    try:
        int(float(string))
        return True
    except ValueError:
        return False


class PdfScraper:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.filename = config.FILENAME

    def scrape_file(self) -> None:

        pdf_content = read_pdf(self.filename, pages="all", multiple_tables=True)

        # Pomiń 1. tabelkę
        for table in pdf_content[1:]:

            name = self.get_table_name(table)

            numbers_table = table.values.tolist()[1:]
            results = self.scrape_results(numbers_table)

            results_list = list(results.items())
            results_list.sort(key=lambda item: item[0])

            self.save_results_to_file(name, results_list)
            

    def get_table_name(self, table) -> str:

        table_name_row = table.head(0).keys()
        
        for name in table_name_row:
            if "Unnamed" not in name:
                # NAPRAWIENIE "ROZSZERZON" W DANYCH
                if "rozszerzony" not in name:
                    name = name.replace("rozszerzon", "rozszerzony")
                return name

    def scrape_results(self, numbers_table: pd.DataFrame) -> dict:
        
        results = dict()

        for row in numbers_table:
            try:
                parsed_row = [(int(percent), int(percentile)) for percent, percentile in zip(row[::2], row[1::2]) if str(percent) != "nan"]
            except ValueError:
                # Debugowanie tabelki
                debugged_table = self.debug_numbers_table(numbers_table)
                return self.scrape_results(debugged_table)
            for percent, percentile in parsed_row:
                results[percent] = percentile

        return results

    def debug_numbers_table(self, numbers_table) -> list:
        # Takie coś naprawi te jebane zepsute tabelki
        debugged_table = list()
        for row in numbers_table:
            for item in row:
                if is_int(item):
                    debugged_table.append(str(int(float(item))))
                elif type(item) == str and len(item.split()) > 1:
                    for sub_item in item.split():
                        if is_int(sub_item):
                            debugged_table.append(str(int(float(sub_item))))

        return [debugged_table]


    def save_results_to_file(self, name: str, results_list: list) -> None:
        filepath = self.config.DATA_DIR + f"/{name}.csv"

        percents = [line[0] for line in results_list]
        percentiles = [line[1] for line in results_list]

        df = pd.DataFrame({self.config.CHART_X:percents, self.config.CHART_Y:percentiles})

        with open(filepath, "w") as f:
            f.write(df.to_csv(index=False))
            


def main() -> None:
    pdf_scraper = PdfScraper(Config)
    pdf_scraper.scrape_file()


if __name__ == '__main__':
    main()
