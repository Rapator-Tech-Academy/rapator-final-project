# Generated by Django 3.1.5 on 2021-01-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_merge_20210113_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Finished'), (3, 'Rejected')], default=0),
        ),
    ]