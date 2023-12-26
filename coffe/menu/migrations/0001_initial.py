# Generated by Django 5.0 on 2023-12-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled', max_length=255)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
