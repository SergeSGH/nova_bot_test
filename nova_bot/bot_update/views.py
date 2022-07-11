import os

from django.shortcuts import redirect, render

from .forms import MessageForm


# вью для страницы с логами (с ней удобнее смотреть полученные данные от Telegram)
# также можно поменять сообщение при запуске бота
def OnePageView(request):
    template = 'index.html'
    form = MessageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        bot_message = form.cleaned_data['bot_message']
        with open('bot_message.txt', 'w', encoding="utf-8") as f:
            f.write(bot_message)
        form = MessageForm()
    else:
        if os.path.isfile('bot_message.txt'):
            with open('bot_message.txt', 'r', encoding="utf-8") as f:
                bot_message = f.read()
        else:
            bot_message = 'не установлено'

    if os.path.isfile('numbers_sent.txt'):
        with open('numbers_sent.txt', 'r', encoding="utf-8") as f:
            numbers_sent = f.read()
    else:
        numbers_sent = ''

    if os.path.isfile('request_data.txt'):
        with open('request_data.txt', 'r', encoding="utf-8") as f:
            request_data = f.read()
    else:
        request_data = ''

    context = {
        'bot_message': bot_message,
        'numbers_sent': numbers_sent,
        'request_data': request_data,
        'form': form
    }
    return render(request, template, context)

# удаляем данные на странице по запросу
def CleanData(request):
    if os.path.isfile('request_data.txt'):
        f = open('request_data.txt', 'w+')
        f.seek(0)
        f.close()
    if os.path.isfile('numbers_sent.txt'):
        f = open('numbers_sent.txt', 'w+')
        f.seek(0)
        f.close()
    return redirect('/')
