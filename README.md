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


## Dodatkowe informacje

* Lista uczestników znajduje się na prywatnym kanale Discord w celu ograniczenia dostępu do niej

### Opiekun repozytorium

* [Tomasz Zdeb](https://github.com/Tomasz-Zdeb)
