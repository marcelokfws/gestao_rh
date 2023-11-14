# Generated by Django 4.2.7 on 2023-11-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_alter_funcionario_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='de_ferias',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]