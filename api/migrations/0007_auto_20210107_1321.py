# Generated by Django 3.1.5 on 2021-01-07 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20210107_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='owning_users',
            field=models.ManyToManyField(related_name='owned_games', through='api.GameOwnership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gameownership',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_ownership_link', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playersessionlink',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='user_session_links', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='users',
            field=models.ManyToManyField(related_name='sessions', through='api.PlayerSessionLink', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='gameownership',
            unique_together={('user', 'game')},
        ),
        migrations.AlterUniqueTogether(
            name='playersessionlink',
            unique_together={('user', 'session')},
        ),
        migrations.RemoveField(
            model_name='gameownership',
            name='player',
        ),
        migrations.RemoveField(
            model_name='playersessionlink',
            name='player',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
