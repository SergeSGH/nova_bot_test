from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Login(models.Model):
    chat_id = models.IntegerField('ID чата', help_text='ID')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Chat ID'
        verbose_name_plural = 'Chat IDs'

    def __str__(self):
        return str(self.chat_id)
