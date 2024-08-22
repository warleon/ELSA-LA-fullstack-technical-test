# Generated by Django 5.1 on 2024-08-22 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('inscription_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.person')),
            ],
        ),
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.person')),
            ],
        ),
    ]
