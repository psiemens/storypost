from django.shortcuts import render_to_response, render, redirect, HttpResponse

from codexapp.main.models import User, List, Prompt, Reply
from codexapp.main.forms import RegistrationForm, UserForm, ListForm, PromptForm, PromptQuickForm, ReplyForm

def home(request):
    context = {
        'featured_replies': [
            Reply.objects.get(pk=5)
        ]
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
        'title': "Register",
        'form': form,
    }

    return render(request, "register.html", context)

def profile(request):

    user = User.objects.get(auth_user=request.user.id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(profile)
    else:
        form = UserForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, "user/profile.html", context)

def logout(request):
    from django.contrib.auth.views import logout
    return logout(request, template_name='home.html')

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


def list_view(request, list_id):

    lst = List.objects.get(pk=list_id)

    context = {
        'list_id': list_id,
        'list': lst,
        'codex_user': User.objects.get(pk=lst.user_id),
        'prompts': Prompt.objects.filter(list_id=list_id)
    }

    return render(request, "list/view.html", context)


def list_subscribe(request, list_id):

    user = User.objects.get(auth_user=request.user.id)

    list = List.objects.get(pk=list_id)

    list.add_member(user)

    return redirect(list_view, list_id)


def list_unsubscribe(request, list_id):

    user = User.objects.get(auth_user=request.user.id)

    list = List.objects.get(pk=list_id)

    list.remove_member(user)

    return redirect(list_view, list_id)


def prompt_view(request, list_id, id):

    p = Prompt.objects.get(pk=id)

    context = {
        'prompt': p,
        'other_user_prompts': Prompt.objects.filter(user__id=p.user_id)
                                            .order_by('-id')[:4],
        'prev_prompt': Prompt.objects.filter(list__id=p.list_id)
                                     .filter(pk__lt=id)
                                     .order_by('-id').first(),
        'next_prompt': Prompt.objects.filter(list__id=p.list_id)
                                     .filter(pk__gt=id)
                                     .order_by('id').first()
    }

    return render(request, "prompt/prompt.html", context)


def prompt_add_quick(request):

    user = User.objects.get(auth_user=request.user.id)

    if request.method == 'POST':
        form = PromptQuickForm(request.POST)
        if form.is_valid():
            prompt = form.save(commit=False)
            prompt.user = user
            prompt.save()
            return redirect(prompt_edit, prompt.list_id, prompt.id)
    else:
        form = PromptQuickForm()

    context = {
        'title': "Create a prompt",
        'form': form,
    }

    return render(request, "prompt/quick_add.html", context)

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

    prompt = Prompt.objects.get(pk=id)

    sent = prompt.send()

    if not sent:
         raise Exception('Campaign wasn\'t sent')

    return render(request, "prompt/send.html")

def prompt_respond(request, list_id, id):
    
    form = ReplyForm(request.POST)
    print dir(request.POST)
    print request.POST

    if not form.is_valid():
        return HttpResponse("bad form! no potato")

    reply = form.save(commit=False)

    me = User.objects.get(pk=User.objects.get(auth_user=request.user).id)

    reply.user = me
    reply.email = me.email
    reply.prompt = Prompt.objects.get(pk=id)

    reply.save()

    return redirect('prompt_view', list_id, id)


def user_view(request, id):
    context = {
        'person': User.objects.get(pk=id),
        'lists': List.objects.filter(user__id=id)
    }
    return render(request, "user/view.html", context)
