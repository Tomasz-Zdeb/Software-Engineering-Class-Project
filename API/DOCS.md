# API

## Flask

Flask to mikro-framework napisany w języku Python, który pozwala na tworzenie aplikacji internetowych.

Charakteryzuje się:

- **Prostotą**: Jest łatwy w nauce i zrozumieniu, nawet dla początkujących programistów.
- **Elastycznością**: Pozwala na dużą swobodę w konfiguracji i rozbudowie aplikacji, oferując modularną strukturę.
- **Skalowalnością**: Jest odpowiedni dla projektów o różnym stopniu złożoności, od prostych stron do rozbudowanych systemów.
- **Wsparciem społeczności**: Dysponuje bogatą bazą zasobów, ciągłym rozwojem i aktualizacjami dzięki zaangażowanej społeczności.
- **Integracją z Pythonem**: Zapewnia doskonałe połączenie z innymi bibliotekami i narzędziami Pythona, co ułatwia rozwój i utrzymanie aplikacji.

W naszym projekcie wykorzystujemy Flask do budowy API, które służy komunikacji pomiędzy frontendem a backendem aplikacji. Dzięki użyciu Flask w naszym API, możemy szybko implementować nowe funkcje, a także łatwo aktualizować i modyfikować istniejące elementy.

## Flask-RESTX

Flask-RESTx to rozszerzenie dla Flask, które ułatwia tworzenie szybkich, elastycznych i łatwych w utrzymaniu API opartych na architekturze REST. Zaprojektowany z myślą o prostocie i wydajności, Flask-RESTx wprowadza zestaw narzędzi, które pozwalają na szybką implementację, testowanie oraz dokumentowanie API.

Flask-RESTx charakteryzuje się:

- **Prostotą**: Ułatwia tworzenie API opartych na architekturze REST, oferując czytelne i zwięzłe struktury kodu.
- **Automatyczna dokumentacja**: Wspiera automatyczne generowanie interaktywnej dokumentacji API z wykorzystaniem standardu OpenAPI.
- **Walidacja danych**: Zapewnia wbudowane mechanizmy walidacji danych, co pozwala na utrzymanie spójności i poprawności danych wejściowych i wyjściowych.
- **Przejrzystość**: Dzięki zastosowaniu dekoratorów i przestrzeni nazw, Flask-RESTx pozwala na łatwe rozróżnienie poszczególnych zasobów i funkcji API.
- **Integracja z Flask**: Jako rozszerzenie Flask, Flask-RESTx doskonale współpracuje z innymi elementami frameworka, umożliwiając płynną integrację z istniejącymi aplikacjami opartymi na Flask.

W projekcie, głównym zastosowaniem Flask-RESTx będzie automatyczna generacja dokumentacji Swagger dla endpointów API. Korzystając z interaktywnej dokumentacji API opartej na standardzie OpenAPI, Flask-RESTx pozwala na łatwe zrozumienie, eksplorację i testowanie endpointów API przez użytkowników oraz programistów. Dzięki temu, proces rozwijania i aktualizowania API jest znacznie uproszczony, a czas potrzebny na tworzenie ręcznej dokumentacji jest zredukowany. Automatyczna dokumentacja pozwala także na utrzymanie jej aktualności i spójności z bieżącym stanem endpointów.

## SQLAlchemy

SQLAlchemy to popularna biblioteka ORM (Object Relational Mapper) dla języka Python, która umożliwia programistom łatwe i efektywne zarządzanie bazami danych, korzystając z abstrakcyjnego interfejsu programowania. ORM pozwala na reprezentowanie struktur baz danych jako obiektów w kodzie, co ułatwia pracę z danymi.

### Dlaczego SQLAlchemy?

Wybraliśmy SQLAlchemy ze względu na:

1. **Dostępność**: Obsługa różnych baz danych, co pozwala na elastyczność i łatwość integracji.
2. **Wydajność**: Wysoka wydajność, odpowiednia dla aplikacji o dużym natężeniu ruchu.
3. **Wsparcie**: Dojrzałość, stabilność i aktywny rozwój biblioteki, wsparcie od społeczności.

### Porównanie z innymi bibliotekami: SQLAlchemy vs. Psycopg2

Psycopg2 to również popularna biblioteka Python, służąca do łączenia się i zarządzania bazą danych PostgreSQL. Jednak w przeciwieństwie do SQLAlchemy, Psycopg2 nie jest ORM i operuje na niższym poziomie abstrakcji, co oznacza, że programiści muszą pisać więcej kodu SQL i zarządzać strukturami danych ręcznie.

## Flask-JWT-Extended

Flask-JWT-Extended to rozszerzenie dla Flask, które ułatwia implementację uwierzytelniania i autoryzacji w aplikacjach internetowych. Zapewnia mechanizmy uwierzytelniania oparte na tokenach JWT (JSON Web Token).

## Mechanizm uwierzytelniania użytkowników

Mechanizm uwierzytelniania użytkowników opiera się o JWT (JSON Web Token). JWT to standard definiujący sposób przesyłania informacji
pomiędzy stronami w formie obiektów JSON. Przesyłany token jest podpisany cyfrowo, co pozwala na weryfikację jego autentyczności.

### Logowanie

Podczas logowania, dane wprowadzone przez użytkownika sprawdzane są z danymi znajdującymi się w bazie danych. Jeśli dane są zgodne,
zwrócony zostaje token JWT. W tokenie zapisane jest ID zalogowanego użytkownika, wykorzystywane później przy wykonywaniu różnych operacji w aplikacji (np. tworzenie nowej notatki).

Po udanym logowaniu, token zwracany jest w następującym formacie:

```json
{'access_token': access_token}
```

### Rejestracja

Rejestracja polega na dodaniu nowego użytkownika do bazy danych. W przypadku, gdy użytkownik o podanym adresie email już istnieje, rejestracja nie zostanie przeprowadzona. Po udanej rejestracji token JWT nie zostaje zwrócony. Logowanie musi zostać przeprowadzone osobno.

### Autoryzacja

Autoryzacja polega na sprawdzeniu, czy użytkownik ma uprawnienia do wykonania danej operacji. Brak tokena w nagłówku będzie
zawsze skutkować odmową dostępu, dla każdego endpointu, który wymaga autoryzacji. W przypadku, gdy token jest obecny, sprawdzane jest czy:

- token jest poprawny
- token nie wygasł (domyślnie 1 godzina)
- użytkownik ma uprawnienia do wykonania danej operacji (np. czy edytuje własną notatkę)

Informacja o wymogu tokena dla danego endpointa znajduje się w dokumentacji Swagger. Token należy przekazać w nagłówku Authorization w formacie `Bearer <token>`, za każdym razem
gdy następuje dostęp do chronionego endpointu.

### Wygasanie tokena i wylogowanie

Mechanizm wygasania tokena jest zaimplementowany w podstawowej formie. Token wygasa po upływie określonego czasu (domyślnie 1 godzina). Po wygaśnięciu tokena, użytkownik musi zalogować się ponownie, aby uzyskać nowy token. Mechanizm ten może
zostać dodatkowo rozbudowany o tokeny odświeżąjące, które pozwalają na przedłużenie czasu ważności tokena.

Nie istnieje sposób na ręczne unieważnienie wprost tokena, dlatego w aktualnej implementacji mechanizm wylogowania
użytkownika musi polegać na usunięciu tokena z pamięci po stronie klienta (czyli stronie frontendowej). W aplikacji produkcyjnej ten mechanizm powinien być
rozbudowany o rozwiązanie, polegające na prowadzeniu listy unieważnionych tokenów, tak by móc unieważniać tokeny również po stronie API.

## Flask-CORS

Flask-CORS to rozszerzenie dla Flask, które zapewnia obsługę polityki CORS (Cross-Origin Resource Sharing). CORS to mechanizm, który pozwala na wymianę zasobów pomiędzy różnymi domenami. Dzięki temu, aplikacja frontendowa może komunikować się z API. Zastosowanie biblioteki Flask-CORS znacznie ułatwia konfigurację mechanizmu CORS w API, bez konieczności ręcznego definiowania nagłówków HTTP.

## Flask-Bcrypt

Flask-Bcrypt to rozszerzenie dla Flask, które zapewnia funkcjonalność hashowania haseł. Hasła są hashowane przed zapisaniem do bazy danych. Przy logowaniu hash wprowadzonego hasła jest porównywany z hashem zapisanym w bazie danych. Hashowanie odbywa się za pomocą funkcji bcrypt i szyfru Blowfish.
