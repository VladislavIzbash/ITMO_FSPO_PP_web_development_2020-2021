# Generated by Django 3.1.7 on 2021-03-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passport',
            field=models.CharField(default=5238690201, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]