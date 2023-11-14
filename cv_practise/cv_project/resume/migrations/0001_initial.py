# Generated by Django 4.2.7 on 2023-11-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('summary', models.TextField(max_length=2000)),
                ('degree', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=500)),
                ('previous_work', models.TextField(max_length=2000)),
                ('skills', models.TextField(max_length=2000)),
                ('strength', models.TextField(max_length=2000)),
                ('project', models.TextField(max_length=2000)),
                ('address', models.TextField(max_length=2000)),
                ('nationalityy', models.CharField(max_length=200)),
                ('blood_group', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
        ),
    ]