# Generated by Django 3.2.9 on 2022-09-06 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_signals', '0006_auto_20211204_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='mailing_list',
            field=models.TextField(help_text='The mailing list to send the signal to. Either enter a comma separated list of emails or the app will search for a function with the same name in the model instance.'),
        ),
    ]
