from django import forms
from .models import Owner, Book


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
