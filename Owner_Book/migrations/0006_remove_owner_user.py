# Generated by Django 3.1.3 on 2021-10-31 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Owner_Book', '0005_auto_20211101_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
    ]
