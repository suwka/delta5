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
* **Persona (Dodatek B):** Marek (student potrzebujący szybkości) oraz Anna (wykładowczyni ceniąca automatyzację).

### 2.3. Ograniczenia Projektowe
* **Techniczne:** Wybór Django, React i PostgreSQL determinuje architekturę API-first.
* **Organizacyjne:** Realizacja MVP w 3 miesiące przez dwóch studentów.
* **Budżetowe:** Ograniczenie do bezpłatnych subskrypcji oraz planów studenckich narzędzi i modeli AI.

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

* **Scenariusz Alternatywny (Błędne odpowiedzi):**
    * **Given:** Student wypełnił test, ale zaznaczył większość błędnych odpowiedzi.
    * **When:** Student zatwierdza formularz.
    * **Then:** System pokazuje niski wynik punktowy.
    * **And:** System NIE wyświetla poprawnych odpowiedzi (aby zapobiec przekazywaniu ich innym studentom), jeśli prowadzący włączył opcję "Ukryj klucz".

* **Scenariusz Wyjątkowy (Zerwanie połączenia):**
    * **Given:** Student jest w trakcie rozwiązywania testu.
    * **When:** Użytkownik traci połączenie z internetem w momencie kliknięcia "Wyślij".
    * **Then:** System wyświetla komunikat o błędzie sieci ("Brak połączenia").
    * **And:** System umożliwia ponowną próbę wysłania odpowiedzi po odzyskaniu połączenia, bez utraty zaznaczonych wcześniej opcji.

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
| Cecha | Delta5 | Delta4 | MS Teams |
| :--- | :--- | :--- | :--- |
| **UX** | Nowoczesny, ergonomiczny | Przestarzały | Korporacyjny |
| **Komunikacja** | Czat wbudowany | Brak real-time | Zewnętrzny moduł |
| **Ocenianie** | Auto-testy i statystyki | Skomplikowane tabele | Podstawowe |

---
