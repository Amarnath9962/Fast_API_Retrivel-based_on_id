# Generated by Django 5.0.2 on 2024-02-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('ssc_score', models.IntegerField()),
                ('percentage', models.IntegerField()),
                ('speciliation', models.CharField(max_length=100)),
                ('degree_score', models.IntegerField()),
                ('company', models.CharField(max_length=100, null=True)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
