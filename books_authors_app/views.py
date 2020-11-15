from django.shortcuts import render, redirect
from books_authors_app.models import Book, Author

def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request,'index.html',context)

def create_book(request):
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
    )
    return redirect('/')

def display_book(request, book_id):
    context = {
        "book": Book.objects.get(id = book_id),
        "authors": Author.objects.exclude(books__id = book_id),
    }
    return render(request, "book.html", context)

def update_book(request, book_id): 
    if request.POST["add_author"] == "":
        return redirect(f"/book/{book_id}")
    else:
        book = Book.objects.get(id = book_id)
        author = Author.objects.get (id = request.POST["add_author"])
        book.authors.add(author)
        book.save()
        return redirect(f"/book/{book_id}")

def author_index(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request,"author.html",context)

def create_author(request):
    Author.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        notes = request.POST['notes'],
    )
    return redirect('/authors')

def display_author(request, author_id):
    context = {
        "author": Author.objects.get(id = author_id),
        "books": Book.objects.exclude(authors__id = author_id),
    }
    return render(request, "author_page.html", context)

def update_author(request, author_id): 
    if request.POST["add_book"] == "":
        return redirect(f"/author/{author_id}")
    else:
        author = Author.objects.get(id = author_id)
        book = Book.objects.get (id = request.POST["add_book"])
        author.books.add(book)
        author.save()
        return redirect(f"/author/{author_id}")

def delete_book(request, book_id):
    del_book = Book.objects.get(id = book_id)
    del_book.delete()
    return redirect('/')

def delete_author(request, author_id):
    del_author = Author.objects.get(id = author_id)
    del_author.delete()
    return redirect('/authors')