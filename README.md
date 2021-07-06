OPIS PROJEKTU:

Projekt wydobywa dane z pliku pdf zawierającego centylowe wyniki matur 2021, a następnie tworzy z nich wykresy słupkowe.


WYMAGANIA:

Należy zainstalować interpreter pythona 3.8+ oraz najnowszy JAVA RUNTIME (kompatybilność z tabula-py).
Aby zainstalować wszystkie biblioteki należy aktywować komendę:

pip install -r requirements.txt


OPIS PLIKÓW:

- config.py - zawiera wszystkie dane zmienne, które używają pozostałe pliki

- scraper.py - zdejmuje dane z pliku pdf (opisanego w config.py) a następnie zapisuje je do folderu

- chart_creator.py - na podstawie danych wytworzonych przez scraper.py generuje wykresy

DZIAŁANIE:

Należy najpierw uruchomić scraper.py, a następnie chart_creator.py. Nie można zamienić kolejności bądź uruchomić je z tego samego skryptu, ponieważ JAVA RUNTIME na to nie pozwala.