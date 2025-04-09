# Tiny url

Aplikacja do skracania adresów url.

## Instalacja

Projekt przygotowany jest na Python w wersji 3.13.2.

1. Zainstaluj zależności:

```commandline
pip install -r requirements/requirements.txt
```

...lub całą aplikację:

```commandline
pip install .
```

2. Uruchom migracje:

 ```commandline
python manage.py migrate
```

## Serwer developerski

Uruchomienie serwera developerskiego możliwe jest przy użyciu komendy:

```commandline
python manage.py runserver
```

## Użycie

Aby skrócić url, należy zapytać końcówkę `/api/link/` np.:

```commandline
curl -X POST -d '{"original_url": "https://google.pl"}' -H Content-Type:application/json localhost:8000/api/link/
```

Zapytanie adresu zwróconego pod kluczem `short_url` (np. przez przeglądarkę) przekieruje na oryginalny adres.

### Panel administracyjny

Panel administracyjny Django dostępny jest pod adresem `/admin/`.

## Deploy

Domyślna konfiguracja aplikacjji **nie jest** przystosowana do deployu. Minimalne czynności, które powinny zostać
dokonane przed uruchomieniem produkcyjnym opisane są w dokumentacji Django:

https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

## Testy

Aby uruchomić testy trzeba mieć zainstalowane zależności z pliku `requirements/requirements-tests.txt`:

```commandline
pip install -r requirements/requirements-tests.txt
```

Uruchomić testy pozwala komenda  `pytest`:

```commandline
pytest
```
