# Generated by Django 5.1.6 on 2025-03-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_stage_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='stage',
            field=models.CharField(choices=[('ORC', 'Orçamento e aprovação'), ('COR', 'Corte de materiais'), ('LIX', 'Lixamento e preparação'), ('MON', 'Montagem estrutural'), ('PNT', 'Acabamento e pintura'), ('SEC', 'Secagem e ajustes finais'), ('REV', 'Revisão e controle de qualidade'), ('ENT', 'Pronto para retirada/entrega')], max_length=3),
        ),
    ]
