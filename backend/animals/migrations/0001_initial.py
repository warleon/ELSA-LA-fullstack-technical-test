# Generated by Django 5.1 on 2024-08-22 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shelters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('inscription_date', models.DateTimeField(auto_now_add=True)),
                ('age_at_inscription', models.IntegerField()),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelters.shelter')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.breed')),
            ],
        ),
        migrations.AddField(
            model_name='breed',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.specie'),
        ),
    ]
