# Generated by Django 4.0.1 on 2022-01-19 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blahaj',
            fields=[
                ('BlahajId', models.AutoField(primary_key=True, serialize=False)),
                ('BlahajName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UsersId', models.AutoField(primary_key=True, serialize=False)),
                ('UsersName', models.CharField(max_length=500)),
                ('Blahaj', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
    ]
