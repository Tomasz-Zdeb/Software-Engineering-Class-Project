Dokumentacja skryptów SQL:

Jak wykonać skrypty z command line?

 - Skopiuj skrypt SQL do kontenera Docker, uruchamiając następujące polecenie:
    docker cp <path to the_script.sql> <container-name>:/<the_script.sql>
 - Połącz się z serwerem PostgreSQL działającym w twoim kontenerze Docker za pomocą następującego polecenia:
    docker exec -it <container-name> psql -U postgres
 - Wykonaj skrypt SQL, uruchamiając następujące polecenie w wierszu polecenia psql:
    \i /<the_script.sql>
<the_script.sql> zastępujemy nazwą pliku naszego skryptu, a <container-name> nazwą naszego kontenera
<path to the_script.sql>: tutaj będziemy musieli podać lokalny plik skryptu z naszego zaktualizowanego repo 

Opis działania skryptów:

1. db-init.sql: skrypt inicjalizujący bazę danych w środowisku PostgreSQL. Tworzy bazę danych 'ioproject', dwóch użytkowników: admin-user posiadającego pełne uprawnienia, oraz regular-user posiadającego uprawienia write i read. Tworzy także schema public.

2. tables-init.sql: skrypt tworzący wszystkie siedem tabel używanych w projekcie. Kolejno tabele: bin, catalog, note, note_tag, tag, user_note, user_table. Nadawane są uprawnienia dla regular_user na select, insert, update, delete oraz tworzone są foreign keys

3. insert-dummies.sql: skrypt wpisujący do każdej tabeli po 10 dummy rekordów

