# Inżynieria Oprogramowania : Aplikacja Webowa do Przechowywania Notatek

W ramach zaliczenia laboratorium z przedmiotu jesteśmy zobowiązani grupowo wykonać projekt. Kryteria nie są z góry narzucone.

## Specyfikacja

### Architektura

- Komponent frontendowy (Web GUI)
- Komponent backendowy (API)
- Baza danych

### Funkcjonalności

- Rejestracja użytkowników
- Logowanie użytkowników
- Tworzenie notatek
- Przechowywanie notatek
- Przeglądanie notatek
- Edycja notatek
- Wyszukiwanie po zadanym parametrze
- Tagowanie notatek
- Filtrowanie po tagach
- Usuwanie do kosza
- Udostępnianie notatek między użytkownikami

### Wymagania

- Stylizacja tekstu w trakcie edycji, stylami: bold, italic, underline
- Stylizacja nagłówków w trzech poziomach
- Stylizacja zawartości w listy: numerowane i nienumerowane
- Utrzymywanie sesji przez określony w konfiguracji timeout

### Dodatkowe funkcjonalności (nie planowane do implementacji)

- Ograniczenie praw użytkowników którym udostępniono notatkę
- Automatyczne kopie zapasowe
- Eksport notatek

> Ze względu na sposób organizacji pracy, niniejsza specyfikacja może ewoluować w trakcie pracy nad projektem

### Diagram związków encji

![Entity-Relationship-Diagram](https://github.com/Tomasz-Zdeb/Software-Engineering-Class-Project/blob/master/DB/ERD-diagram.drawio.png)

## Format komunikacji

Format  JSON  (JavaScript Object Notation) został wspólnie  wybrany  przez  zespoły  frontendowy  i  API  jako  podstawowy  sposób  komunikacji  między  nimi.

Wybór  ten  podyktowany  jest  kilkoma  istotnymi  zaletami, które  sprawiają, że  JSON  jest  odpowiednim  rozwiązaniem  dla  naszego  projektu:

1. **Uniwersalność**: JSON  jest  obsługiwany  przez  większość języków  programowania  i  frameworków, co  ułatwia  integrację między  różnymi  technologiami  używanymi  przez  zespoły  frontendowy  i  API.
2. **Czytelność**: JSON  jest łatwy  do  czytania  zarówno  dla  ludzi, jak  i  maszyn. Jego  struktura  opiera  się na  parze  klucz-wartość, co  sprawia, że  dane  są proste  do  zrozumienia  i  interpretacji.
3. **Lekkość**: JSON  jest  lżejszy  od  innych  formatów  wymiany  danych, takich  jak  XML, co  przekłada  się na  szybsze  przesyłanie  danych  między  klientem  a  serwerem, a  także  na  mniejsze  obciążenie  sieci.
4. **Elastyczność**: JSON  pozwala  na łatwe  manipulowanie  danymi, a  także  na  ich  konwersję na  inne  formaty. Dzięki  temu  można łatwo  przekształcić dane  otrzymane  z  API  do  postaci, która  jest  odpowiednia  dla  konkretnego  zadania.

### Przykład zapytania w formacie: `application/json`

```json
{ 
    "email": "example@email.com", 
    "password": "example_password" 
}
```

### Przykład odpowiedzi w formacie: `application/json`

```json
{  
    "status": "success",  
    "data":  
        {  
            "user_id": 123,  
            "name": "John Doe",  
            "token": "abcd1234"  
        }
}
```

## Model kolaboracji

### Definiowanie zadań : **Backlog**

- W celu definiowania zadań korzystamy z funkcjonalności **GitHub Issues** na poziomie repozytorium stanowiącej **Backlog** projektu
- Definicja zadania składa się z:
  - **Tytułu** będącego krótkim opisem w trybie rozkazującym, np. "*Stwórz specyfikację projektu*"
  - **Kryteriów akceptacji zadania**, czyli wysokopoziomowych stwierdzeń opisujących stan po realizacji zadania. Kryterium akceptacji powinno być zdefiniowane tak aby możliwa była boolowska walidacja stanu jego realizacji `[T/F]`
- W celu utworzenia Issue wskazane jest skorzystanie z gotowego szablonu dostępnego w repozytorium
- Issues oznaczane są **labelami** klasyfikującymi:
  - kategorię techniczną
  - priorytet
  - czas-życia
  - dodatkowe atrybuty

### Branching

- Aktualny stan projektu reprezentowany jest przez branch: **master**
- Zadania (Issues) implementuje się na dedykowanych branchach o nazwach odpowiadających nazwie zadania, które po zakończeniu pracy nad zadaniem merguje się do brancha master poprzez stworzenie Pull Requesta
- Pull Requesty pozostawia się z domyślną nazwę
- Opis w Pull Requeście jest tworzony jedynie gdy stopień złożoności zmian jest bardzo wysoki
- Po zmergowaniu Pull Requesta, branch jest usuwany

### Techniki Programistyczne

- Pair programming
- Group programming

## CI/CD : **GitHub Actions**

### Dokumentacja

- [GitHub Actions Docs](https://docs.github.com/en/actions/quickstart)

### Pipeline'y

- `delete-branch-on-merge.yml`
  - Opis: usuwa gałąź połączoną z danym *Pull Request'em*, jeśli *PR* został połączony z gałęzią docelową. Dzięki temu akcja ta pozwala na utrzymanie repozytorium w czystości poprzez automatyczne usuwanie niepotrzebnych gałęzi.
  - Trigger: *Action* uruchamia się w momencie zamknięcia *Pull Request'a* oznaczonego jako ```closed```. Następnie wykorzystuje istniejące *Action*: `SvanBoxel/delete-merged-branch`, aby usunąć gałąź, która była źródłem zmian *Pull Requesta*.
  - Konfiguracja: plik: `./.github/delete-merged-branch-config.yml`
  - Zależności:
    - `GITHUB_TOKEN` - Automatycznie tworzony token autoryzacyjny, który umożliwia wykonanie operacji na repozytorium za pomocą API GitHuba. Aby `secrets.GITHUB_TOKEN` działał z action prawidłowo istotne jest, aby w ustawieniach repozytorium na GitHubie, w sekcji "*Secrets*", `GITHUB_TOKEN` z został skonfigurowany z odpowiednimi uprawnieniami do usuwania gałęzi. Więcej informacji na temat GITHUB_TOKEN i jego konfiguracji znajduje się w [oficjalnej dokumentacji](https://docs.github.com/en/actions/reference/authentication-in-a-workflow).
    - `SvanBoxel/delete-merged-branch` to *Action*, który usuwa gałęzie z repozytorium po ich scaleniu (*merge*) z innymi gałęziami, najczęściej z główną gałęzią repozytorium. *Action* ten działa następująco: **kiedy następuje zdarzenie typu pull_request o typie closed, *Action* pobiera informacje o zamkniętym *Pull Request'cie* i sprawdza, czy został on scalony**. Jeśli tak, *Action* pobiera informacje o gałęzi, która została scalona z gałęzią główną, i usuwa ją z repozytorium. Dodatkowych informacji na temat *Action* może dostarczy analiza [kodu źródłowego](https://github.com/SvanBoxel/delete-merged-branch).
- `markdownlint.yml`
  - Opis: przeprowadza linting wszystkich plików z rozszerzniem `.md` znajdujących się w projekcie, pod kątem poprawności składni języka `markdown`. Więcej informacji na temat reguł walidacji i konfiguracji lintera znajduje się w [oficjalnej dokumentacji](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
  - Trigger:
    - Push zmian
    - Modyfikacja *Pull Requesta*
  - Konfiguracja: plik: `./.markdownlint.json`

## Skrypty

### Linux

- `refresh-git-remotes-list.sh` - Odświeża listę branchów znajdujących się na remote: origin (domyślna nazwa zdalnego repozytorium)

- `stop-app.sh` - Zatrzymuje aplikację i usuwa persistent storage volumes

- `start-app.sh` - Jeżeli aplikacja jest uruchomiona, zatrzymuje ją, buduje na nowo wszystkie obrazy i uruchamia w trybie detached (w tle)

### Windows

- `refresh-git-remotes-list.bat` - Odświeża listę branchów znajdujących się na remote: origin (domyślna nazwa zdalnego repozytorium)

## Konteneryzacja Aplikacji : Docker

Każdy z komponentów aplikacji przystosowany jest do uruchamiania w kontenerze **Dockera**. Każdy komponent zawiera w swoim katalogu plik: `Dockerfile` pozwalający na zbudowanie obrazu.

W celu uproszczenia procesu uruchamiania aplikacji wykorzystywane jest narzędzie: `docker-compose` pozwalające na uruchomienie kontenerów, stworzenie sieci i przeprowadzenie wszelkiej konfiguracji niezbędnej do prawidłowego współdziałania komponentów aplikacji.


### Volumes

Kontenery z natury są nietrwałe/ulotne. Oznacza to że z momentem usunięcia danego kontenera wszelkie dane z nim związane są tracone. Docker oferuje jednak możliwość utworzenia trwałych wolumenów danych i zmapowanie ich z danym kontenerem co pozwala na przechowywanie danych np. zapisanych w bazie danych bez względu na to czy w danym momencie istnieje kontener zawierający baze danych czy nie.

Aby usunąć wolumeny zdefiniowane przez `docker-compose` należy skorzystać z flagi: `--volumes`

- `docker-compose down --volumes`

### Referencje

- [Dokumentacja obrazu PostgrSQL](https://hub.docker.com/_/postgres/)

## Dodatkowe Informacje

- Lista uczestników znajduje się na prywatnym kanale Discord w celu ograniczenia dostępu do niej

### Opiekun repozytorium

- [Tomasz Zdeb](https://github.com/Tomasz-Zdeb)
