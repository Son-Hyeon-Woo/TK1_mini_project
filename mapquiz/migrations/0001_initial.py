# Generated by Django 2.2.5 on 2022-01-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_name', models.CharField(max_length=100, null=True)),
                ('place_lat', models.FloatField(default=0, null=True)),
                ('place_long', models.FloatField(default=0, null=True)),
                ('place_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'place',
                'managed': False,
            },
        ),
    ]
