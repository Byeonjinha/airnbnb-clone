# Generated by Django 2.2.5 on 2022-02-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='accuracy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='check_in',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='cleanLiness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='communication',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.IntegerField(),
        ),
    ]
