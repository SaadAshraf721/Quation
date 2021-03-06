# Generated by Django 4.0.1 on 2022-01-27 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=255)),
                ('to', models.IntegerField()),
                ('sts', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_primary_manual_roats', to=settings.AUTH_USER_MODEL, verbose_name='doc')),
                ('pa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_secondary_manual_roats', to=settings.AUTH_USER_MODEL, verbose_name='pa')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
