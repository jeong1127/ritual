# Generated by Django 4.0.4 on 2022-04-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_remove_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
    ]
