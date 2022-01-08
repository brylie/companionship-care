# Generated by Django 4.0 on 2022-01-08 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_display_name_alter_user_email'),
        ('care_groups', '0005_remove_caregroup_coordinators_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareGroupMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_organizer', models.BooleanField(default=False)),
                ('care_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='care_groups.caregroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='care_groups', to='accounts.user')),
            ],
        ),
    ]
