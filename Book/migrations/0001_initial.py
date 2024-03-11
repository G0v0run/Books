# Generated by Django 4.2 on 2023-09-17 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('compositors', models.CharField(max_length=200)),
                ('available', models.BooleanField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'sheets',
            },
        ),
        migrations.CreateModel(
            name='SheetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Koots.sheets')),
            ],
            options={
                'db_table': 'sheet_images',
            },
        ),
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('sheets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Koots.sheets')),
            ],
            options={
                'db_table': 'buyers',
            },
        ),
    ]
