# Generated by Django 4.2.16 on 2024-10-20 05:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ColourType',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basemodel')),
                ('type', models.CharField(max_length=4)),
                ('first_value_max', models.PositiveIntegerField(blank=True, null=True)),
                ('second_value_max', models.PositiveIntegerField(blank=True, null=True)),
                ('third_value_max', models.PositiveIntegerField(blank=True, null=True)),
            ],
            bases=('app.basemodel',),
        ),
    ]
