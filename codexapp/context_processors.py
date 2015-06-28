from codexapp.main.models import User

def user_id(request):
    user = User.objects.get(auth_user=request.user.id)
    return user.id

def user(request):
    return {
        'user_id': user_id(request)
    }