# Generated by Django 3.0.7 on 2020-06-17 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('run_date', models.DateTimeField(verbose_name='date submitted')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Submission')),
            ],
        ),
    ]
