# Generated by Django 5.0.1 on 2024-01-25 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(max_length=15)),
                ('image', models.FileField(upload_to='students/')),
                ('student_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('author_name', models.CharField(max_length=1000)),
                ('no_of_copies', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.category')),
            ],
        ),
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_at', models.DateField()),
                ('returned_at', models.DateField(blank=True, null=True)),
                ('is_returned', models.BooleanField(default=False)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.book')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.student')),
            ],
        ),
    ]
