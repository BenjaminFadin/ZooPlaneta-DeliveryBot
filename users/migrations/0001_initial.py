# Generated by Django 5.0.3 on 2024-03-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('tg_user_id', models.PositiveIntegerField(unique=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('lang', models.CharField(blank=True, choices=[('uz', 'uz'), ('ru', 'ru')], max_length=2, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=30, null=True)),
                ('first_name', models.CharField(max_length=25, null=True)),
                ('last_name', models.CharField(max_length=25, null=True)),
            ],
            options={
                'ordering': ('-created_time',),
                'abstract': False,
            },
        ),
    ]
