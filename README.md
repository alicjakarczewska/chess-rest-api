# chess-rest-api
Flask simple chess REST API

Polecenia do uruchomienia lokalnie aplikacji. 
Pisane w terminalu w główym folderze aplikacji 'flask_api':

1. Utworzenie środowiska wirtualnego

`python -m venv venv`

2. Uruchomienie utworzonego środowiska pracy

`python venv\Scripts\activate`

3. Instalacja pakietów z pliku requirements.txt

`pip install -r requirements.txt`

4. Testowanie aplikacji
Pliki zawierające testy znajdują się w folderze 'tests'. Polecenie do uruchomienia wszystkich testów:

`pytest`

5. Uruchomienie aplikacji

`python app.py`

Aplikacja uruchamia się pod adresem localhost:8000
Możliwe jest wysyłanie przykładowych zapytań, zgodnych z założeniami zadania:

- Pobranie listy możliwych ruchów figury:
/api/v1/{chess-figure}/{current-field}/{dest-field}

Przykładowe zapytanie:
http://localhost:8000/api/v1/king/b2

Odpowiedź:
{"figure": "king", "currentField": "B2", "availableMoves": ["B3", "C3", "C2", "C1", "B1", "A1", "A2", "A3"], "error": null}


- Walidacja możliwości ruchu figury:
/api/v1/{chess-figure}/{current-field}/{dest-field}

1. Przykładowe zapytanie:
http://localhost:8000/api/v1/king/b2/b3

Odpowiedź:
{"figure": "king", "currentField": "B2", "destField": "B3", "error": null, "move": "valid"}

2. Przykładowe zapytanie:
http://localhost:8000/api/v1/king/b2/b4

Odpowiedź:
{"figure": "king", "currentField": "B2", "destField": "B4", "error": null, "move": "invalid"}

- W zapytaniach w nazwie figury i pola można używać zarówno dużych i małych liter. 
Przykładowo:
  - http://localhost:8000/api/v1/KING/b2/B3
  - http://localhost:8000/api/v1/King/b2/B3

- Obsłużone są również przypadki, gdy podane parametry są niepoprawne - zgodnie z treścią zadania:
    - 200 (jeśli wszystko jest ok)
    - 409 (w przypadku złego pola)
    - 404 (jeśli odpytamy o nieistniejącą figurę)
    - 500 (w przypadku błędu serwera)
 
1. Przykładowe zapytanie:
http://localhost:8000/api/v1/king/b9

Odpowiedź:
{"figure": "king", "currentField": "B9", "availableMoves": [], "error": "Field does not exist."}

2. Przykładowe zapytanie:
http://localhost:8000/api/v1/kings/b9

Odpowiedź:
{"figure": "kings", "currentField": "B8", "availableMoves": [], "error": "Figure does not exist."}

Powyższe przypadki zostały także zawarte w utworzonych testach (plik tests/test_api.py).
