from django.shortcuts import render
from .models import Image
from .forms import imageform

# Create your views here.
def index(request):
    if request.method=="POST":
        form = imageform(request.POST, request.FILES)
        if form.is_valid():
         form.save()
    form=imageform()
    img=Image.objects.all()
    return render(request, 'index.html', {'img':img, 'form':form})
