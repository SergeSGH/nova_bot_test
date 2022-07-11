# Generated by Django 3.0 on 2022-07-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_update', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='login',
            options={'ordering': ['-id'], 'verbose_name': 'Chat ID', 'verbose_name_plural': 'Chat IDs'},
        ),
        migrations.RemoveField(
            model_name='login',
            name='username',
        ),
        migrations.AddField(
            model_name='login',
            name='chat_id',
            field=models.IntegerField(default=0, help_text='ID', verbose_name='ID чата'),
            preserve_default=False,
        ),
    ]