# Generated by Django 5.1.6 on 2025-02-12 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasteur_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificat',
            name='references_legales',
        ),
    ]
