# Generated by Django 5.0.2 on 2024-03-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='goal_category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]