# Aplikacja Frontendowa

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
