# Generated by Django 4.0.2 on 2022-02-28 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Backend1', '0007_remove_post_post_image_alter_people_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Likes',
            field=models.ManyToManyField(related_name='Post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('Created_date', models.DateTimeField(auto_now_add=True)),
                ('Updated_date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_post', to='Backend1.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
