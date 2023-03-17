# Projekt zaliczeniowy

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

----------

*Ze względu na sposób organizacji pracy, niniejsza specyfikacja może ewoluować w trakcie pracy nad projektem*

## Definiowanie zadań

* W celu definiowania zadań korzystamy z funkcjonalności: **Issues** oferowanej przez **GitHub** na poziomie repozytorium, stanowi ona **Backlog** projektu
* Definicja zadania powinna składać się z:
  * Krótkiego opisowego tytułu (wskazany tryb rozkazujący), np. "*Stwórz specyfikację projektu*"
  * **Kryteriów akceptacji zadania**, czyli punktów opisujących w wysokopoziomowy sposób stan po ukończeniu zadania, np.
   
### Przykład:

Tytuł: Stwórz specyfikację projektu

**Kryteria Akceptacji Projektu:**
* *Specyfikacja projektu jest utworzona*
* *Specyfikacja projektu przedstawiona jest w postaci listy funkcjonalności*

**Dodatkowe informacje:**
* ...

## Model kolaboracji

* Zadania są opisywane przy pomiocy **GitHub Issues** w sposób opisany powyżej
* Implementacja zadań przeprowadzana jest tak, że każde zadanie implementowane jest na oddzielnym branchu
* Branche są nazywane tak jak zadanie które realizują
* Po ukończeniu implementacji zadania na danym branchu tworzony jest **Pull Request** do brancha **master**
* **PR** jest linkowany do **Issue** które realizuje (dzięki temu zmergowanie **PR** będzie skutkowało automatycznym zamknięciem Issue)
* Po pozytywnym rozpatrzeniu **PR** branch jest mergowany do brancha **master** i usuwany

## Dodatkowe informacje

* Lista uczestników znajduje się na prywatnym kanale Discord w celu ograniczenia dostępu do niej

### Opiekun repozytorium

* [Tomasz Zdeb](https://github.com/Tomasz-Zdeb)
