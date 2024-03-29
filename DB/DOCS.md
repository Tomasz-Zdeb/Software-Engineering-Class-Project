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

### Hashowanie haseł

- metoda potrzebuje stworzenia rozszerzenia pgcrypto i tabeli:
  - `hashed_password`
- wprowadzanie nowego użytkownika odbywa się za pomocą:
  `INSERT INTO user_table (username, hashed_password)`
  `VALUES ('user_name', crypt('userpassword', gen_salt('bf')));`
- W przypadku dodawania nowych użytkowników przez API hashowanie odbywa się w API i DB przechowuje już zahashowane hasło (z saltem) w tabeli hashed_password

