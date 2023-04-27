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

### Definiowanie zadań

- W celu definiowania zadań korzystamy z funkcjonalności: **Issues** oferowanej przez **GitHub** na poziomie repozytorium, stanowi ona **Backlog** projektu
- Definicja zadania powinna składać się z:
  - Krótkiego opisowego tytułu (wskazany tryb rozkazujący), np. "*Stwórz specyfikację projektu*"
  - **Kryteriów akceptacji zadania**, czyli punktów opisujących w wysokopoziomowy sposób stan po ukończeniu zadania, np.
- W celu utworzenia typowego Issue wskazane jest skorzystanie z gotowego szablonu dostępnego w repozytorium
- Issues oznaczane są **labelem** klasyfikującym jego: `{kategorię,priorytet}`

### Branching

- Aktualny stan projektu reprezentowany jest przez branch: **master**
- Zadania (Issues) implementuje się na dedykowanych branchach o nazwach odpowiadających nazwie zadania, które po zakończeniu pracy nad zadaniem merguje się do brancha master poprzez stworzenie Pull Requesta
- Pull Requesty pozostawia się z domyślną nazwę
- Opis w Pull Requeście jest tworzony jedynie gdy stopień złożoności zmian jest bardzo wysoki
- Po zmergowaniu Pull Requesta, branch jest usuwany

### Techniki Programistyczne

- Pair programming
- Group programming

### Pipeline'y CI/CD : **GitHub Actions**

- ```delete-branch-on-merge.yml```
  - Opis: usuwa gałąź połączoną z danym *Pull Request'em*, jeśli *PR* został połączony z gałęzią docelową. Dzięki temu akcja ta pozwala na utrzymanie repozytorium w czystości poprzez automatyczne usuwanie niepotrzebnych gałęzi.
  - Trigger: *Action* uruchamia się w momencie zamknięcia *Pull Request'a* oznaczonego jako ```closed```. Następnie wykorzystuje istniejące *Action*: ```SvanBoxel/delete-merged-branch```, aby usunąć gałąź, która była źródłem zmian *Pull Requesta*.
  - Zależności:
    - `GITHUB_TOKEN` - Automatycznie tworzony token autoryzacyjny, który umożliwia wykonanie operacji na repozytorium za pomocą API GitHuba. Aby ```secrets.GITHUB_TOKEN``` działał z action prawidłowo istotne jest, aby w ustawieniach repozytorium na GitHubie, w sekcji "*Secrets*", `GITHUB_TOKEN` z został skonfigurowany z odpowiednimi uprawnieniami do usuwania gałęzi. Więcej informacji na temat GITHUB_TOKEN i jego konfiguracji znajduje się w [oficjalnej dokumentacji](https://docs.github.com/en/actions/reference/authentication-in-a-workflow).
    - `SvanBoxel/delete-merged-branch` to *Action*, który usuwa gałęzie z repozytorium po ich scaleniu (*merge*) z innymi gałęziami, najczęściej z główną gałęzią repozytorium. *Action* ten działa następująco: **kiedy następuje zdarzenie typu pull_request o typie closed, *Action* pobiera informacje o zamkniętym *Pull Request'cie* i sprawdza, czy został on scalony**. Jeśli tak, *Action* pobiera informacje o gałęzi, która została scalona z gałęzią główną, i usuwa ją z repozytorium. Dodatkowych informacji na temat *Action* może dostarczy analiza [kodu źródłowego](https://github.com/SvanBoxel/delete-merged-branch).

## Dodatkowe informacje

- Lista uczestników znajduje się na prywatnym kanale Discord w celu ograniczenia dostępu do niej

### Opiekun repozytorium

- [Tomasz Zdeb](https://github.com/Tomasz-Zdeb)
