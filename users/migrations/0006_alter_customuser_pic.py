# Generated by Django 5.0.7 on 2024-07-30 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_customuser_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="pic",
            field=models.ImageField(default="no_picture.jpg", upload_to="users"),
        ),
    ]
