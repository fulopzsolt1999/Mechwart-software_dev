# Generated by Django 5.0.4 on 2024-04-06 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Szak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('szakNev', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Felvetelizo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=100)),
                ('szul_ev', models.IntegerField()),
                ('pontszam', models.IntegerField()),
                ('szak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='felviadmin.szak')),
            ],
        ),
    ]
