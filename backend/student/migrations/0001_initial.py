# Generated by Django 5.0.6 on 2024-06-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('grade', models.IntegerField(max_length=100, null=True)),
                ('no_of_books_checked_in', models.IntegerField(max_length=13, null=True)),
                ('timeStamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
