# Generated by Django 5.2 on 2025-04-14 21:59

import livros.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='ano_publicacao',
            field=models.PositiveIntegerField(default=2000, validators=[livros.models.validar_ano]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livro',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
