# Generated by Django 2.2.19 on 2023-01-20 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]