# Generated by Django 5.0.4 on 2024-04-24 18:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('employment_status', models.CharField(choices=[('full-time', 'Full-Time'), ('part-time', 'Part-Time')], default='full time', max_length=25)),
                ('salary_min', models.IntegerField(null=True)),
                ('salary_max', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=100)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('source', models.CharField(choices=[('wellfound', 'Wellfound'), ('linkedin', 'LinkedIn'), ('otta', 'Otta'), ('indeed', 'Indeed')], max_length=25)),
                ('link', models.CharField(max_length=200, null=True)),
                ('follow_up_date_1', models.DateField(null=True)),
                ('follow_up_date_2', models.DateField(null=True)),
                ('has_received_response', models.BooleanField(default=False)),
                ('has_received_interview_invitation', models.BooleanField(default=False)),
                ('was_rejected', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]