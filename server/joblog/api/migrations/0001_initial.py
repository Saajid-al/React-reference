# Generated by Django 5.1.2 on 2024-10-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobLink', models.CharField(max_length=10000000)),
                ('dateApplied', models.IntegerField()),
            ],
        ),
    ]
