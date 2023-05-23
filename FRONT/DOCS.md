# Aplikacja Frontendowa 

## Użyte technologie
###React.js - Framework
React to, popularny framework JavaScript do budowy interfejsów użytkownika. React zapewnia efektywny sposób tworzenia interaktywnych, dynamicznych i responsywnych aplikacji internetowych.
Zalety to między innymi komponentowy model, reaktywność, dynamiczna zmiana interfejsu oraz elastyczność.

###Boostrap - Biblioteka stylu
Bootstrap to popularny framework CSS i JavaScript, który zapewnia gotowe komponenty i narzędzia do szybkiego budowania responsywnych aplikacji internetowych. 
Zalety Bootstrapa obejmują łatwość użycia, dostępność gotowych stylów i układów, responsywność na różnych urządzeniach(niezależnie od rozdzielczości ekranu), 
możliwość dostosowania do własnych potrzeb oraz obszerną dokumentację i wsparcie społecznościowe.

###JSON - Komunikacja pomiędzy warstwami aplikacji
Zapytania oraz odpowiedzi na zapytania kierowane z Frontu do API przesyłane są w technologii JSON zgodnie z  [dokumentacją API](
https://github.com/Tomasz-Zdeb/Software-Engineering-Class-Project/blob/master/API/DOCS.md
)

## Struktura aplikacji

###Struktura katalogów i komponentów
```txt
front-app/
├─ src/
│   ├─ components/
│   │   ├─ Editor/          // Komponenty głównego edytora notatek
│   │   ├─ NoteList/        // Komponenty listy notatek (eksplorator notatek) - Leftbar
│   │   ├─ NoteItem/        // Komponenty pojedynczej notatki - NoteItem
│   │   ├─ NoteToolbar/        // Komponenty narzędzi do edycji notatek  - Rightbar
│   │   ├─ LoginWindow/        // Komponenty okna logowania
│   │   └─ ...
│   ├─ services/
│   │   └─ apiService.js           // Moduł do komunikacji z API backendu
│   ├─ utils/
│   │   └─ helpers.js       // Funkcje pomocnicze, uzupełniające React'a
│   ├─ App.js               // Główny komponent aplikacji
│   ├─ App.css              // Główny szablon stylów aplikacji
│   └─ index.js             // Punkt
├─ public/  //
│   └─ ...
├─ package.json
└─ ...
```

###Struktura podziału wyświetlanych treści
- Okno aplikacji - sztywno ustalony rozmiar: wysokość 1000px, szerokość 1200px
  - Topbar: wysokość 200px, szerokość jak okna aplikacji
  - Leftbar: wysokość 800px, szerokość 20% okna aplikacji
  - NoteItem: wysokość 800px, szerokość 70% okna aplikacji
  - Rightbar: wysokość 800px, szerokość 10# okna aplikacji
- Okno logowania - Modal wyświetlony z pomocą z-index, skalowane na środku Okna aplikacji
  - Rozmiar: wysokość 200px, szerokość 400px


## Inicjalizacja aplikacji

```sh
npx create-react-app my-react-app
```

## Testy

Pliki źródłowe testów znajdują się w katalogu

```txt
front-app/
├─ src/
│  ├─ tests/
```

Aby wykonać wszystkie testy należy skorzystać z polecenia znajdując się w directory projektu aplikacji frontendowej `front-app`:

```sh
npm test
```

## Framework CSS - Bootstrap

Bootstrap został dodany poprzez wykonanie polecenia:

```sh
npm install bootstrap react-bootstrap
```

oraz zaimportowanie zainstalowanego modułu w pliku `index.js`

```javascript
import 'bootstrap/dist/css/bootstrap.min.css';
```
