# Generated by Django 3.1.7 on 2021-03-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('CRE', 'Created'), ('PRG', 'In Progress'), ('CMP', 'Completed')], default='CRE', max_length=3)),
                ('content', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(max_length=200)),
            ],
        ),
    ]