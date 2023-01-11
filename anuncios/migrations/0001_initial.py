# Generated by Django 4.1.5 on 2023-01-11 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imoveis', '0002_alter_imovel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.CharField(choices=[('AIRBNB', 'AirBnb'), ('BOOKING', 'Booking'), ('TRIVAGO', 'Trivago'), ('HOTEL_URBANO', 'Hotel Urbano')], max_length=30)),
                ('taxa_plataforma', models.FloatField()),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
                ('dt_atualizacao', models.DateTimeField(auto_now=True)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.imovel')),
            ],
        ),
    ]