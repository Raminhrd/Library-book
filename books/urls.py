from django.urls import path
from books.views  import show_all_books, reserve_books

urlpatterns = [
    path('book-list/', show_all_books),
    path('reserve-book/', reserve_books)
]