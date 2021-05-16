# Generated by Django 2.2.13 on 2021-05-02 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0002_auto_20210501_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(blank=True, null=True)),
                ('room_type', models.CharField(choices=[('COVID', 'Covid'), ('GENERAL', 'General')], default='COVID', max_length=10)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('no_beds', models.IntegerField(blank=True, null=True)),
                ('filled_beds', models.IntegerField(blank=True, null=True)),
                ('rem_beds', models.IntegerField(blank=True, null=True)),
                ('roomhospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomhospital', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
