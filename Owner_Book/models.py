from django.db import models


# Create your models here.
class Owner(models.Model):
    GENDER_CHOICES = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('TRANS_GENDER', 'TRANS GENDER')]
    firstname = models.CharField(max_length=50, verbose_name="First Name")
    lastname = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phoneNumber = models.CharField(max_length=15, unique=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='MALE', verbose_name="Gender")

    def __str__(self):
        return self.firstname + " " + self.lastname


class Book(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, default=None, verbose_name="Owner")
    book_name = models.CharField(max_length=100, verbose_name="Book Name")
    writer_name = models.CharField(max_length=100, verbose_name="Writer Name")

    def __str__(self):
        return self.owner.firstname + " -> " + self.book_name
