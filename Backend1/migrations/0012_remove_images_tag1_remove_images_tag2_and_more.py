# Generated by Django 4.0.2 on 2022-03-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend1', '0011_remove_post_tags_remove_post_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='Tag1',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Tag2',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Tag3',
        ),
        migrations.RemoveField(
            model_name='images',
            name='description',
        ),
        migrations.RemoveField(
            model_name='images',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Tag1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Tag2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Tag3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
