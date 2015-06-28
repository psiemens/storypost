from codexapp.main.models import User

def user(request):
    try:
        user = User.objects.get(auth_user=request.user.id)
        user_id = user.id
        user_mc_enabled = user.mc_api_key
    except:
        user_id = None
        user_mc_enabled = False
    return {
        'user_id': user_id,
        'user_mc_enabled': user_mc_enabled
    }