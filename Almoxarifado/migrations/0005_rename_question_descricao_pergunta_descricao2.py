# Generated by Django 4.0.4 on 2022-05-11 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Almoxarifado', '0004_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descricao',
            old_name='question',
            new_name='pergunta',
        ),
        migrations.CreateModel(
            name='Descricao2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twxto_mun', models.TextField(max_length=10000)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Almoxarifado.pergunta')),
            ],
        ),
    ]
