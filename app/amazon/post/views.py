from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_author_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_success')  # Redirect to a named URL
    else:
        form = AuthorForm()
    
    return render(request, 'add_author.html', {'form': form})

def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_success')  # Redirect to a named URL
    else:
        form = BookForm()
    
    return render(request, 'add_book.html', {'form': form})

# my_app/views.py

def author_success_view(request):
    return render(request, 'author_success.html')

def book_success_view(request):
    return render(request, 'book_success.html')

# my_app/views.py



def author_list_view(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_update_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})

def author_delete_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_confirm_delete.html', {'object': author})

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'object': book})
def save(request):
    name=request.POST['uname']