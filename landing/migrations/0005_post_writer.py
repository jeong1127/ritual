# Generated by Django 4.0.4 on 2022-04-26 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_tempuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.tempuser'),
        ),
    ]
