# Generated by Django 3.1.7 on 2021-05-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210508_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=25000),
        ),
    ]