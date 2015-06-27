from django.shortcuts import render_to_response, render, redirect

from codexapp.remote import mailchimp
from codexapp.main.models import List, Prompt
from codexapp.main.forms import ListForm, PromptForm

def home(request):

    context = {
        'lists': mailchimp.lists()
    }

    return render(request, "home.html", context)


def create_list(request):

    list = List(title='Test list 255', description='This is a test description')
    list.save()

    context = {
        'list': list,
    }

    return render(request, "create_list.html", context)


def lists(request):

    context = {
        'lists': List.objects.all()
    }

    return render(request, "list/index.html", context)


def list_add(request):

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect(list_edit, list.id)
    else:
        form = ListForm()

    context = {
        'form': form,
    }

    return render(request, "list/edit.html", context)


def list_edit(request, id):

    list = List.objects.get(pk=id)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
    else:
        form = ListForm(instance=list)

    context = {
        'form': form,
    }

    return render(request, "list/edit.html", context)


def prompts(request):

    context = {
        'prompts': Prompt.objects.all()
    }

    return render(request, "prompt/index.html", context)

def prompt_view(request, id):
    context = {
        'prompt': {
            'message': "What is the craziest dream you've ever had?"
        }
    }
    context['prompt'] = Prompt.objects.get(pk=1)
    return render(request, "prompt/prompt.html", context)

def prompt_add(request):

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.save()
            return redirect(prompt_edit, prompt.id)
    else:
        form = PromptForm()

    context = {
        'form': form,
    }

    return render(request, "prompt/edit.html", context)

def prompt_edit(request, id):

    prompt = Prompt.objects.get(pk=id)

    if request.method == 'POST':
        form = PromptForm(request.POST, instance=prompt)
        if form.is_valid():
            form.save()
    else:
        form = PromptForm(instance=prompt)

    context = {
        'form': form,
    }

    return render(request, "prompt/edit.html", context)
