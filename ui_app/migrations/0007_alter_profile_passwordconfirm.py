# Generated by Django 3.2.9 on 2021-12-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_app', '0006_profile_passwordconfirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='passwordConfirm',
            field=models.CharField(default='none', max_length=15),
        ),
    ]
