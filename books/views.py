from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from books.models import All_books , Reserv , Waitinglist
from django.utils import timezone
from datetime import timedelta



def show_all_books(request):
    books = All_books.objects.all().values('name' , 'price' , 'reservation')
    books_list = list(books)
    return JsonResponse(books_list , safe = False)

def reserve_books(request):
    book_id = request.GET.get('book_id')

    try:
        book = All_books.objects.get(id=book_id)
    except All_books.DoesNotExist:
        return JsonResponse({"status": "Error", "message": "No have book for this name"})
    except ValueError:
        return JsonResponse({"status": "Error", "message": "id is not ok"})

    reserve_check = Reserv.objects.filter(book=book)
    if reserve_check.count() < book.reservation:
        book.reservation -=1
        book.save()
        Reserv.objects.create(
            user=request.user,
            book=book,
            start_reserve=timezone.now(),
            end_reserve=timezone.now() + timedelta(days=7)
        )
        return JsonResponse({"status": "Success", "message": "book Reserved for you"})
    else:
        Waitinglist.objects.create(user=request.user, book=book)
        return JsonResponse({"status": "Full", "message": "Capcity is full, your name have saved for list"})
