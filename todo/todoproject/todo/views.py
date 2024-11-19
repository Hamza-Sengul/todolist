from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:  # Yalnızca yönetici kullanıcıları giriş yapabilir
            login(request, user)
            return redirect('admin_panel')  # Özel yönetici paneline yönlendirme
        else:
            return render(request, 'admin_login.html', {'error': 'Geçersiz giriş bilgileri veya yetkisiz erişim'})
    return render(request, 'admin_login.html')

@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('index')  # Yönetici değilse ana sayfaya yönlendir
    return render(request, 'admin_panel.html')

def member_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_panel')  # Yönetici yönetici paneline yönlendirilir
            else:
                return redirect('member_panel')  # Üye üye paneline yönlendirilir
        else:
            return render(request, 'member_login.html', {'error': 'Geçersiz giriş bilgileri'})
    return render(request, 'member_login.html')

@login_required
def member_panel(request):
    if request.user.is_superuser:  # Eğer yönetici giriş yaptıysa, yönetici paneline yönlendir
        return redirect('admin_panel')
    return render(request, 'member_panel.html')

@login_required
def user_tasks(request):
    tasks = Task.objects.filter(user=request.user)  # Kullanıcıya atanmış görevler
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        if task.user == request.user:  # Güvenlik kontrolü
            task.is_completed = True  # Görevi tamamlandı olarak işaretle
            task.save()
        return redirect('user_tasks')
    return render(request, 'user_tasks.html', {'tasks': tasks})

@login_required
def admin_view_tasks(request):
    if not request.user.is_superuser:
        return redirect('index')  # Yalnızca yönetici erişimi
    tasks = Task.objects.all()
    return render(request, 'admin_view_tasks.html', {'tasks': tasks})
