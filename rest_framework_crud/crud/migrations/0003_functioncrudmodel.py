# Generated by Django 2.2.1 on 2019-05-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionCrudModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.CharField(default='Inactive', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
