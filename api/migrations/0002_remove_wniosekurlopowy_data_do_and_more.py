# Generated by Django 5.1.5 on 2025-03-23 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wniosekurlopowy',
            name='data_do',
        ),
        migrations.RemoveField(
            model_name='wniosekurlopowy',
            name='data_od',
        ),
        migrations.RemoveField(
            model_name='wniosekurlopowy',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wniosekurlopowy',
            name='zatwierdzone',
        ),
        migrations.AddField(
            model_name='wniosekurlopowy',
            name='data_utworzenia',
            field=models.DateTimeField(auto_now_add=True, default='2025-03-23 12:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wniosekurlopowy',
            name='pracownik',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wnioski', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wniosekurlopowy',
            name='status',
            field=models.CharField(choices=[('oczekuje', 'Oczekuje na zatwierdzenie'), ('zatwierdzony', 'Zatwierdzony'), ('odrzucony', 'Odrzucony')], default='oczekuje', max_length=20),
        ),
        migrations.AddField(
            model_name='wniosekurlopowy',
            name='wybrane_dni',
            field=models.JSONField(default=list),
        ),
    ]
