from django.urls import path
from Owner_Book import views

# from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addowner/', views.addowner, name='addowner'),
    path('addbook/', views.addBook, name='addbook'),
    path('viewowner/', views.viewOwner, name='viewowner'),
    path('booklist/<int:id>/', views.bookList, name='booklist'),
    path('bookdetails/<int:book_id>/<stor_id>/', views.bookDetails, name='bookdetails'),
]