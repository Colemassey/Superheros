
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/details.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
        # Save the form contents as a new db object
        # return to index
    else:
        return render(request, 'superheroes/create.html')

def edit(request, hero_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        Superhero.objects.filter(pk=hero_id).update(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        single_hero = Superhero.objects.get(pk=hero_id)
        context = {
            'single_hero': single_hero,
            'hero_id': hero_id
        }
        return render(request, 'superheroes/edit.html', context)

def delete(request, hero_id):
    Superhero.objects.filter(pk=hero_id).delete()
    return HttpResponseRedirect(reverse('superheroes:index'))