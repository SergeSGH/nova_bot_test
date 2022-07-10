from django import forms


class MessageForm(forms.Form):
    bot_message = forms.CharField(help_text='bot_message')
