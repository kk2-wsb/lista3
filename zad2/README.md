1. Zrobiłem prostą aplikację, której kod wygląda tak:

def licz(a,b):
    return a+b
print(licz(2,3))

2. Napisałem testy:

from app import licz

def test():
    assert licz(10,5) == 15

3. Stworzyłem plik Makefile:

install:

test:
    pytest test_app.py

run:
    python app.py

4. Przetestowałem makefile.