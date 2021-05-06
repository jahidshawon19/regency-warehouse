# Generated by Django 3.1.5 on 2021-05-06 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockManagement', '0005_auto_20210505_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='issueBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stock',
            name='receiveBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receive_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
