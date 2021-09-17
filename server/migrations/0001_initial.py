# Generated by Django 3.2.7 on 2021-09-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDocumentServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField()),
                ('project_name', models.CharField(max_length=200)),
                ('port_number', models.IntegerField()),
            ],
        ),
    ]
