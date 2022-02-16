# Generated by Django 4.0.1 on 2022-02-15 10:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaloonModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='saloon')),
                ('address', models.TextField()),
                ('town', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('rating', models.IntegerField(default=0)),
                ('start_timings', models.TimeField(default='09:00:00')),
                ('end_timings', models.TimeField(default='18:00:00')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('service_name', models.CharField(max_length=50)),
                ('service_cost', models.FloatField(default=100)),
                ('service_duration', models.DurationField()),
                ('saloon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saloon_services', to='app.saloonmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SeatModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('seat_name', models.CharField(max_length=10)),
                ('is_available', models.BooleanField(default=True)),
                ('saloon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saloon_seats', to='app.saloonmodel')),
            ],
            options={
                'ordering': ['seat_name'],
            },
        ),
    ]