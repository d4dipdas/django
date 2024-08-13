# my_app/forms.py

from django import forms
from .models import Author
from .models import Book
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthdate']
        # You can also specify widgets if needed
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn']
        # You can also specify widgets if needed
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
