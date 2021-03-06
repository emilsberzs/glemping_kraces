# Generated by Django 3.1.5 on 2021-02-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glemping', '0015_auto_20210205_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone_number',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='surname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
