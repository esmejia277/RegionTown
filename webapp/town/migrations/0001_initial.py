# Generated by Django 2.2.4 on 2019-08-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Código')),
                ('name_town', models.CharField(max_length=100, verbose_name='Nombre')),
                ('status', models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipio',
                'ordering': ['-name_town'],
            },
        ),
    ]
