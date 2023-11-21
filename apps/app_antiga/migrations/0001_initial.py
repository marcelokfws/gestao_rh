# Generated by Django 4.2.7 on 2023-11-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuarios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'registro_usuarios',
            },
        ),
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
            ],
        ),
    ]
