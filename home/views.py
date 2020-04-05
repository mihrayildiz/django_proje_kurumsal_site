from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib import messages


from home.models import Settings,ContactFormu,ContactFormMessage


def index(request):
    setting = Settings.objects.get(pk =1)
    context = {'setting': setting, 'page': 'aboutus'}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Settings.objects.get(pk =1)
    context = {'setting': setting, 'page': 'aboutus'}
    return render(request, 'aboutus.html', context)

def references(request):
    setting = Settings.objects.get(pk =1)
    context = {'setting': setting, 'page': 'aboutus'}
    return render(request, 'references.html', context)


def contactus(request):
    setting = Settings.objects.get(pk =1)
    context = {'setting': setting, 'page': 'aboutus'}
    return render(request, 'contactus.html', context)

def iletisim(request):


      if request.method == 'POST':
            form = ContactFormu(request.POST)
            if form.is_valid():
                data = ContactFormMessage()
                data.name = form.cleaned_data['name']
                data.email = form.cleaned_data['email']
                data.subject = form.cleaned_data['subject']
                data.message = form.cleaned_data['message']
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                messages.success(request, "Mesaj Gönderilmiştir. İlginize Teşekkürler")
                return HttpResponseRedirect('/iletisim')

      setting = Settings.objects.get(pk=1)
      form = ContactFormu()
      context = {'setting': setting, 'form' : form}
      return render(request, 'contactus.html', context)



