# Generated by Django 5.0.3 on 2024-03-06 00:02

import produto.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=65)),
                ('descrição', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('quantidade', models.IntegerField(default=0)),
                ('imagem', models.ImageField(blank=True, upload_to=produto.models.get_upload_path)),
            ],
        ),
    ]
