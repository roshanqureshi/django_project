# Generated by Django 4.1 on 2022-09-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.IntegerField()),
            ],
        ),
    ]
