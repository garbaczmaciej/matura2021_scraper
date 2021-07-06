from os import mkdir

class Config:
    # NAZWA PDFa Z TABELKAMI
    FILENAME = "centyle.pdf"

    DATA_DIR = "./data"
    CHART_DIR = "./charts"

    CHART_X = "Wynik"
    CHART_Y = "Centyl"

try:
    mkdir(Config.DATA_DIR)
except FileExistsError:
    pass

try:
    mkdir(Config.CHART_DIR)
except FileExistsError:
    pass