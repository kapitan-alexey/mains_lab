# Generated by Django 4.0.6 on 2022-07-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256)),
                ('fraud_weight', models.IntegerField(default=0)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mains_rest.clients')),
            ],
            options={
                'unique_together': {('name', 'client_name')},
            },
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('sum', models.FloatField()),
                ('date', models.DateField()),
                ('service', models.CharField(max_length=128)),
                ('fraud_score', models.FloatField()),
                ('service_class', models.IntegerField()),
                ('service_name', models.CharField(max_length=64)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mains_rest.clients')),
                ('client_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mains_rest.organizations')),
            ],
            options={
                'unique_together': {('client_org', 'number')},
            },
        ),
    ]
