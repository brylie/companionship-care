# Generated by Django 4.0 on 2021-12-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'activity', 'verbose_name_plural': 'activities'},
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_date',
            field=models.DateField(auto_now=True),
        ),
    ]
