# Specyfikacja Wymagań Oprogramowania (SRS) – Projekt Delta5 (v 1.0)

## 1. Wstęp

### 1.1. Cel
Dokument ten definiuje pełny zakres wymagań dla platformy Delta5 w wersji MVP. Jest on przeznaczony dla zespołu deweloperskiego oraz prowadzących przedmiot w celu weryfikacji zgodności projektu z założeniami biznesowymi.

### 1.2. Wizja, Zakres i Cele Produktu
* **Wizja:** Delta5 to nowoczesne centrum nauki, integrujące komunikację w czasie rzeczywistym i kontrolę postępów w jednym miejscu.
* **Zakres:** System obejmuje zarządzanie kursami, komunikację (czat), moduł zadań i ocen oraz automatyczne sprawdzanie testów.
* **Cele Biznesowe (KPIs):**
    * Średnia tygodniowa aktywność studentów na poziomie 90% (wzrost o 20% względem Delta4).
    * Osiągnięcie 85% satysfakcji użytkowników z łatwości obsługi na desktopie.
    * Skrócenie czasu przesyłania projektów i oceniania o 20%.
* **Poza Zakresem:** System nie będzie wspierał natywnych aplikacji mobilnych oraz integracji z systemem EHMS w fazie MVP.

### 1.3. Definicje i Akronimy
* **LMS:** Learning Management System. 

System informatyczny służący do kompleksowego zarządzania procesem zdalnego nauczania, umożliwiający tworzenie kursów, udostępnianie materiałów edukacyjnych oraz monitorowanie postępów studentów
* **MVP:** Minimum Viable Product.

Pierwsza, funkcjonalna wersja platformy Delta5, skupiona na kluczowych modułach takich jak komunikacja i zarządzanie zadaniami, mająca na celu szybką walidację założeń projektowych.
* **RODO:** Rozporządzenie o Ochronie Danych Osobowych.

Europejskie rozporządzenie o ochronie danych osobowych, które w projekcie narzuca konieczność stosowania silnego szyfrowania oraz bezpiecznego przechowywania danych wrażliwych, w tym ocen i prywatnych wiadomości użytkowników
* **LCP:** Largest Contentful Paint.

Metryka mierząca czas, jaki upływa od rozpoczęcia ładowania strony do momentu pełnego wyrenderowania największego elementu treści (np. obrazu lub bloku tekstu) w obszarze widocznym dla użytkownika


### 1.4. Przegląd dokumentu
Dokument ten stanowi kompleksową specyfikację wymagań dla platformy Delta5. Rozdział 2 przedstawia ogólną charakterystykę systemu, wizję produktu oraz założenia projektowe. W Rozdziale 3 zdefiniowano szczegółowe wymagania funkcjonalne wraz z historyjkami użytkownika i kryteriami akceptacji. Rozdział 4 określa wymagania niefunkcjonalne (atrybuty jakościowe) oraz kryteria ich weryfikacji, a Rozdział 5 zawiera analizę wymagań.

---

## 2. Opis Ogólny

### 2.1. Główne Funkcje Produktu
1. **Zarządzanie Kursem:** Tworzenie kursów, przydzielanie prowadzących i harmonogramy.
2. **Komunikacja:** Czaty grupowe i indywidualne, powiadomienia w czasie rzeczywistym.
3. **Moduł Zadań i Ocen:** Przesyłanie plików (do 200MB) oraz wizualizacja statystyk.
4. **Automatyczne Testy:** Moduł tworzenia i samoczynnego sprawdzania quizów teoretycznych.
5. **Materiały i Ogłoszenia:** Publikacja materiałów kursowych (pliki/linki) oraz ogłoszeń w kursie.
6. **Uwierzytelnianie i Role:** Logowanie, sesje oraz kontrola dostępu (Student/Prowadzący/Owner).

### 2.2. Klasy Użytkowników i Persony
* **Student:** Skupiony na terminowości i intuicyjnej obsłudze mobilnej/desktopowej.
* **Prowadzący:** Kluczowy użytkownik zarządzający treścią i ocenami.
* **Persony (MVP):**
    * **Kamil, 22 lata — student z niepełnosprawnością (dostępność jako warunek konieczny).**
        * **Kontekst:** Studiuje dziennie, dużo pracuje wieczorami. Ma obniżoną ostrość wzroku i nadwrażliwość na bodźce (w tym migotanie / intensywne animacje).
        * **Cele:** Szybko odnaleźć zadania i terminy, bezbłędnie wysłać pliki, sprawdzić wyniki testów.
        * **Potrzeby dostępności:** możliwość zwiększenia rozmiaru tekstu (min. 120–150%), stabilny **ciemny motyw** o wysokim kontraście, ograniczenie animacji (preferencja „reduced motion”), pełna obsługa klawiaturą.
        * **Ryzyka/obawy:** przypadkowe ukrycie ważnych informacji (np. terminów), niedostępne komponenty (brak focus state), zbyt małe elementy klikalne.
    * **Ola, 20 lat — studentka pracująca dorywczo (czas i powiadomienia jako klucz).**
        * **Kontekst:** Łączy studia z pracą, uczy się „w okienkach” i często działa na laptopie w podróży. Ma kilka kursów równolegle.
        * **Cele:** Nie przegapić terminów, szybko sprawdzić czy zadanie „poszło”, mieć wgląd w oceny bez proszenia prowadzących.
        * **Potrzeby:** jednoznaczny status oddania (Oddane/Spóźnione), powiadomienia o nowych zadaniach i opublikowanych ocenach, szybki dostęp do materiałów.
        * **Ryzyka/obawy:** brak potwierdzenia po uploadzie, ukryte informacje o terminie, powiadomienia „spamujące” zamiast przydatnych.
    * **Teresa, 61 lat — prowadząca ceniąca prostotę i przewidywalność.**
        * **Kontekst:** Prowadzi kilka grup, nie chce „walczyć z narzędziem”. Często pracuje na laptopie z touchpadem.
        * **Cele:** Jednym miejscem zarządzić kursem (harmonogram, zadania, testy), szybko zobaczyć kto oddał i jakie są wyniki.
        * **Preferencje UX:** proste, jednoznaczne etykiety i komunikaty, mało kroków, domyślne ustawienia „bezpieczne”, brak ukrytych akcji.
        * **Ryzyka/obawy:** pomyłkowe opublikowanie testu/zadania, trudne do znalezienia ustawienia, zbyt techniczne błędy.
    * **Marek, 35 lat — prowadzący „techniczny” (szybkie masowe operacje i audyt).**
        * **Kontekst:** Prowadzi zajęcia projektowe, ma dużą grupę i ograniczony czas. Zależy mu na porządku i minimalnej liczbie ręcznych czynności.
        * **Cele:** Szybko wystawić oceny i feedback, mieć jasną listę oddań (kto nie oddał), móc wrócić do historii zmian przy sporach.
        * **Potrzeby:** lista oddań z filtrami/statusami, możliwość szkicowania i publikacji ocen, historia wersji oddań i zmian ocen (audyt).
        * **Ryzyka/obawy:** brak śladu kto zmienił ocenę/role, trudne do pobrania pliki, niejednoznaczne statusy.

### 2.3. Ograniczenia Projektowe
* **Organizacyjne:** Realizacja MVP w 3 miesiące przez dwóch studentów bez wcześniejszego doświadczenia w tworzeniu produkcyjnych systemów LMS.
* **Budżetowe:** Ograniczenie do bezpłatnych subskrypcji oraz planów studenckich narzędzi chmurowych i modeli AI (brak budżetu na dedykowaną infrastrukturę).
* **Regulacyjne:** Wymóg zgodności z RODO przy przetwarzaniu danych osobowych użytkowników.
* **Środowiskowe:** Brak dostępu do środowiska testowego identycznego z produkcyjnym – testy przeprowadzane na maszynach deweloperskich.

### 2.4. Założenia Projektowe

1. **Techniczne: Darmowy plan hostingu obsłuży obciążenie pilotażowe.**
    * **Treść:** Zakładamy, że darmowe plany (np. Render/Heroku dla Django i PostgreSQL) wystarczą do obsłużenia ruchu generowanego przez jedną grupę dziekańską.
    * **Ryzyko:** Serwer może przestać odpowiadać przy nagłym skoku aktywności (np. wszyscy studenci logują się na kolokwium), co zablokuje dostęp do materiałów i zniechęci użytkowników.
    * **Plan walidacji:** Przeprowadzenie testów obciążeniowych symulujących 50 jednoczesnych użytkowników przed oficjalnym startem semestru.

2. **Użytkowe: Czarny motyw interfejsu (Dark Mode) jest preferowany przez grupę docelową.**
    * **Treść:** Zakładamy, że domyślny ciemny motyw zwiększy komfort pracy studentów, którzy często uczą się w godzinach wieczornych.
    * **Ryzyko:** Część użytkowników może mieć trudności z czytelnością przy słabym kontraście, co wpłynie negatywnie na dostępność (Accessibility) i satysfakcję.
    * **Plan walidacji:** Przeprowadzenie testów A/B na etapie prototypu oraz zebranie ankiet satysfakcji po pierwszym tygodniu użytkowania wersji Beta.

---

## 3. Wymagania Funkcjonalne

### 3.1. Priorytetyzacja (Model Fibonacci)
Priorytet wyliczony wg wzoru: Priorytet = (Korzyść + Kara) / (Koszt + Ryzyko)


| Funkcjonalność | Korzyść | Kara | Koszt | Ryzyko | Priorytet |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Uwierzytelnianie i role (RBAC) | 13 | 21 | 5 | 3 | **4.25** |
| Przesyłanie zadań | 21 | 13 | 3 | 2 | **6.80** |
| Oceny i feedback | 13 | 21 | 5 | 3 | **4.25** |
| Materiały i ogłoszenia | 13 | 13 | 5 | 2 | **3.71** |
| Powiadomienia (deadline, oceny, czat) | 8 | 13 | 3 | 2 | **4.20** |
| Zarządzanie kursem | 13 | 13 | 5 | 3 | **3.25** |
| Automatyczne testy | 13 | 5 | 8 | 5 | **1.38** |
| Czat Real-time | 8 | 3 | 13 | 8 | **0.52** |

**Uzasadnienie zakresu MVP:** Na podstawie wyliczonego priorytetu, rdzeń MVP (największa wartość przy relatywnie niskim koszcie/ryzyku) stanowią: **Przesyłanie zadań**, **Uwierzytelnianie i role (RBAC)**, **Oceny i feedback**, **Powiadomienia** oraz **Materiały i ogłoszenia** — te funkcje bezpośrednio realizują KPI (aktywność, skrócenie czasu oddawania/oceniania) i minimalizują ryzyko sporów o terminy/oceny. **Zarządzanie kursem** pozostaje elementem niezbędnym do spójnego działania pozostałych modułów. **Czat real-time** i **Automatyczne testy** mają niższy priorytet w modelu (wysoki koszt/ryzyko względem korzyści), ale są utrzymane w MVP jako funkcje wyróżniające; w przypadku ograniczeń czasowych są implementowane jako ostatnie w kolejności prac.

### 3.2. Szczegółowe Wymagania

Poniższe wymagania odpowiadają pozycjom z tabeli priorytetów (Rozdział 3.1). Każde wymaganie zawiera user story oraz **mocno rozpisane** kryteria akceptacji w stylu BDD (Given/When/Then), w tym scenariusze alternatywne i wyjątkowe.

#### WF-AUTH-01: Uwierzytelnianie i role (logowanie, sesja, RBAC)
* **Opis:** System umożliwia logowanie użytkowników (Student/Prowadzący) oraz egzekwuje kontrolę dostępu na podstawie ról w kontekście kursu (RBAC).
* **User Story (Użytkownik):** Jako użytkownik, chcę zalogować się bezpiecznie i utrzymać sesję, abym miał dostęp do kursów i swoich zasobów.
* **User Story (Prowadzący/Owner):** Jako prowadzący/owner, chcę aby osoby spoza kursu nie miały dostępu do jego treści, abym chronił materiały i dane studentów.
* **Cel Biznesowy:** Zapewnienie bezpiecznego, jednoznacznego dostępu do systemu i ograniczenie ryzyka wycieku danych (RODO).
* **Warunki Wstępne:** Użytkownik posiada aktywne konto w systemie.
* **Warunki Końcowe:** Użytkownik ma aktywną sesję, a dostęp do zasobów jest ograniczony rolami i członkostwem w kursach.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path — logowanie):**
    * **Given:** Użytkownik znajduje się na ekranie logowania.
    * **When:** Podaje poprawne dane logowania i zatwierdza.
    * **Then:** System tworzy sesję i przekierowuje do panelu „Kursy”.
    * **And:** Użytkownik widzi wyłącznie kursy, do których należy.

* **Scenariusz Alternatywny (Błędne dane):**
    * **Given:** Użytkownik jest na ekranie logowania.
    * **When:** Podaje niepoprawne dane logowania.
    * **Then:** System odmawia zalogowania.
    * **And:** System wyświetla komunikat ogólny (np. „Nieprawidłowy login lub hasło”), bez ujawniania czy konto istnieje.

* **Scenariusz Alternatywny (Wygaśnięcie sesji):**
    * **Given:** Użytkownik był zalogowany i nie wykonał żadnej akcji przez określony czas.
    * **When:** Próbuje wykonać akcję wymagającą autoryzacji.
    * **Then:** System wymaga ponownego zalogowania.
    * **And:** System nie traci danych wprowadzonych w formularzu (jeśli to możliwe) albo wyświetla jasną instrukcję odtworzenia akcji.

* **Scenariusz Wyjątkowy (Ochrona przed atakiem brute-force):**
    * **Given:** Ten sam adres IP lub konto generuje wiele nieudanych prób logowania.
    * **When:** Przekroczony zostanie limit prób (np. 10 w 10 minut).
    * **Then:** System stosuje ograniczenie (rate-limit lub czasową blokadę) i rejestruje zdarzenie bezpieczeństwa.

* **Scenariusz Bezpieczeństwa (RBAC — brak dostępu):**
    * **Given:** Użytkownik nie jest uczestnikiem kursu.
    * **When:** Próbuje otworzyć zasób kursu (materiały/oceny/czat) przez bezpośredni link.
    * **Then:** System odmawia dostępu (np. 403/404) i nie ujawnia treści ani metadanych zasobu.

---

#### WF-COURSE-01: Zarządzanie kursem (tworzenie, role, zapis)
* **Opis:** System umożliwia prowadzącemu tworzenie i konfigurowanie kursów (nazwa, opis, harmonogram), zarządzanie rolami oraz listą uczestników (zaproszenia / kod dołączenia), a studentowi dołączanie do kursu.
* **User Story (Prowadzący):** Jako prowadzący, chcę utworzyć kurs i przydzielić do niego studentów oraz ustawienia, abym mógł prowadzić zajęcia i publikować materiały, zadania oraz testy w jednym miejscu.
* **User Story (Student):** Jako student, chcę dołączyć do kursu poprzez kod lub zaproszenie, abym miał dostęp do czatu, zadań i testów mojej grupy.
* **Cel Biznesowy:** Uporządkowanie pracy w jednym narzędziu i ograniczenie liczby błędów organizacyjnych (np. praca „w złym kursie”).
* **Warunki Wstępne:** Użytkownik jest zalogowany. Prowadzący ma uprawnienie do tworzenia kursów.
* **Warunki Końcowe:** Kurs istnieje w bazie danych, ma przypisane role, a działania (utworzenie/zmiany) są audytowane.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path — utworzenie kursu):**
    * **Given:** Prowadzący jest zalogowany i znajduje się w panelu „Kursy”.
    * **When:** Prowadzący wybiera „Utwórz kurs”, podaje wymagane dane (min. nazwa) i zapisuje.
    * **Then:** System tworzy nowy kurs i przekierowuje do widoku kursu.
    * **And:** System wyświetla widoczne potwierdzenie „Kurs utworzony”.
    * **And:** Prowadzący ma rolę **Owner/Instructor** w utworzonym kursie.

* **Scenariusz Główny (Happy Path — dołączenie studenta kodem):**
    * **Given:** Student jest zalogowany i posiada kod dołączenia do kursu.
    * **When:** Student wprowadza kod w akcji „Dołącz do kursu”.
    * **Then:** System dopisuje studenta do listy uczestników kursu.
    * **And:** Student widzi kurs na liście kursów oraz ma dostęp do modułów (czat, zadania, testy) zgodnie z rolą **Student**.

* **Scenariusz Alternatywny (Błędny / wygasły kod):**
    * **Given:** Student wprowadza kod, który nie istnieje lub jest wygasły.
    * **When:** Student zatwierdza formularz.
    * **Then:** System odmawia dołączenia do kursu.
    * **And:** System wyświetla komunikat zrozumiały dla nietechnicznego użytkownika (np. „Kod jest nieprawidłowy lub wygasł”).
    * **And:** System nie ujawnia w komunikacie, czy dany kurs istnieje (ochrona przed enumeracją).

* **Scenariusz Alternatywny (Zarządzanie rolami):**
    * **Given:** W kursie istnieje co najmniej 1 prowadzący i co najmniej 1 student.
    * **When:** Owner zmienia rolę wybranego użytkownika na „Prowadzący” lub usuwa uczestnika.
    * **Then:** Zmiana jest natychmiast widoczna w kursie.
    * **And:** Użytkownik traci/zyskuje dostęp do akcji administracyjnych zgodnie z rolą.
    * **And:** System zapisuje kto i kiedy wykonał zmianę (audyt).

* **Scenariusz Wyjątkowy (Brak uprawnień):**
    * **Given:** Student próbuje wejść w URL ustawień kursu.
    * **When:** System weryfikuje uprawnienia.
    * **Then:** System blokuje dostęp (np. 403) i pokazuje komunikat „Brak uprawnień”.
    * **And:** Żadne dane administracyjne (np. lista ról) nie są ujawnione w UI.

* **Wymagania dostępności (konkretne, testowalne):**
    * **Given:** Użytkownik włączył tryb ciemny oraz zwiększył rozmiar tekstu do 150%.
    * **When:** Użytkownik przegląda listę kursów i formularz tworzenia kursu.
    * **Then:** Interfejs pozostaje czytelny (brak uciętych etykiet, nachodzących elementów, ukrytych przycisków) oraz wszystkie akcje są dostępne z klawiatury.

---

#### WF-MATERIAL-01: Materiały i ogłoszenia w kursie
* **Opis:** System umożliwia prowadzącemu publikowanie materiałów (pliki/linki) oraz ogłoszeń w ramach kursu, a studentom przeglądanie i pobieranie.
* **User Story (Prowadzący):** Jako prowadzący, chcę dodać materiały do kursu, abym mógł udostępnić studentom pliki i linki w jednym miejscu.
* **User Story (Student):** Jako student, chcę szybko znaleźć aktualne materiały i ogłoszenia, abym nie przegapił ważnych informacji.
* **Cel Biznesowy:** Ograniczenie chaosu komunikacyjnego (mniej linków w mailach/Teams) i poprawa organizacji kursu.
* **Warunki Wstępne:** Użytkownik jest zalogowany i ma dostęp do kursu.
* **Warunki Końcowe:** Materiał/ogłoszenie jest zapisane, ma autora i znacznik czasu, oraz jest widoczne zgodnie z rolą.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path — publikacja materiału):**
    * **Given:** Prowadzący jest w widoku kursu i ma uprawnienie do dodawania materiałów.
    * **When:** Dodaje materiał (plik lub link), ustawia tytuł i publikuje.
    * **Then:** Materiał pojawia się na liście materiałów kursu.
    * **And:** System zapisuje autora i czas publikacji.

* **Scenariusz Główny (Happy Path — odczyt studenta):**
    * **Given:** Student jest uczestnikiem kursu.
    * **When:** Otwiera listę materiałów.
    * **Then:** Widzi materiały w kolejności od najnowszych.
    * **And:** Może pobrać plik lub otworzyć link.

* **Scenariusz Alternatywny (Wersjonowanie/aktualizacja):**
    * **Given:** Materiał został już opublikowany.
    * **When:** Prowadzący podmienia plik lub edytuje link.
    * **Then:** System oznacza materiał jako zaktualizowany i pokazuje datę aktualizacji.
    * **And:** System zachowuje poprzednią wersję lub co najmniej historię zmian (min. kto i kiedy).

* **Scenariusz Wyjątkowy (Brak uprawnień):**
    * **Given:** Student próbuje dodać materiał.
    * **When:** Zatwierdza formularz.
    * **Then:** System odmawia wykonania akcji i pokazuje komunikat „Brak uprawnień”.

* **Wymagania dostępności (konkretne, testowalne):**
    * **Given:** Użytkownik korzysta z klawiatury i ma ustawione 150% rozmiaru tekstu.
    * **When:** Przegląda listę materiałów i otwiera szczegóły.
    * **Then:** Wszystkie elementy (filtry, przyciski, linki) są dostępne z klawiatury i mają widoczny fokus.

---

#### WF-TEST-01: Automatyczne sprawdzanie testów
* **Opis:** System umożliwia tworzenie testów jednokrotnego wyboru, które są automatycznie oceniane przez algorytm natychmiast po ich przesłaniu.
* **User Story:** Jako prowadzący, chcę, aby system automatycznie sprawdzał testy teoretyczne, abym mógł zaoszczędzić czas i szybciej udostępnić wyniki studentom.
* **Cel Biznesowy:** Skrócenie czasu oczekiwania na ocenę (feedback) oraz odciążenie prowadzących z powtarzalnych czynności administracyjnych.
* **Warunki Wstępne:** Użytkownik jest zalogowany jako student, a test jest aktywny w harmonogramie kursu.
* **Warunki Końcowe:** Wynik testu oraz odpowiedzi studenta zostają zapisane w bazie danych PostgreSQL, a dziennik ocen zostaje zaktualizowany.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path):**
    * **Given:** Student otworzył aktywny quiz w przeglądarce.
    * **When:** Student zaznacza odpowiedzi na wszystkie pytania i klika przycisk "Wyślij".
    * **Then:** System porównuje odpowiedzi z kluczem w bazie danych.
    * **And:** System wyświetla studentowi wynik punktowy (np. 15/20).
    * **And:** Ocena jest automatycznie zapisywana w module Oceny.

* **Scenariusz Alternatywny (Ograniczenie prób):**
    * **Given:** Prowadzący ustawił limit prób dla testu (np. 1 próba).
    * **When:** Student próbuje uruchomić test po wykorzystaniu limitu.
    * **Then:** System blokuje kolejne podejście.
    * **And:** System pokazuje informację „Wykorzystano limit prób” oraz (jeśli dostępne) ostatni wynik.

* **Scenariusz Alternatywny (Błędne odpowiedzi):**
    * **Given:** Student wypełnił test, ale zaznaczył większość błędnych odpowiedzi.
    * **When:** Student zatwierdza formularz.
    * **Then:** System pokazuje niski wynik punktowy.
    * **And:** System NIE wyświetla poprawnych odpowiedzi (aby zapobiec przekazywaniu ich innym studentom), jeśli prowadzący włączył opcję "Ukryj klucz".

* **Scenariusz Alternatywny (Widoczność wyniku):**
    * **Given:** Prowadzący ustawił „Pokaż wynik natychmiast” = WYŁ.
    * **When:** Student wysyła test.
    * **Then:** System zapisuje wynik, ale student widzi komunikat „Odpowiedzi zapisane — wynik zostanie opublikowany przez prowadzącego”.

* **Scenariusz Wyjątkowy (Zerwanie połączenia):**
    * **Given:** Student jest w trakcie rozwiązywania testu.
    * **When:** Użytkownik traci połączenie z internetem w momencie kliknięcia "Wyślij".
    * **Then:** System wyświetla komunikat o błędzie sieci ("Brak połączenia").
    * **And:** System umożliwia ponowną próbę wysłania odpowiedzi po odzyskaniu połączenia, bez utraty zaznaczonych wcześniej opcji.

* **Wymagania dostępności (konkretne, testowalne):**
    * **Given:** Użytkownik korzysta z nawigacji klawiaturą.
    * **When:** Przechodzi między pytaniami i zaznacza odpowiedzi.
    * **Then:** Fokus jest zawsze widoczny, a wybór odpowiedzi można wykonać bez myszy.
    * **And:** Interfejs nie wykorzystuje migających animacji przy odliczaniu czasu (jeśli timer istnieje).

---

#### WF-GRADE-01: Oceny i feedback (zadania + testy)
* **Opis:** System umożliwia prowadzącemu ocenianie oddań zadań oraz publikowanie ocen/komentarzy, a studentowi przegląd ocen i historii zmian.
* **User Story (Prowadzący):** Jako prowadzący, chcę wystawić ocenę i feedback do oddania, abym mógł dać studentowi jasną informację zwrotną.
* **User Story (Student):** Jako student, chcę zobaczyć swoje oceny i komentarze, abym wiedział co poprawić.
* **Cel Biznesowy:** Skrócenie czasu komunikacji „kto ma jaką ocenę” oraz zmniejszenie liczby sporów.
* **Warunki Wstępne:** Użytkownik jest zalogowany i ma dostęp do kursu. Istnieje oddanie zadania lub wynik testu.
* **Warunki Końcowe:** Ocena jest zapisana i (po publikacji) widoczna dla studenta. Zdarzenia są audytowane.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path — wystawienie oceny):**
    * **Given:** Prowadzący otworzył listę oddań dla zadania.
    * **When:** Wybiera studenta, wprowadza ocenę (np. 0–100 lub 2.0–5.0) i komentarz oraz publikuje.
    * **Then:** System zapisuje ocenę i komentarz.
    * **And:** Student widzi ocenę w module „Oceny”.

* **Scenariusz Alternatywny (Szkic oceny):**
    * **Given:** Prowadzący ocenia oddanie.
    * **When:** Zapisuje ocenę jako szkic (nie publikuje).
    * **Then:** Ocena nie jest widoczna dla studenta.
    * **And:** Prowadzący widzi ją jako „Szkic”.

* **Scenariusz Alternatywny (Zmiana oceny):**
    * **Given:** Ocena została opublikowana.
    * **When:** Prowadzący zmienia ocenę.
    * **Then:** System zapisuje nową wartość.
    * **And:** System zachowuje historię zmian (min. poprzednia wartość, kto i kiedy).

* **Scenariusz Wyjątkowy (Brak uprawnień):**
    * **Given:** Student próbuje wystawić ocenę.
    * **When:** Próbuje zapisać ocenę przez UI lub API.
    * **Then:** System blokuje akcję.
    * **And:** System rejestruje zdarzenie jako próbę naruszenia uprawnień.

* **Wymagania dostępności (konkretne, testowalne):**
    * **Given:** Student korzysta z czytnika ekranu.
    * **When:** Otwiera listę ocen.
    * **Then:** Oceny są przedstawione w strukturze możliwej do odczytu (tabela z nagłówkami/etykietami), bez informacji zakodowanej tylko kolorem.

---

#### WF-TASK-01: Przesyłanie zadań (upload, terminy, wersje)
* **Opis:** System umożliwia prowadzącemu tworzenie zadań z terminem oddania oraz studentom przesyłanie rozwiązań jako pliki (do 200MB), z możliwością ponownego przesłania przed terminem.
* **User Story (Student):** Jako student, chcę przesłać rozwiązanie zadania w postaci pliku i mieć pewność, że system je poprawnie zapisał, abym nie stracił zaliczenia przez błąd techniczny.
* **User Story (Prowadzący):** Jako prowadzący, chcę szybko zobaczyć kto oddał zadanie i pobrać przesłane pliki, abym mógł sprawnie ocenić i dać feedback.
* **Cel Biznesowy:** Skrócenie czasu „operacyjnego” związanego z przyjmowaniem prac oraz zmniejszenie liczby sporów o terminy i status oddania.
* **Warunki Wstępne:** Użytkownik jest zalogowany i jest uczestnikiem kursu. Zadanie jest opublikowane.
* **Warunki Końcowe:** Plik rozwiązania jest zapisany, metadane (autor, czas, wersja) są w bazie, a status oddania jest widoczny dla obu stron.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path — utworzenie zadania):**
    * **Given:** Prowadzący jest w kursie i ma uprawnienie do tworzenia zadań.
    * **When:** Prowadzący tworzy zadanie z tytułem, opisem i terminem oddania, a następnie publikuje.
    * **Then:** Zadanie jest widoczne na liście zadań dla studentów.
    * **And:** Termin jest prezentowany jednoznacznie (data + godzina + strefa czasowa/założenie lokalne).

* **Scenariusz Główny (Happy Path — przesłanie rozwiązania):**
    * **Given:** Student otworzył zadanie przed upływem terminu.
    * **When:** Student wybiera plik (≤ 200MB) i klika „Wyślij”.
    * **Then:** System zapisuje plik i wyświetla potwierdzenie „Wysłano”.
    * **And:** System pokazuje metadane: nazwa pliku, rozmiar, data/godzina wysłania.
    * **And:** Status zadania zmienia się na „Oddane”.

* **Scenariusz Alternatywny (Ponowne przesłanie przed terminem):**
    * **Given:** Student oddał już zadanie, a termin jeszcze nie minął.
    * **When:** Student wysyła nowy plik.
    * **Then:** System zapisuje nową wersję jako aktualną.
    * **And:** System zachowuje historię (min. liczba wersji i czas wysłania), aby prowadzący mógł zweryfikować przebieg.

* **Scenariusz Alternatywny (Po terminie):**
    * **Given:** Termin oddania minął.
    * **When:** Student próbuje wysłać rozwiązanie.
    * **Then:** System domyślnie blokuje wysyłkę i pokazuje komunikat „Termin minął”.
    * **And:** Jeśli prowadzący włączył opcję „Zezwól na spóźnione”, system przyjmuje plik, ale oznacza je jako „Spóźnione”.

* **Scenariusz Wyjątkowy (Zbyt duży plik):**
    * **Given:** Student wybiera plik większy niż 200MB.
    * **When:** Student próbuje wysłać.
    * **Then:** System odrzuca upload.
    * **And:** System pokazuje czytelny komunikat z limitem oraz sugeruje rozwiązanie (np. „spakuj plik” / „usuń niepotrzebne dane”).

* **Scenariusz Wyjątkowy (Przerwanie uploadu):**
    * **Given:** Upload trwa.
    * **When:** Połączenie zostaje przerwane.
    * **Then:** System pokazuje błąd i nie oznacza zadania jako „Oddane”.
    * **And:** Student może wznowić proces wysyłki bez konieczności ręcznego „czyszczenia” stanu.

* **Scenariusz Administracyjny (Lista oddań dla prowadzącego):**
    * **Given:** W zadaniu istnieją oddania od wielu studentów.
    * **When:** Prowadzący otwiera podgląd zadania.
    * **Then:** System wyświetla listę studentów z jednoznacznym statusem (Nie oddał / Oddane / Spóźnione).
    * **And:** Prowadzący może pobrać plik (lub aktualną wersję) dla wybranego studenta.

* **Wymagania dostępności (konkretne, testowalne):**
    * **Given:** Użytkownik ma ustawione 150% rozmiaru tekstu.
    * **When:** Przechodzi przez proces wysyłki.
    * **Then:** Kluczowe informacje (termin, status, przycisk wysyłki, komunikaty błędów) pozostają widoczne bez przewijania w poziomie.

---

#### WF-NOTIF-01: Powiadomienia (zadania, oceny, wiadomości)
* **Opis:** System dostarcza powiadomienia w UI (oraz opcjonalnie e-mail) o kluczowych zdarzeniach: nowe ogłoszenie, nowe zadanie, zbliżający się termin, opublikowana ocena, nowa wiadomość.
* **User Story (Student):** Jako student, chcę dostawać czytelne powiadomienia o terminach i ocenach, abym nie przegapił ważnych zdarzeń.
* **User Story (Prowadzący):** Jako prowadzący, chcę aby studenci widzieli ogłoszenia i zmiany bez spamowania, abym zwiększył skuteczność komunikacji.
* **Cel Biznesowy:** Zwiększenie terminowości i aktywności, przy minimalizacji frustracji (brak „nadmiaru” alertów).
* **Warunki Wstępne:** Użytkownik jest zalogowany i ma dostęp do kursu.
* **Warunki Końcowe:** Powiadomienie zostaje zapisane jako przeczytane/nieprzeczytane i jest możliwe do audytu.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path — nowe zadanie):**
    * **Given:** Prowadzący publikuje nowe zadanie w kursie.
    * **When:** Student otworzy aplikację.
    * **Then:** System wyświetla powiadomienie „Nowe zadanie: <tytuł>”.
    * **And:** Powiadomienie prowadzi linkiem do zadania.

* **Scenariusz Główny (Happy Path — ocena opublikowana):**
    * **Given:** Prowadzący opublikował ocenę dla studenta.
    * **When:** Student przejdzie do panelu lub otworzy listę powiadomień.
    * **Then:** Widzi powiadomienie o opublikowanej ocenie.

* **Scenariusz Alternatywny (Konsolidacja i ograniczenie spamu):**
    * **Given:** System generuje wiele powiadomień w krótkim czasie.
    * **When:** Przekroczony zostanie próg (np. 5 zdarzeń w 1 minutę).
    * **Then:** System konsoliduje je w jedno powiadomienie zbiorcze (np. „5 nowych zdarzeń w kursie”).

* **Scenariusz Alternatywny (Ustawienia):**
    * **Given:** Użytkownik ma dostęp do ustawień powiadomień.
    * **When:** Wyłączy powiadomienia e-mail dla czatu, ale zostawi dla ocen.
    * **Then:** System nie wysyła e-maili o czacie i nadal wysyła e-maile o ocenach.

* **Wymagania dostępności (konkretne, testowalne):**
    * **Given:** Użytkownik ma włączoną preferencję ograniczenia animacji.
    * **When:** Pojawia się powiadomienie.
    * **Then:** Powiadomienie nie używa migających animacji.
    * **And:** Jest możliwe do zamknięcia klawiaturą i ma poprawną etykietę dla czytnika ekranu.

---

#### WF-CHAT-01: Czat Real-time (kursowy i prywatny)
* **Opis:** System zapewnia komunikację w czasie rzeczywistym (real-time) w ramach kursu (kanał grupowy) oraz wiadomości prywatne 1:1, z natychmiastową synchronizacją między użytkownikami.
* **User Story (Student):** Jako student, chcę napisać do prowadzącego i grupy na czacie w czasie rzeczywistym, abym mógł szybko wyjaśnić wątpliwości dotyczące zadań i testów.
* **User Story (Prowadzący):** Jako prowadzący, chcę mieć jeden kanał komunikacji przypięty do kursu, abym mógł ograniczyć chaos informacyjny i nie gubić pytań studentów.
* **Cel Biznesowy:** Zwiększenie aktywności i skrócenie czasu uzyskania odpowiedzi (wzrost satysfakcji i regularności pracy).
* **Warunki Wstępne:** Użytkownik jest zalogowany i ma dostęp do kursu (dla czatu kursowego) lub jest uprawniony do kontaktu 1:1.
* **Warunki Końcowe:** Wiadomości są zapisane (persistencja) i widoczne po odświeżeniu strony.

**Kryteria Akceptacji:**

* **Scenariusz Główny (Happy Path — czat kursowy):**
    * **Given:** Student i prowadzący są w tym samym kursie.
    * **When:** Student wysyła wiadomość na kanale kursu.
    * **Then:** Wiadomość pojawia się u innych uczestników bez ręcznego odświeżania.
    * **And:** Wiadomość zawiera autora oraz czas wysłania.
    * **And:** Po odświeżeniu strony wiadomość nadal jest widoczna (persistencja).

* **Scenariusz Główny (Happy Path — wiadomość prywatna 1:1):**
    * **Given:** Student otworzył konwersację prywatną z prowadzącym.
    * **When:** Student wysyła wiadomość.
    * **Then:** Wiadomość trafia tylko do uczestników tej konwersacji.
    * **And:** Użytkownicy spoza konwersacji nie mają dostępu do jej treści ani metadanych.

* **Scenariusz Alternatywny (Powiadomienie o nowej wiadomości):**
    * **Given:** Użytkownik jest zalogowany i znajduje się w innym module (np. zadania).
    * **When:** Przyjdzie nowa wiadomość.
    * **Then:** System pokazuje czytelny wskaźnik nieprzeczytanych (badge/licznik) bez agresywnych animacji.
    * **And:** Po wejściu w czat, wskaźnik nieprzeczytanych jest aktualizowany.

* **Scenariusz Wyjątkowy (Utrata połączenia i ponowne połączenie):**
    * **Given:** Użytkownik ma otwarty czat.
    * **When:** Traci połączenie z internetem.
    * **Then:** System pokazuje stan „Rozłączono” i blokuje wysyłanie z jasnym komunikatem.
    * **And:** Po odzyskaniu połączenia system wznawia działanie, a czat synchronizuje brakujące wiadomości.

* **Scenariusz Bezpieczeństwa (Brak dostępu do cudzych kursów):**
    * **Given:** Użytkownik nie jest uczestnikiem kursu.
    * **When:** Próbuje otworzyć czat kursu przez bezpośredni link.
    * **Then:** System odmawia dostępu i nie ujawnia historii wiadomości.

* **Wymagania dostępności (konkretne, testowalne):**
    * **Given:** Użytkownik ma włączony ciemny motyw oraz preferencję ograniczenia animacji.
    * **When:** Otrzymuje powiadomienie i przewija historię czatu.
    * **Then:** System nie używa migających elementów ani wymuszonych animacji przewijania.
    * **And:** Kompozytor wiadomości i lista wiadomości są w pełni obsługiwalne klawiaturą.

---
## 4. Atrybuty Jakościowe

### 4.1. Wybór i Priorytetyzacja
1. **Użyteczność i dostępność (Prio 1):** Krytyczne, bo MVP ma być realnie używane przez osoby o różnym poziomie kompetencji i potrzebach dostępności (persona: Kamil, Teresa). Wymagania muszą być mierzalne, by dało się je przetestować.
2. **Bezpieczeństwo (Prio 2):** System przetwarza dane osobowe, oceny i prywatne wiadomości (RODO) – priorytetem jest ochrona przed nieautoryzowanym dostępem i audyt działań.
3. **Wydajność (Prio 3):** Najbardziej obciążające operacje (upload 200MB, listy oddań/wiadomości) nie mogą „zabijać” UX, bo to obniża aktywność i KPI.

### 4.2. Mierzalna specyfikacja (Scenariusze jakościowe dla TOP 3)

#### 4.2.1. Scenariusz jakościowy: Użyteczność i dostępność

| Element | Opis |
| :--- | :--- |
| **Źródło bodźca** | Nowy student oraz prowadząca z niską tolerancją na złożony UI. |
| **Bodziec** | Student dołącza do kursu i przesyła pierwsze oddanie; prowadząca publikuje zadanie i ogłoszenie. |
| **Artefakt** | UI modułu Kursy/Zadania/Materiały oraz nawigacja klawiaturą. |
| **Środowisko** | Desktop 1366×768, powiększenie tekstu 150%, włączony ciemny motyw, preferencja „reduced motion”. |
| **Reakcja** | System prowadzi użytkownika przez proces bez niejasnych komunikatów, zapewnia fokus i dostępność elementów oraz nie wymusza animacji. |
| **Miara reakcji** | (1) 100% kluczowych akcji MVP (dołączenie do kursu, upload zadania, start testu, odczyt oceny, odczyt ogłoszenia) dostępnych z klawiatury; (2) brak przewijania w poziomie w kluczowych ekranach przy 150%; (3) kontrast tekstu spełnia WCAG 2.1 AA; (4) test użyteczności: min. 4/5 badanych kończy „Dołącz + Wyślij zadanie” w ≤ 3 min bez pomocy. |

#### 4.2.2. Scenariusz jakościowy: Bezpieczeństwo

| Element | Opis |
| :--- | :--- |
| **Źródło bodźca** | Atakujący z zewnątrz oraz nieuprawniony użytkownik (student) próbujący uzyskać dane. |
| **Bodziec** | (A) Seria nieudanych prób logowania (brute-force). (B) Próba wejścia w zasób kursu przez bezpośredni link. |
| **Artefakt** | Moduł logowania/sesji, kontrola dostępu (RBAC), API kursów, moduł ocen i czatu. |
| **Środowisko** | Publiczny internet, normalne obciążenie (np. 100 aktywnych użytkowników). |
| **Reakcja** | System ogranicza próby logowania, rejestruje zdarzenia bezpieczeństwa i blokuje dostęp do zasobów niezgodny z rolą/członkostwem. |
| **Miara reakcji** | (1) Rate-limit/lockout po przekroczeniu progu (np. 10 prób/10 min) z rejestracją zdarzenia; (2) brak ujawnienia istnienia konta w komunikatach; (3) 100% prób dostępu do zasobów kursu bez członkostwa kończy się 403/404; (4) audyt: zapis „kto/co/kiedy” dla zmian ról i publikacji ocen. |

#### 4.2.3. Scenariusz jakościowy: Wydajność

| Element | Opis |
| :--- | :--- |
| **Źródło bodźca** | Wiele jednoczesnych akcji studentów na koniec terminu. |
| **Bodziec** | 50 studentów jednocześnie wysyła oddania (do 200MB) + 200 użytkowników przegląda listy zadań/wiadomości. |
| **Artefakt** | Endpointy uploadu, widok listy zadań/oddań, widok czatu, baza danych. |
| **Środowisko** | Szczytowe obciążenie (np. 250 aktywnych sesji), łącze użytkownika 20 Mbps, serwer klasy „free tier”. |
| **Reakcja** | System utrzymuje responsywność UI i nie „wiesza się” w kluczowych akcjach; upload jest odporny na przerwania i raportuje postęp. |
| **Miara reakcji** | (1) LCP ≤ 2.5 s dla 75 percentyla stron kluczowych (Kursy/Zadania/Czat) na desktop; (2) P95 czasu odpowiedzi dla list (zadania/oceny) ≤ 800 ms; (3) upload 200MB kończy się sukcesem u ≥ 95% prób przy stabilnym łączu, a przerwanie połączenia nie powoduje „fałszywego” statusu „Oddane”. |

### 4.3. Analiza kompromisów architektonicznych (dla TOP 3)

#### 4.3.1. Kompromisy dla „Użyteczność i dostępność”
* **Możliwe rozwiązanie:** Spójny design system (komponenty z widocznym fokusem), ograniczenie liczby kroków w procesach krytycznych, walidacja formularzy inline.
* **Kompromis:**
    * **Pozytywny:** Mniej błędów użytkownika i wyższa satysfakcja (KPIs).
    * **Negatywny:** Większy koszt implementacji UI/QA (więcej testów dostępności), wolniejsze tempo dodawania nowych funkcji.

#### 4.3.2. Kompromisy dla „Bezpieczeństwo”
* **Możliwe rozwiązanie:** Rate-limiting, audyt działań, zasada minimalnych uprawnień (RBAC), bezpieczne komunikaty błędów.
* **Kompromis:**
    * **Pozytywny:** Redukcja ryzyka wycieku danych i lepsza zgodność z RODO.
    * **Negatywny:** Potencjalnie gorszy UX w skrajnych przypadkach (np. czasowa blokada logowania), dodatkowa złożoność w backendzie.

#### 4.3.3. Kompromisy dla „Wydajność”
* **Możliwe rozwiązanie:** Ograniczenie ciężkich zapytań (paginacja, indeksy), asynchroniczny upload z paskiem postępu, cache dla często czytanych danych.
* **Kompromis:**
    * **Pozytywny:** Stabilny UX w szczycie obciążenia.
    * **Negatywny:** Większa złożoność (cache/inwalidacja), ryzyko niespójności danych i większy koszt utrzymania.

---

## 5. Analiza Porównawcza

### 5.1. Identyfikacja Konkurencji
* **Delta4** – poprzednia wersja wewnętrznego LMS uczelni.
* **Microsoft Teams** – platforma edukacyjna używana podczas pandemii.
* **Google Classroom** – popularny darmowy LMS.
* **Moodle** – standard w polskich uczelniach.

### 5.2. Tabela Porównawcza

| Cecha | Delta5 | Delta4 | MS Teams | Classroom | Moodle |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Czat real-time | ✅ | ✅ | ✅ | ❌ | ❌ |
| Auto-testy | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| Interfejs | Nowoczesny | Przestarzały | Przeładowany | Minimalny | Skomplikowany |
| Dostępność | WCAG 2.1 AA | Brak | Certyfikowane | Częściowe | Zależy od motywu |
| Koszt | Darmowy | N/A | 5$/user | Darmowy | Hosting płatny |
| Setup | <5 min | ~15 min | ~20 min | <3 min | >1h |

### 5.3. Kluczowe Wnioski

**Co konkurencja robi dobrze:**
* **Teams:** Pełna komunikacja (czat + wideo) + integracja z Microsoft 365.
* **Classroom:** Ekstremalnie prosty – setup <3 min.
* **Moodle:** Najbogatszy zestaw funkcji (1800+ pluginów).

**Słabe punkty konkurencji:**
* **Teams:** Wymaga licencji ($5/user) + integracji z Active Directory.
* **Classroom:** Brak czatu real-time – tylko komentarze.
* **Moodle:** Setup >1h, skomplikowane menu.
* **Delta4:** Brak accessibility.

**Unikalna wartość Delta5:**
* Real-time komunikacja (jak Teams) + prostota (jak Classroom) + darmowy self-hosting (jak Moodle) + accessibility (WCAG 2.1 AA).
* **Segment docelowy:** Małe uczelnie (50-500 studentów), które potrzebują prostszego narzędzia niż Moodle, ale nie stać ich na Teams.

**Świadome braki:**
* Brak natywnych aplikacji mobilnych.
* Brak wideokonferencji (wymaga zewnętrznego narzędzia).
* Brak pluginów/integracji.

---
