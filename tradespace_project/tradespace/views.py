from django.shortcuts import render

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'magna/index.html', context)

def login(request):
    return render(request, 'tradespace/login.html')

def home(request):
    return render(request, 'tradespace/index.html')

def categories(request):
    return render(request, 'tradespace/categories.html')

def my_profile(request):
    return render(request, 'tradespace/my_profile.html')

def user_profile(request):
    return render(request, 'tradespace/user_profile.html')

def messages(request):
    return render(request, 'tradespace/messages.html')

def create_post(request):
    return render(request, 'tradespace/create_post.html')

def post_detail(request):
    return render(request, 'tradespace/post_detail.html')

def find_friends(request):
    return render(request, 'tradespace/find_friends.html')

def friend_requests(request):
    return render(request, 'tradespace/friend_requests.html')

def notifications(request):
    return render(request, 'tradespace/notifications.html')

def saved(request):
    return render(request, 'tradespace/saved.html')

def invite(request):
    return render(request, 'tradespace/invite.html')

def setting(request):
    return render(request, 'tradespace/setting.html')

def explore(request):
    return render(request, 'tradespace/explore.html')
