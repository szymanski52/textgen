from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .forms import UserRegistrationForm, PrivateGoalCreateForm
from .models import PrivateGoal, Event


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'eventsmanager/home.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'eventsmanager/registration.html', {'user_form': user_form})


def showGoalsTable(request):
    user = request.user
    goals = PrivateGoal.objects.filter(userId=user)
    form = PrivateGoalCreateForm
    context = {
        'goals': goals,
        'form': form,
    }
    return render(request, 'eventsmanager/goals.html', context)


def goalsRedirect(request):
    if request.method == 'POST':
        form = PrivateGoalCreateForm(request.POST)
        if form.is_valid():
            new_goal = form.save(commit=False)
            new_goal.userId = request.user
            new_goal.save()
            redirect('goals_add')
    return redirect('goals')


def home(request):
    user = request.user
    goals = PrivateGoal.objects.filter(userId=user)[:3]
    context = {
        'goals': goals,
    }
    return render(request, 'eventsmanager/home.html', context)


def login(request):
    return render(request, 'eventsmanager/login.html')


def showEventsList(request):
    return render(request, 'eventsmanager/events.html')
