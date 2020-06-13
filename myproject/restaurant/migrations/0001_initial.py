# Generated by Django 3.0.6 on 2020-06-10 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, unique=True)),
                ('composition', models.CharField(max_length=100)),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.TextField(max_length=1000)),
                ('prix', models.IntegerField()),
                ('nb_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=30)),
                ('nb_table', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Utilisateurs', to='restaurant.Commande')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Utilisateurs', to='restaurant.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(max_length=30)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='restaurant.Menu')),
            ],
        ),
    ]