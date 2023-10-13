from django.http import HttpResponse
from .models import Book

def home(request):
    books = Book.objects.all()

    for book in books: 
        if book.id % 2 != 0:
            book.delete()
    
    return HttpResponse(content="Odd books has been successfully deleted!")
