# Generated by Django 3.2.5 on 2021-12-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0002_alter_candidate_u_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='U_ID',
        ),
        migrations.AddField(
            model_name='candidate',
            name='U_NAME',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
