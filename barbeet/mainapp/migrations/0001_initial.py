# Generated by Django 2.2.5 on 2020-05-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pixels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.IntegerField()),
            ],
        ),
    ]