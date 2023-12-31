# Generated by Django 4.2.2 on 2023-07-05 14:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('point_value', models.DecimalField(decimal_places=2, default=1.0, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name="UserPoints",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("points_granted", models.DecimalField(decimal_places=2, default=10.0, max_digits=9)),
                ("points_spent", models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ("user", models.ForeignKey(on_delete=models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),

    ]
