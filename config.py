class Config:
    FILENAME = "centyle.pdf"
    DATA_DIR = "./data"
    SUBTRACTED_DATA_DIR = "./sub_data"
    CHART_DIR = "./charts"
    USED_DIR = DATA_DIR

    DATA_CHART_X = "Wynik"
    DATA_CHART_Y = "Centyl"

    SUB_DATA_CHART_X = "Wynik"
    SUB_DATA_CHART_Y = "Procent osob z takim wynikiem"

    CHART_X = DATA_CHART_X if USED_DIR == DATA_DIR else SUB_DATA_CHART_X
    CHART_Y = DATA_CHART_Y if USED_DIR == DATA_DIR else SUB_DATA_CHART_Y