# Generated by Django 5.1.4 on 2024-12-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('father', '0005_alter_element_bucket_alter_element_galon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]