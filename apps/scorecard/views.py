from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

def new_game(request):
    """foo"""
    try:
        current_game = request.session['current_game']
    except KeyError:
        current_game = Game.objects.create().save()
        request.session['current_game'] = current_game

    else:
        current_game = request.session['current_game']
        scorecards = ScoreCard.objects.get(game=current_game.id, )
        
            
    if request.method == 'POST':
        form = NewScoreCardForm(request.POST)
        if form.is_valid():
            new_player = form.save(current_game)
                  
        return redirect(reverse('newgame'))
     
    else:
        form = NewScoreCardForm()
    
    return render(request,'newgame.html',{'form':form,
                                          'scorecards':scorecards})

