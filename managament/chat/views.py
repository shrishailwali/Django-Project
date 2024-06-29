from django.shortcuts import render
from  .models import Chat
from .forms import ChatForm, UserRegistrationForm
# from .forms import SearchForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



# Create your views here.
def index(request):
    return render(request, 'index.html')

def chat_list(request):
    chats = Chat.objects.all().order_by('created_at')
    return render(request, 'chat_list.html', {'chats':chats})

@login_required
def chat_create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            chats = form.save(commit=False)
            chats.user = request.user
            chats.save()
            return redirect('chat_list')
        else:
            # Optional: Add handling for invalid form
            return render(request, 'form.html', {'form': form, 'error': 'Invalid form submission'})
    else:
        form = ChatForm()
    return render(request, 'form.html', {'form': form})

@login_required
def chat_update(request, id):
    chats = get_object_or_404(Chat,pk=id, user = request.user)
    if request.method == 'PUT':
        form = ChatForm(request.POST, request.FILES, instance=chats)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.save()
            return redirect('chat_list')
    else:
        form = ChatForm(instance=chats)
        return render(request, 'form.html', {'form':form})

@login_required
def chat_delete(request, id):
    chats = get_object_or_404(Chat, pk=id, user=request.user)
    if request.method =='POST':
        chats.delete()
        return redirect('chat_list')
    return render(request, 'form_delete.html', {'chats':chats})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('chat_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

# def search_list(request):
#     form = SearchForm()
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             chats = Chat.objects.filter(name__icontains = query).order_by('created_at')
#     return render(request, 'search_list.html', {'chats':chats})
