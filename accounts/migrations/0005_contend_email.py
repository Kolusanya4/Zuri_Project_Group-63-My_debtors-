# Generated by Django 4.1.4 on 2022-12-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_contend'),
    ]

    operations = [
        migrations.AddField(
            model_name='contend',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
    ]
