# Generated by Django 4.0.6 on 2022-10-26 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEcoindustry', '0008_alter_agenda_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='placa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appEcoindustry.vehiculo'),
            preserve_default=False,
        ),
    ]
