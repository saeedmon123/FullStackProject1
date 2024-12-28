# Generated by Django 5.1.4 on 2024-12-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('date', models.DateField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=255)),
                ('bucket', models.IntegerField()),
                ('galon', models.IntegerField()),
                ('kilo', models.IntegerField()),
                ('half_kilo', models.IntegerField()),
                ('kes', models.IntegerField()),
            ],
        ),
    ]