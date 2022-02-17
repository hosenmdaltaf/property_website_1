# Generated by Django 3.2 on 2022-02-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_auto_20220208_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='categories',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, choices=[('ON', 'Ongoing'), ('CM', 'Commercial'), ('CO', 'Complated')], max_length=2, null=True),
        ),
    ]