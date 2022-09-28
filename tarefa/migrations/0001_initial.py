# Generated by Django 4.1.1 on 2022-09-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=65)),
                ('feita', models.BooleanField(default=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
