# Generated by Django 4.0.3 on 2022-03-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.TextField(max_length=200)),
                ('ultimo_nome', models.TextField(blank=True, max_length=200)),
                ('alcunha', models.TextField(blank=True, max_length=200)),
                ('golos', models.BigIntegerField(blank=True)),
                ('assistencias', models.BigIntegerField(blank=True)),
            ],
        ),
    ]
