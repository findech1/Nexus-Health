# Generated by Django 3.2.12 on 2024-05-31 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticsrecord',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_records', to='appointments.appointment'),
        ),
    ]
