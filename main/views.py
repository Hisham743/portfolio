import os

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from main.forms import Mail
from main.models import Work


def home(request):
    if request.method == 'POST':
        form = Mail(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                f"Message from {data['name']}! (portfolio)",
                f"email_address: {data['email']}\n\n{data['message']}",
                from_email=os.environ['EMAIL'],
                recipient_list=[os.environ['EMAIL']],
                fail_silently=False,
            )
            messages.success(request, 'Message sent Successfully!')
            return redirect('home')
    else:
        form = Mail()
    context = {'data': Work.objects.all(),
               'form': form}
    return render(request, 'main/index.html', context=context)
