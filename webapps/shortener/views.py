# shortener/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import URL
from .forms import URLForm
from django.utils import timezone

def home(request):
    s = URL.objects.all()
    
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return JsonResponse({
                'original_url': url.original_url,
                'short_url': request.build_absolute_uri(url.short_url)
            })
    else:
        form = URLForm()
    
    return render(request, 'shortener/home.html', {'form': form, 'urls': s})

def redirect_short_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    if url.is_expired():
        return JsonResponse({'error': 'This short URL has expired.'}, status=404)
    
    url.access_count += 1
    url.save()
    
    return redirect(url.original_url)

