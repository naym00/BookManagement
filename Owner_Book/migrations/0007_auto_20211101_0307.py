# Generated by Django 3.1.3 on 2021-10-31 21:07

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Owner_Book', '0006_remove_owner_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(default=builtins.id, on_delete=django.db.models.deletion.CASCADE, to='Owner_Book.owner', verbose_name='Owner'),
        ),
    ]