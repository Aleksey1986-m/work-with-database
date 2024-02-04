# Generated by Django 5.0.1 on 2024-02-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
