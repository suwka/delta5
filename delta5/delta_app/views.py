from django.shortcuts import render
from .models import WynikTestu

# 1. DANE TESTOWE (Zaszyte na sztywno - symulacja bazy danych)
QUIZ_DATA = [
    {
        'id': 'q1',
        'pytanie': 'Co oznacza skrót MVP w IT?',
        'opcje': [
            ('a', 'Most Valuable Player'),
            ('b', 'Minimum Viable Product'), # Poprawna
            ('c', 'Maximum Virtual Protocol')
        ],
        'poprawna': 'b'
    },
    {
        'id': 'q2',
        'pytanie': 'Jaka jest rola pliku views.py w Django?',
        'opcje': [
            ('a', 'Przechowuje hasła do bazy'),
            ('b', 'Definiuje wygląd strony (HTML)'),
            ('c', 'Zawiera logikę biznesową i steruje działaniem'), # Poprawna
        ],
        'poprawna': 'c'
    },
    {
        'id': 'q3',
        'pytanie': 'Jaki status HTTP oznacza "Brak dostępu"?',
        'opcje': [
            ('a', '403 Forbidden'), # Poprawna
            ('b', '200 OK'),
            ('c', '404 Not Found')
        ],
        'poprawna': 'a'
    }
]

# 2. FUNKCJA OBSŁUGUJĄCA TEST
def rozwiaz_test(request):
    # Scenariusz 1: Użytkownik wysłał formularz (POST) -> SPRAWDZAMY
    if request.method == 'POST':
        punkty = 0
        total = len(QUIZ_DATA)

        # Algorytm sprawdzający
        for pytanie in QUIZ_DATA:
            # Pobieramy odpowiedź zaznaczoną przez usera dla danego ID pytania
            odpowiedz_studenta = request.POST.get(pytanie['id'])
            
            if odpowiedz_studenta == pytanie['poprawna']:
                punkty += 1
        
        # Obliczenie procentów
        wynik_procent = int((punkty / total) * 100)

        # Pobieramy imię studenta
        imie_studenta = request.POST.get('imie', 'Anonim')

        # Zapis do bazy (trwałe świadectwo wykonania zadania)
        WynikTestu.objects.create(student=imie_studenta, wynik_procent=wynik_procent)

        # Wyświetlenie wyniku (prosty render bez osobnego pliku HTML)
        return render(request, 'quiz.html', {
            'pokaz_wynik': True,
            'wynik': wynik_procent,
            'punkty': punkty,
            'total': total,
            'imie': imie_studenta
        })

    # Scenariusz 2: Wejście na stronę (GET) -> WYŚWIETLAMY PYTANIA
    return render(request, 'quiz.html', {'pytania': QUIZ_DATA})