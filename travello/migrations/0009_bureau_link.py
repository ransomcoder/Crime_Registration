# Generated by Django 3.0.2 on 2020-01-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0008_auto_20200127_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='bureau',
            name='link',
            field=models.TextField(default=''),
        ),
    ]
