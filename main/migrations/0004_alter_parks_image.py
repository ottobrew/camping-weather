# Generated by Django 4.2.4 on 2023-09-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_parks_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parks",
            name="image",
            field=models.ImageField(default="NewtonHills.jpg", upload_to=""),
        ),
    ]
