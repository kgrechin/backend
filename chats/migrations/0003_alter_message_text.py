# Generated by Django 4.2 on 2023-04-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(default='asasas'),
            preserve_default=False,
        ),
    ]
