# Baza Danych

## Skrypty

### Wywołanie

#### Polecenia

 - Skopiuj skrypt SQL do kontenera:
    `docker cp <path to the_script.sql> <container-name>:/<the_script.sql>`
 - Połącz się z serwerem PostgreSQL:
    `docker exec -it <container-name> psql -U postgres`
 - Wykonaj skrypt SQL w wierszu poleceń **psql**:
    `\i /<the_script.sql>`

#### Parametry

- `<the_script.sql>` nazwa skryptu
- `<container-name>` nazwa kontenera
- `<path to the_script.sql>` ścieżka do skryptu

### Opis

- `db-init.sql`
  - Tworzy bazę danych `ioproject`
  - Tworzy dwóch użytkowników
    - `admin-user` - pełne uprawnienia
    - `regular-user`  write i read
  - Tworzy schema `public`

- `tables-init.sql`
  - Tworzy tabele
  - Tworzy relacje
  - Nadaje uprawnienia

- `insert-dummies.sql` Wprowadza do każdej tabeli po 10 dummy rekordów

