# Generated by Django 2.1.5 on 2019-02-26 11:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='childparentsrelation',
            unique_together={('student', 'parent')},
        ),
    ]
