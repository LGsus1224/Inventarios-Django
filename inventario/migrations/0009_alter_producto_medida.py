# Generated by Django 5.0.7 on 2024-09-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_proveedor_informacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='medida',
            field=models.CharField(choices=[('1', 'sacos'), ('2', 'kg'), ('3', 'lb'), ('4', 'arrobas')], default='1', max_length=20),
        ),
    ]
