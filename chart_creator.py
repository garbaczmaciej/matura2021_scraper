from os import listdir

import plotly.express as px

from chart_creator_config import Config


class ChartCreator:
    def __init__(self, filename: str):
        
        self.filename = filename
        
        self.name = None
        self.data = None
        self.parse_data()

    def parse_data(self) -> None:
        with open(self.filename, "r") as f:
            content = [line for line in f.read().split("\n") if line.split()]
            self.name = content[0]
            self.data = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in content[1:]]

    def create_chart(self) -> None:
        fig = px.bar(self.data, x="procent", y="centyl")
        fig.show()


def draw_charts():
    for filename in listdir(Config.DATA_DIRECTORY)[:1]:
        chart_creator = ChartCreator(f"{Config.DATA_DIRECTORY}/{filename}")
        chart_creator.create_chart()


def main():
    draw_charts()


if __name__ == '__main__':
    main()