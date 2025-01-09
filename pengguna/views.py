from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json

# Create your views here.
@csrf_exempt
def book_list(request):
    try:
        if request.method == 'GET':
            books = Book.objects.all()
            books_list = list(books.values())
            return JsonResponse(books_list, safe=False)
        elif request.method == 'POST':
            data = json.loads(request.body)
            book = Book.objects.create(**data)
            return JsonResponse({'message': 'success insert book','id': book.id}, status=201)
    except Exception as e:
        return JsonResponse({'message': 'Error', 'error': e.args}, status=400)

@csrf_exempt
def book_detail(request, pk):
    try:
        book = get_object_or_404(Book, pk=pk)
        if request.method == 'GET':
            return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date})
        elif request.method == 'PUT':
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            return JsonResponse({'message': 'success', 'id': book.id})
        elif request.method == 'DELETE':
            book.delete()
            return JsonResponse({'message': 'success'}, status=204)
    except Exception as e:
        return JsonResponse({'message': 'Error', 'error': e.args}, status=400)
