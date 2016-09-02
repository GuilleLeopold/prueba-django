from django.shortcuts import render
from django.conf import settings

import requests


from .forms import SubmitEmbed
from .serializer import EmbedSerializer


def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        print 'hola'
        if form.is_valid():
            print 'hola2'
            url = form.cleaned_data['url']
            r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
            json = r.json()
            print json
            serializer = EmbedSerializer(data=json)
            print serializer
            if serializer.is_valid():
                print 'hola3'
                embed = serializer.save()
                return render(request, 'embeds.html', {'embed': embed})
            else:
                print serializer.errors
    else:
        form = SubmitEmbed()

    return render(request, 'index.html', {'form': form})
