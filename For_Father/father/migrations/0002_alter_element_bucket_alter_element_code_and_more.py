# Generated by Django 5.1 on 2024-12-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('father', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='bucket',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='galon',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='half_kilo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='kes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='kilo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
