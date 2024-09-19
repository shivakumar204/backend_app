from django.shortcuts import render, redirect
from .models import Snippet

def home(request):
    snippets = Snippet.objects.all().order_by('-created_at')
    return render(request, 'lock/home.html', {'snippets': snippets})
def share_snippet(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Snippet.objects.create(text=text)
            return redirect('home')
    return render(request, 'lock/share_snippet.html')
