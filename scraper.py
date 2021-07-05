from tabula import read_pdf

from scraper_config import Config


def is_int(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False


class PdfScraper:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def scrape_file(self) -> None:

        pdf_content = read_pdf(self.filename, pages="all", multiple_tables=True)
        for table in pdf_content[16:]:

            # Znajdź nazwę tabeli
            table_name_row = table.head(0).keys()
            for name in table_name_row:
                if "Unnamed" not in name:
                    break

            numbers_table = table.values.tolist()[1:]
            results = dict()

            a = False
            for row in numbers_table:
                if len(row) == 6:
                    parsed_row = [(int(percent), int(percentile)) for percent, percentile in zip(row[::2], row[1::2]) if str(percent) != "nan"]
                    for percent, percentile in parsed_row:
                        results[percent] = percentile
                else:
                    print(row)
                    a = True
            if a:
                print(numbers_table)
                print()
                print()
                return

            results_list = list(results.items())
            results_list.sort(key=lambda item: item[0])

            self.save_results_to_file(name, results_list)
            


    def save_results_to_file(self, name: str, results_list: list) -> None:
        filepath = Config.DATA_DIR + f"/{name}.txt"
        # CLEAR FILE
        with open(filepath, "w") as f:
            f.write("")

        with open(filepath, "a") as f:
            f.write(f"{name}\n")
            for percent, percentile in results_list:
                f.write(f"{percent},{percentile}\n")
            


def main() -> None:
    pdf_scraper = PdfScraper(Config.FILENAME)
    pdf_scraper.scrape_file()


if __name__ == '__main__':
    main()
