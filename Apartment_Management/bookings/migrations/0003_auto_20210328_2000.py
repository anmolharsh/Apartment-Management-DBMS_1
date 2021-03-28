# Generated by Django 3.1.7 on 2021-03-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20210328_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('WAIT', 'WAITING FOR APPROVAL'), ('ALOT', 'ALLOTTED'), ('REJC', 'REJECTED')], default='WAIT', max_length=4),
        ),
    ]