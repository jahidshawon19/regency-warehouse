# Generated by Django 3.1.5 on 2021-05-04 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('storeDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField()),
                ('receiveQuantity', models.IntegerField()),
                ('receiveBy', models.CharField(blank=True, max_length=50, null=True)),
                ('issueQuantity', models.IntegerField()),
                ('issueBy', models.CharField(blank=True, max_length=50, null=True)),
                ('issueTo', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=50, null=True)),
                ('exportToCSV', models.BooleanField(default=False)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockManagement.category')),
            ],
        ),
    ]
