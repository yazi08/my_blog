# Generated by Django 3.1.7 on 2021-04-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_messages', '0004_auto_20210429_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description_blog',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]