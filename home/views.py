from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib import messages

from announcement.models import Category, Announcement, Images, Comment
from home.forms import SearchForm, JoinForm
from home.models import Settings, ContactFormu, ContactFormMessage, UserProfile, FAQ
from menu.models import Content, Menu


def index(request):
    setting = Settings.objects.get(pk =1)
    category = Category.objects.all()
    announcement = Announcement.objects.filter(category_id=15)
    # announcement = Announcement.objects.all()
    news = Announcement.objects.filter(category_id=17)
    educations = Announcement.objects.filter(category_id=16)
    menu =Menu.objects.all()
    sliderdata = Announcement.objects.all()
    content = Content.objects.all()
    context = {
        'setting': setting,
        'page': 'home',
        'category': category,
        'announcement' : announcement,
        'news': news,
        'educations' :educations,
        'menu':menu,
        'content': content,
        'sliderdata': sliderdata
    }
    return render(request, 'index.html', context)


def aboutus(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    sliderdata = Announcement.objects.all()
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting,'category': category,'sliderdata': sliderdata,'menu':menu,}
    return render(request, 'aboutus.html', context)

def references(request):
    menu = Menu.objects.all()
    sliderdata = Announcement.objects.all()
    category = Category.objects.all()
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting, 'page': 'aboutus','category': category,'sliderdata': sliderdata,'menu':menu,}
    return render(request, 'references.html', context)


def contactus(request):
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
            return HttpResponseRedirect('/contactus')
    menu = Menu.objects.all()
    sliderdata = Announcement.objects.all()
    category = Category.objects.all()
    setting = Settings.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form,'category': category,'menu':menu,'sliderdata': sliderdata}
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
    menu = Menu.objects.all()
    sliderdata = Announcement.objects.all()
    category = Category.objects.all()
    setting = Settings.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form' : form,'category': category,'sliderdata': sliderdata,'menu':menu,}
    return render(request, 'contactus.html', context)

def category_products(request,id,slug):
    menu = Menu.objects.all()
    sliderdata = Announcement.objects.all()

    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    announcement = Announcement.objects.filter(category_id=id)
    context = {'announcement': announcement,
               'category': category,
               'categorydata': categorydata,
               'menu': menu,
               'sliderdata' : sliderdata
               }
    return render(request, 'announcement.html', context)


def announcement_detail(request,id,slug):
    menu = Menu.objects.all()
    category = Category.objects.all()
    sliderdata = Announcement.objects.all()

    announcement = Announcement.objects.get(pk=id)
    images = Images.objects.filter(announcement_id =id)
    comments = Comment.objects.filter(announcement_id =id, status ='True')
    context = { 'announcement': announcement,
                'category': category,
                'images': images,
                'comments': comments,
                'menu': menu,
                'sliderdata': sliderdata

                }

    return render(request, 'announcement_detail.html', context)

def announcement_search(request):
    if request.method== 'POST':
        form =SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()

            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                announcement = Announcement.objects.filter(title__icontains=query)

            else:
                announcement = Announcement.objects.filter(title__icontains=query,category_id=catid)
            context = { 'announcement':announcement,
                        'category':category,


                        }
            return render(request,'announcement_search.html',context)
    return HttpResponseRedirect('/')



def announcement_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        announcement = Announcement.objects.filter(title__icontains=q)
        results = []
        for rs in announcement:
            announcement_json = {}
            announcement_json = rs.title
            results.append(announcement_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:

            messages.warning(request, "Kullanıcı adı yada Şifre yanlış")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()

    context = {'category':category,}
    return render(request, 'login.html', context)

def join_view(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user =request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image ="images/users/iconuser.jpg"
            data.save()
            messages.success(request,"Kullanıcı oluşturuldu.")

            # Redirect to a success page.
            return HttpResponseRedirect('/')
    form = JoinForm()

    category = Category.objects.all()

    context = {'category': category,
               'form': form,}
    return render(request, 'join.html', context)


def faq(request):
    category = Category.objects.all()
    sliderdata = Announcement.objects.all()
    menu = Menu.objects.all()
    faq= FAQ.objects.all().order_by('ordernumber')
    context = {'category': category,
               'faq': faq,
               'sliderdata': sliderdata,'menu':menu,}
    return render(request, 'fag.html', context)


def menu(request, id):
    try:
        content = Content.objects.get(menu_id=id)
        link = '/menu' + "/" + str(content.id) + "/" + str(content.slug)
        return HttpResponseRedirect(link)

    except:
        messages.warning(request, "ERROR ! İlgili İçerik Bulunamadı")
        link = '/home'
        return HttpResponseRedirect(link)


def content_detail(request, id, slug):
    category = Category.objects.all()
    sliderdata = Announcement.objects.all()
    menu = Menu.objects.all()
    images=Images.objects.filter(announcement_id=id)
    content = Content.objects.get(pk=id)
    setting = Settings.objects.get(pk=1)

    context = {
        'category': category,
        'content': content,
        'menu': menu,
        'setting': setting,
        'sliderdata': sliderdata,
        'images':images
    }
    return render(request, 'content_detail.html', context)



def addcontent(request, id, slug):
    category = Category.objects.all()
    sliderdata = Announcement.objects.all()
    menu = Menu.objects.all()
    content = Content.objects.get(pk=id)
    setting = Settings.objects.get(pk=1)

    context = {
        'category': category,
        'content': content,
        'menu': menu,
        'setting': setting,
        'sliderdata': sliderdata
    }
    return render(request, 'user_content.html', context)






