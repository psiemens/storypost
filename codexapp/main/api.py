import json

from django.http import JsonResponse

from codexapp.main.models import Prompt, Reply

def serialize_reply(reply):

    return {
        'id': reply.id,
        'content': reply.content,
        'email': reply.email,
        'points': reply.points,
        'timestamp': reply.timestamp
    }

def prompt(request, id):

    prompt = Prompt.objects.get(pk=id)
    prompt.sync_replies()

    replies = [serialize_reply(r) for r in prompt.replies]

    return JsonResponse({ 'replies': replies })

def reply_upvote(request, id):

    try:
        reply = Reply.objects.get(pk=id)
        reply.points += 1
        reply.save()
        success = True
    except:
        success = False

    return JsonResponse({ 'success': success })
