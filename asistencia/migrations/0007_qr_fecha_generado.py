# Generated by Django 5.0.6 on 2024-05-21 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0006_qr_id_alum_mat_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='fecha_generado',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 20, 19, 59, 55, 43810), editable=False),
        ),
    ]
