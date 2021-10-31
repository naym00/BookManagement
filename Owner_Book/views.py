from django.shortcuts import render, redirect
from .models import Owner, Book
from .forms import OwnerForm, BookForm
from .phonenumbersvalidity import checkNumber


# Create your views here.
def home(request):
    context = {"text": "This is home page"}
    return render(request, 'Owner_Book/home.html', context)


def addowner(request):
    form = OwnerForm()
    text = ""
    textForPhoneNumber = ""
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            phoneNumber = request.POST['phoneNumber']
            if checkNumber(phoneNumber) == 1:
                form.save()
                return redirect('addbook')
            else:
                textForPhoneNumber = "Please type a valid phone number."
        else:
            text = "Not Successful!"

    context = {"form": form, "text": text, "textForPhoneNumber": textForPhoneNumber}
    return render(request, 'Owner_Book/addowner.html', context)


def addBook(request):
    form = BookForm()
    text = ""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            text = "Not Successful!"

    context = {"form": form, "text": text}
    return render(request, 'Owner_Book/addBook.html', context)


def viewOwner(request):
    headLine = "Owner List"
    owner = Owner.objects.all()
    # owner = Owner.objects.order_by("-id") # Descending order
    context = {"headLine": headLine, "owner": owner}
    return render(request, 'Owner_Book/viewOwner.html', context)


def bookList(request, id):
    headLine = "Book List"
    owner = Owner.objects.get(pk=id)
    books = Book.objects.filter(owner=id).order_by('book_name')

    context = {"headLine": headLine, "owner": owner, "books": books, "id": id}
    return render(request, 'Owner_Book/bookList.html', context)


def bookDetails(request, book_id, stor_id):
    headLine = "Book Information"
    book = Book.objects.get(pk=book_id)
    context = {"headLine": headLine, "book": book, "stor_id": stor_id}
    return render(request, 'Owner_Book/bookdetails.html', context)
