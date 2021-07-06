from os import mkdir, path

class Config:
    # NAZWA PDFa Z TABELKAMI
    FILENAME = "centyle.pdf"

    DATA_DIR = "./data"
    CHART_DIR = "./charts"

    CHART_X = "Wynik"
    CHART_Y = "Centyl"

if not path.exists(Config.DATA_DIR):
    mkdir(Config.DATA_DIR)

if not path.exists(Config.CHART_DIR):
    mkdir(Config.DATA_DIR)