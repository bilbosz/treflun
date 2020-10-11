# Setup projektu Treflun

Konsola #1:
```sh
python3 -m pip install virtualenv # instaluje obsługę wirtualnych środowisk
git clone git@github.com:bilbosz/treflun.git treflun
cd treflun
python3 -m virtualenv venv # instaluje wirtualne środowisko w treflun/venv, potrzebne, żeby nie zaśmiecać systemowego pythona
source venv/bin/activate # aktywuje wirtualne środowisko
python --version # powinna być >=3.6.9
python -m pip install -r requirements.txt # instalujemy requirementy przez pip'a
python manage.py # "program" do zarządzania serverem, wyświetla dostępne komendy
python manage.py makemigrations # przygotowuje plik z migracjami, przydatne na produkcji jak już mamy jakieś dane, warto sobie zobaczyć, można zmieniać
python manage.py migrate # wykonuje migracje zawarte w wylistowanych plikach
```

Konsola #2 albo w tle, ale śmieci output:
```sh
redis-server # u mnie Redis version=6.0.6 i musi być chyba >=5.0 z tego co czytałem, wydaje mi się, że domyślne ustawienia wystarczą
```

Konsola #1:
```sh
python manage.py runserver # uruchamia server
```

Można uruchomić w przeglądarce adres wylistowany w outpucie `http://127.0.0.1:8000/`. Nic nie widać, bo nie ma w bazie tokenów i graczy.

Konsola #1:
```sh
python manage.py createsuperuser # dodajemy admina, wypełniamy pola
python manage.py runserver
```

W przeglądarce wchodzimy na adres `http://127.0.0.1:8000/admin` i logujemy się na podane przez nas wcześniej credentiale. Teraz czeka nas dodanie Userów, Tokenów i Graczy.
1. Dodaj usera.
2. Dodaj playera przypisując mu usera.
3. Dodaj token.
4. Przejdź pod adres `http://127.0.0.1:8000/` w dwóch kartach w przeglądarce, twój token powinien być widoczny i zsynchronizowany pomiędzy kartami