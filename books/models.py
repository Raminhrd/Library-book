from django.db import models
from django.contrib.auth.models import User



class All_books(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    reservation = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Reserv(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    book = models.ForeignKey( All_books, on_delete=models.CASCADE)
    start_reserve = models.DateTimeField()
    end_reserve = models.DateTimeField()
    def __str__(self):
        return f"{self.user.username} have {self.book.name}"


class Waitinglist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey( All_books, on_delete=models.CASCADE)
    start_reserve = auto_add_now=True