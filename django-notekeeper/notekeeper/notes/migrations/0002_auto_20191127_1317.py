# Generated by Django 2.2.7 on 2019-11-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
