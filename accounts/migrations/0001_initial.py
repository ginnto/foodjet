# Generated by Django 2.2 on 2022-05-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, unique=True)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('password1', models.IntegerField()),
                ('password2', models.IntegerField()),
            ],
        ),
    ]
