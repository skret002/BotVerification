# Generated by Django 4.2.6 on 2023-10-17 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BotVerification', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InstructionRu',
            new_name='VerificationCode',
        ),
    ]