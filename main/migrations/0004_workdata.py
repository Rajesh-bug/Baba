# Generated by Django 4.0.5 on 2022-06-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_gotradata_delete_gotra_data_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=50)),
                ('rate', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'work_data',
                'managed': False,
            },
        ),
    ]
