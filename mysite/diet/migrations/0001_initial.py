# Generated by Django 4.1.6 on 2023-02-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('meal', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert'), ('Midnight Snack', 'Midnight Snack')], default='Breakfast', max_length=20)),
                ('food', models.CharField(max_length=50)),
                ('calorie', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
