from django.http import Http404
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Album

#mailowe
from music.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums,}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("This album does not exists")
    return render(request, 'music/detail.html', {'album' : album})

def contact(request):
    return render(request, 'music/contact.html')

def cover(request):
    return render(request, 'music/cover.html')


def email(request):
    form_class = ContactForm
 # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('music/email_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Satori Audio" +'',
                ['fr.nikon@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('music:email')

    return render(request, 'music/email.html', {'form': form_class,})
