# Generated by Django 4.1.4 on 2022-12-11 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_comment_school_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='post_school',
        ),
        migrations.RemoveField(
            model_name='school',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_school',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
