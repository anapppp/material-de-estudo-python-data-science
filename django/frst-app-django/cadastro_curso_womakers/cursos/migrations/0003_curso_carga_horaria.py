# Generated by Django 4.2.11 on 2024-03-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_curso_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='carga_horaria',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
