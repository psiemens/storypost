from django.shortcuts import render_to_response, render, redirect

from codexapp.main.models import User, List, Prompt
from codexapp.main.forms import RegistrationForm, ListForm, PromptForm

def home(request):

    from codexapp.remote import mailchimp

    context = {
        'lists': mailchimp.lists()
    }

    return render(request, "home.html", context)


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }

    return render(request, "register.html", context)

def logout(request):
    from django.contrib.auth.views import logout
    return logout(request, template_name='logout.html')

def login(request):
    from django.contrib.auth.views import login
    return login(request, template_name='login.html')

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

    user = User.objects.get(auth_user=request.user.id)

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.user = user
            list.save()
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


def prompts(request, list_id):

    context = {
        'list_id': list_id,
        'prompts': Prompt.objects.filter(list_id=list_id)
    }

    return render(request, "prompt/index.html", context)

def prompt_view(request, list_id, id):
    context = {
        'prompt': {
            'message': "What is the craziest dream you've ever had?"
        }
    }
    context['prompt'] = Prompt.objects.get(pk=id)
    return render(request, "prompt/prompt.html", context)

def prompt_add(request, list_id):

    user = User.objects.get(auth_user=request.user.id)

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.save(commit=False)
            prompt.user = user
            prompt.list_id = list_id
            prompt.save()
            return redirect(prompt_edit, list_id, prompt.id)
    else:
        form = PromptForm()

    context = {
        'form': form,
    }

    return render(request, "prompt/edit.html", context)

def prompt_edit(request, list_id, id):

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

def prompt_send(request, list_id, id):

    from codexapp.remote import mailchimp

    prompt = Prompt.objects.get(pk=id)

    sent = mailchimp.campaigns.get(prompt.mc_campaign_id).send()

    if not sent:
         raise Exception('Campaign wasn\'t sent')

    return render(request, "prompt/send.html")
