from django.contrib import admin
from books.models import *


class BooksAdmin(admin.ModelAdmin):
    list_display = ["name" , "price" , "reservation"]
    search_fields = ["name"]

class ReserveAdmin(admin.ModelAdmin):
    list_display = ["user", "book", "start_reserve", "end_reserve"]

class WaitingAdmin(admin.ModelAdmin):
    list_display = ["user" , "book"]


admin.site.register(All_books , BooksAdmin)
admin.site.register(Reserv)
admin.site.register(Waitinglist, WaitingAdmin)