from django.db import models

class WynikTestu(models.Model):
    student = models.CharField(max_length=100, default="Student") # Uproszczenie: wpisujemy nazwę ręcznie lub automat
    wynik_procent = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student}: {self.wynik_procent}%"