# Generated by Django 5.1.4 on 2024-12-28 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('father', '0008_alter_element_bucket_alter_element_galon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='bucket',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='galon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='half_kilo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='kes',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='kilo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
