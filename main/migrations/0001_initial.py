# Generated by Django 3.1.1 on 2020-11-01 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Yangilik Sarlavhasi:')),
                ('about', models.TextField(verbose_name='Yangilik Haqida:')),
                ('datetime', models.DateTimeField(verbose_name='Yangilik Qoyilgan Vaqti')),
            ],
        ),
        migrations.CreateModel(
            name='Pupils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300, verbose_name="O'quvchining ismi ")),
                ('last_name', models.CharField(max_length=300, verbose_name="O'quvchining familyasi ")),
                ('subject_name', models.CharField(max_length=300, verbose_name='Tanlangan Fan')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon raqami:')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='media/', verbose_name='Birinchi Rasm:')),
                ('image2', models.ImageField(upload_to='media/', verbose_name='Birinchi Rasm:')),
                ('image3', models.ImageField(upload_to='media/', verbose_name='Birinchi Rasm:')),
                ('facebook', models.CharField(max_length=250, verbose_name='Facebook')),
                ('instagram', models.CharField(max_length=250, verbose_name='Instagram')),
                ('telegram', models.CharField(max_length=250, verbose_name='Telegram')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250, verbose_name='Fan Nomi')),
                ('about', models.TextField(verbose_name='Fan haqida')),
                ('price', models.IntegerField(verbose_name='Kurs narxi')),
                ('num', models.IntegerField(verbose_name='Kurs Soni')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ism')),
                ('img', models.ImageField(upload_to='media/')),
                ('facebook', models.CharField(max_length=250, verbose_name='Facebook')),
                ('instagram', models.CharField(max_length=250, verbose_name='Instagram')),
                ('telegram', models.CharField(max_length=250, verbose_name='Telegram')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.subject', verbose_name='Series')),
            ],
        ),
    ]
