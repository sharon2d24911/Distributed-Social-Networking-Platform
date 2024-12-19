# Generated by Django 5.1.1 on 2024-12-01 21:20

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('post', 'Post'), ('shared_post', 'Shared Post'), ('follow', 'Follow Request'), ('like', 'Like'), ('comment', 'Comment')], max_length=11)),
                ('FQIDorId', models.CharField(max_length=1000, null=True, unique=True)),
                ('received_at', models.DateTimeField()),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inboxOwner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('post', 'Post'), ('shared_post', 'Shared Post'), ('follow', 'Follow Request'), ('like', 'Like'), ('comment', 'Comment')], max_length=11)),
                ('received_at', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inbox', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post')),
            ],
        ),
    ]
