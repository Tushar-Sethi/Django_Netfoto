# Generated by Django 4.0.2 on 2022-03-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend1', '0012_remove_images_tag1_remove_images_tag2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Tag1_Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Tag2_Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Tag3_Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
