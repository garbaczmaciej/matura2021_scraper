from os import listdir

import plotly.express as px
import pandas as pd

from config import Config


class ChartCreator:
    def __init__(self, filename: str, config: Config):
        
        self.config = config
        self.filename = filename

        self.path = f"{config.DATA_DIR}/{filename}"
        self.name = filename.split(".")[0]


    def get_data(self) -> pd.DataFrame:
        with open(self.path, "r") as f:
            return pd.read_csv(self.path)

    def create_chart(self) -> None:
        data = self.get_data()
        chart = px.bar(data, x=self.config.CHART_X, y=self.config.CHART_Y, title=self.name)
        chart.update_layout(bargap=0)
        self.save_chart(chart)

    def save_chart(self, chart) -> None:
        chart.write_image(f"{self.config.CHART_DIR}/{self.name}.png")


def draw_charts():
    for filename in listdir(Config.DATA_DIR):
        chart_creator = ChartCreator(filename, Config)
        chart_creator.create_chart()


def main():
    draw_charts()


if __name__ == '__main__':
    main()