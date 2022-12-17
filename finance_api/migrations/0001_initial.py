# Generated by Django 4.1.3 on 2022-12-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('full_address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('date_of_birth', models.CharField(blank=True, max_length=20, null=True)),
                ('occupation', models.CharField(max_length=20)),
                ('monthly_income', models.CharField(max_length=20)),
                ('asset_type', models.CharField(max_length=50)),
                ('contact_status_id', models.CharField(max_length=20)),
                ('lifecycle_stage_id', models.CharField(max_length=20)),
            ],
        ),
    ]