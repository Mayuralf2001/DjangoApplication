# Generated by Django 3.0.2 on 2022-06-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=100)),
                ('sage', models.CharField(max_length=10)),
                ('scity', models.CharField(max_length=100)),
                ('sclass', models.CharField(max_length=100)),
            ],
        ),
    ]
