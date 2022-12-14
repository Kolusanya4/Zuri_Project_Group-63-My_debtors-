# Generated by Django 4.1.4 on 2022-12-11 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=600)),
                ('phone', models.IntegerField(default=234)),
                ('address', models.CharField(blank=True, max_length=700)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debtors_name', models.CharField(max_length=100)),
                ('debt_amount', models.IntegerField()),
                ('debt_paid_amt', models.IntegerField()),
                ('post_status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Active', max_length=60)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('school_owner', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='accounts.schoolowner')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment_name', models.CharField(max_length=100)),
                ('Comment_body', models.TextField()),
                ('comment_date_created', models.DateTimeField(auto_now_add=True)),
                ('comment_post', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.post')),
            ],
        ),
    ]
