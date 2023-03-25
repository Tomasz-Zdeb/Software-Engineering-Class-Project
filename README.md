W ramach zaliczenia laboratorium z przedmiotu: **Inżynieria Oprogramowania** jesteśmy zobowiązani grupowo wykonać projekt. Kryteria nie są z góry narzucone.

# Produkt: Aplikacja Webowa do Przechowywania Notatek

## Specyfikacja

###  Architektura

-   Komponent frontendowy (Web GUI)
-   Komponent backendowy (API)
-   Baza danych

### Funkcjonalności

-   Rejestracja użytkowników
-   Logowanie użytkowników
-   Tworzenie notatek
-   Przechowywanie notatek
-   Przeglądanie notatek
-   Edycja notatek
-   Wyszukiwanie po zadanym parametrze
-   Tagowanie notatek
-   Filtrowanie po tagach
-   Usuwanie do kosza
-   Udostępnianie notatek między użytkownikami

### Wymagania

-   Stylizacja tekstu w trakcie edycji, stylami: bold, italic, underline
-   Stylizacja nagłówków w trzech poziomach
-   Stylizacja zawartości w listy: numerowane i nienumerowane
-   Utrzymywanie sesji przez określony w konfiguracji timeout

### Dodatkowe funkcjonalności (nie planowane do implementacji)

-   Ograniczenie praw użytkowników którym udostępniono notatkę
-   Automatyczne kopie zapasowe
-   Eksport notatek

> Ze względu na sposób organizacji pracy, niniejsza specyfikacja może ewoluować w trakcie pracy nad projektem

## Model kolaboracji

### Definiowanie zadań

* W celu definiowania zadań korzystamy z funkcjonalności: **Issues** oferowanej przez **GitHub** na poziomie repozytorium, stanowi ona **Backlog** projektu
* Definicja zadania powinna składać się z:
  * Krótkiego opisowego tytułu (wskazany tryb rozkazujący), np. "*Stwórz specyfikację projektu*"
  * **Kryteriów akceptacji zadania**, czyli punktów opisujących w wysokopoziomowy sposób stan po ukończeniu zadania, np.
   
  #### Przykład:

```
Tytuł: Stwórz specyfikację projektu

**Kryteria Akceptacji Zadania:**
* *Specyfikacja projektu jest utworzona*
* *Specyfikacja projektu przedstawiona jest w postaci listy funkcjonalności*

**Dodatkowe informacje:**
* ...
```

 * Issues oznaczamy **labelem** klasyfikującym jego: `{kategorię,priorytet}`

### Branching
* Aktualny stan projektu reprezentowany jest przez branch: **master**
* Zadania (Issues) implementuje się na dedykowanych branchach o nazwach odpowiadających nazwie zadania, które po zakończeniu pracy nad zadaniem merguje się do brancha master poprzez stworzenie Pull Requesta
* Pull Requesty pozostawia się z domyślną nazwę
* Opis w Pull Requeście jest tworzony jedynie gdy stopień złożoności zmian jest bardzo wysoki
* Po zmergowaniu Pull Requesta, branch jest usuwany

### _GitHub Actions_
#### ```delete-branch-on-merge.yml```
- Opis:
_Action_ ```delete-merged-branch``` usuwa gałąź połączoną z danym _Pull Request'em_, jeśli _PR_ został połączony z gałęzią docelową. Dzięki temu akcja ta pozwala na utrzymanie repozytorium w czystości poprzez automatyczne usuwanie już niepotrzebnych gałęzi. _Action_ uruchamia się w momencie zamknięcia _Pull Request'a_ oznaczonego jako ```closed```. Następnie wykorzystuje ```SvanBoxel/delete-merged-branch```, aby usunąć gałąź, która była źródłem _Pull Requesta_. Akcja ta nie wymaga dodatkowych zależności i opiera się na standardowych _GitHub Actions_.
- Zależności:
  - _GITHUB_TOKEN_:
  Aby móc wykonać usuwanie gałęzi, _Action_ wymaga dostępu do ```secrets.GITHUB_TOKEN```, który jest automatycznie tworzony przez GitHub i umożliwia wykonanie operacji na repozytorium za pomocą API GitHuba. Ważne jest, aby upewnić się, że w ustawieniach repozytorium na GitHubie, w sekcji "_Secrets_", zostało dodane GITHUB_TOKEN z odpowiednimi uprawnieniami do usuwania gałęzi. Aby uzyskać więcej informacji na temat GITHUB_TOKEN i jak go skonfigurować, można przejrzeć dokumentację GitHuba: https://docs.github.com/en/actions/reference/authentication-in-a-workflow.
  -	_SvanBoxel_:
  ```SvanBoxel/delete-merged-branch``` to gotowy do użycia _Action_, który usuwa gałęzie (_branche_) z repozytorium po ich scaleniu (_merge_) z innymi gałęziami, najczęściej z główną gałęzią repozytorium. _Action_ ten działa następująco: **kiedy następuje zdarzenie typu pull_request o typie closed, _Action_ pobiera informacje o zamkniętym _Pull Request'cie_ i sprawdza, czy został on scalony**. Jeśli tak, _Action_ pobiera informacje o gałęzi, która została scalona z gałęzią główną, i usuwa ją z repozytorium. Link do kodu źródłowego ```SvanBoxel/delete-merged-branch```: https://github.com/SvanBoxel/delete-merged-branch.




## Dodatkowe informacje

* Lista uczestników znajduje się na prywatnym kanale Discord w celu ograniczenia dostępu do niej

### Opiekun repozytorium

* [Tomasz Zdeb](https://github.com/Tomasz-Zdeb)
