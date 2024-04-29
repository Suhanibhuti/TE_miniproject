from .models import pdmM

def user_info(request):
    user_id = request.user.username
    users = pdmM.objects.filter(IDM=user_id)
    if users.exists():
        user = users.first()  # You can choose any logic to select a single user from multiple results
        return {'user_name': user.FnameM}
    else:
        return {}