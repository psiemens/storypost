from codexapp.main.models import User

def user_id(request):
    try:
        user = User.objects.get(auth_user=request.user.id)
        return user.id
    except:
        return None

def user(request):
    return {
        'user_id': user_id(request)
    }