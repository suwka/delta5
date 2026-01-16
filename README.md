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

### 2.2. Klasy Użytkowników i Persony
* **Student:** Skupiony na terminowości i intuicyjnej obsłudze mobilnej/desktopowej.
* **Prowadzący:** Kluczowy użytkownik zarządzający treścią i ocenami.
* **Persony (MVP):**
    * **Kamil, 22 lata — student z niepełnosprawnością (dostępność jako warunek konieczny).**
        * **Kontekst:** Studiuje dziennie, dużo pracuje wieczorami. Ma obniżoną ostrość wzroku i nadwrażliwość na bodźce (w tym migotanie / intensywne animacje).
        * **Cele:** Szybko odnaleźć zadania i terminy, bezbłędnie wysłać pliki, sprawdzić wyniki testów.
        * **Potrzeby dostępności:** możliwość zwiększenia rozmiaru tekstu (min. 120–150%), stabilny **ciemny motyw** o wysokim kontraście, ograniczenie animacji (preferencja „reduced motion”), pełna obsługa klawiaturą.
        * **Ryzyka/obawy:** przypadkowe ukrycie ważnych informacji (np. terminów), niedostępne komponenty (brak focus state), zbyt małe elementy klikalne.
    * **Teresa, 61 lat — prowadząca ceniąca prostotę i przewidywalność.**
        * **Kontekst:** Prowadzi kilka grup, nie chce „walczyć z narzędziem”. Często pracuje na laptopie z touchpadem.
        * **Cele:** Jednym miejscem zarządzić kursem (harmonogram, zadania, testy), szybko zobaczyć kto oddał i jakie są wyniki.
        * **Preferencje UX:** proste, jednoznaczne etykiety i komunikaty, mało kroków, domyślne ustawienia „bezpieczne”, brak ukrytych akcji.
        * **Ryzyka/obawy:** pomyłkowe opublikowanie testu/zadania, trudne do znalezienia ustawienia, zbyt techniczne błędy.

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
| Zarządzanie kursem | 13 | 13 | 5 | 3 | **3.25** |
| Przesyłanie zadań | 21 | 13 | 3 | 2 | **6.80** |
| Automatyczne testy | 13 | 5 | 8 | 5 | **1.38** |
| Czat Real-time | 8 | 3 | 13 | 8 | **0.52** |

### 3.2. Szczegółowe Wymagania

Poniższe wymagania odpowiadają pozycjom z tabeli priorytetów (Rozdział 3.1). Każde wymaganie zawiera user story oraz **mocno rozpisane** kryteria akceptacji w stylu BDD (Given/When/Then), w tym scenariusze alternatywne i wyjątkowe.

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
1. **Użyteczność (Prio 1):** Intuicyjna obsługa zachęca do regularnego korzystania.
2. **Wydajność (Prio 2):** LCP (Largest Contentful Paint - metryka wydajności określająca czas załadowania największego widocznego elementu) poniżej 2.5s, aby nie zniechęcać użytkowników.
3. **Bezpieczeństwo (Prio 3):** Ochrona danych osobowych (RODO) i ocen.

### 4.2. Scenariusz Jakościowy (Wydajność)
* **Źródło bodźca:** Użytkownik (Student).
* **Bodziec:** Przesłanie projektu (paczka .zip 200MB).
* **Środowisko:** Szczytowe obciążenie na koniec semestru.
* **Miara reakcji:** Operacja zakończona sukcesem w mniej niż 4 krokach od zalogowania.

### 4.3. Analiza Kompromisów
* **Kompromis:** Rezygnacja z mikroserwisów na rzecz monolitu.
* **Wpływ:** Poprawa **Wydajności** i szybkości wdrożenia kosztem przyszłej **Skalowalności**.

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
