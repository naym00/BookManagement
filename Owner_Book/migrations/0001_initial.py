# Generated by Django 3.1.3 on 2021-10-31 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First Name', models.CharField(max_length=50, verbose_name='First Name')),
                ('LAst Name', models.CharField(max_length=50, verbose_name='LAst Name')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Phone Number', models.CharField(max_length=15, unique=True, verbose_name='Phone Number')),
                ('Gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('TRANS_GENDER', 'TRANS GENDER')], default='MALE', max_length=20, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book Name', models.CharField(max_length=100, verbose_name='Book Name')),
                ('Writer Name', models.CharField(max_length=100, verbose_name='Writer Name')),
                ('Owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Owner_Book.owner', verbose_name='Owner')),
            ],
        ),
    ]