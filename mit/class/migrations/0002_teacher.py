# Generated by Django 3.2.12 on 2024-02-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]