# Generated by Django 3.2 on 2022-02-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='loaction_maptxt',
            field=models.CharField(blank=True, help_text='loaction map url of your project', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, choices=[('ON', 'Ongoing'), ('CM', 'Commercial'), ('CO', 'Complated')], max_length=2, null=True),
        ),
    ]