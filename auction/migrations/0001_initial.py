# Generated by Django 2.2.2 on 2019-06-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_stop', models.DateTimeField(blank=True)),
                ('description', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('photo', models.ManyToManyField(to='auction.Photo')),
            ],
        ),
    ]