# Generated by Django 4.0.2 on 2022-05-04 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Backend1', '0036_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('currentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentUser', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='Backend1.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relateduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
