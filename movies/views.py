# from django.http import HttpResponse
from datetime import date
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404,get_list_or_404
from .models import *
from .forms import *
from django.urls import reverse
import datetime
# Create your views here





def index(request):
    movies = Movie.objects.filter(is_active = True,is_home= True)
    slider = get_list_or_404(Slider)
  
    return render(request,'index.html',{
        'movies':movies,
        'sliders':slider,
        
        
    })





def movies(request):
    movies = Movie.objects.filter(is_active = True)
    return render(request,'movies.html',{
        'movies':movies
    })



def movie_details(request,slug):
    movies = get_object_or_404(Movie,slug = slug)
    comment_form = CommentForm()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movies
            comment.save()
            return redirect(reverse('movie_details',args=[slug]))
    
    content={
        'movie':movies,
        'genres':movies.genres.all(),
        'people':movies.people.all(),
        'videos':movies.video_set.all(),
        'comments':movies.comments.all().order_by('-full_name'),
        'comment_form':comment_form,
        'slug':slug
    }
    return render(request,'movie-details.html',content)