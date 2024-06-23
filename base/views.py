from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.contrib.auth import logout
from .froms import *
from django.db.models import Q

# Create your views here.


def downloadsheet(request, file_id):
    cheatsheet = get_object_or_404(UploadFile, id = file_id)
    file_path = cheatsheet.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attechment; filename="{cheatsheet.type_file}"'
    return response


@login_required
def home(request):
    
    if request.method == 'GET':
        
        if request.user.user_type == 'مساعد':
            context = {
                'files': StatusFile.objects.filter((Q(status=None) | Q(status='2') | Q(status='3')) & Q(is_proccessed=False)),
            }
        elif request.user.user_type == 'مدقق':
            context = {
                'files':StatusFile.objects.filter(Q(status=None) & Q(is_proccessed=False)),
            }
        elif request.user.user_type == 'مشرف':

            context = {
                'files':StatusFile.objects.filter(Q(status='1') & Q(is_proccessed = False)),
            }
        # fiels=UploadFile.objects.all()

        elif request.user.user_type == 'مدير':
            
            context = {
                'files':StatusFile.objects.filter((Q(status='4') | Q(status='5')) & Q(is_proccessed=False)),
            }   

        return render(request, 'files.html', context)
    
@login_required(login_url='login')
def all_files(request):
    context = {
        'files':StatusFile.objects.all()
    }
    return render(request, 'all_files.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def upload_file(request):
    
    if request.method == 'POST':
        form = FormUploadFile(request.POST)
        file = request.FILES['file']
        note = request.POST['note']
        type_file = request.POST['type_file']
        file_ = UploadFile.objects.create(user=request.user, file=file,note=note,type_file=type_file)
        if request.user.user_type == 'مدقق':
            status_file = StatusFile.objects.create(file=file_, user=request.user, status = '1')
        else:
            status_file = StatusFile.objects.create(file=file_, user=request.user)
        return redirect('home')
    context = {
        'form' : FormUploadFile()
    }
    return render(request, 'upload_file.html', context)


@login_required
def get_my_files(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'files':user.orderfile_set.all()
    }

    return render(request, 'my_files.html', context)

@login_required
def get_info_file(request, file_id):
    context = {
        'file':get_object_or_404(UploadFile, pk=file_id)
    }

    return render(request, 'get_file_info.html', context)


@login_required
def edit_file(request, file_id):
    file = get_object_or_404(UploadFile, pk=file_id)
    # f = file.statusfile_set.all().first()
    # f.is_proccessed = True
    # f.save()
    if request.method == 'POST':
        form = FormUploadFile(request.POST, request.FILES, instance=file)
        if form.is_valid():
            # form.save(commit=False)
            # file.file = request.POST['file']
            form.save()
        return redirect('home')
    context = {
        'form':FormUploadFile(instance=file)
    }
    return render(request, 'edit_file.html', context)

@login_required
def accept_file(request, file_id):
    file = get_object_or_404(StatusFile, pk=file_id)
    if request.user.user_type == 'مدقق':
        status_file = StatusFile.objects.create(
            file = file.file,
            user = file.file.user,
            status = '1',
            # is_proccessed = True
        )
    elif request.user.user_type == 'مشرف':
        status_file = StatusFile.objects.create(
            file = file.file,
            user = file.file.user,
            status = '5',
            # is_proccessed = True
        )

    elif request.user.user_type == 'مدير':
        status_file = StatusFile.objects.create(
            file = file.file,
            user = file.file.user,
            status = '5',
            # is_proccessed = True
        )
    file.delete()
    return redirect('home')

def review(request, file_id):
    file = get_object_or_404(StatusFile, pk=file_id)
    if request.user.user_type == 'مساعد':
        status_file = StatusFile.objects.create(
            file = file.file,
            user = file.file.user,
            status = None,
            note = '',
            # is_proccessed = True
        )
        file.delete()
        return redirect('home')
    
    if request.method == 'POST':
        
        # f = StatusFile.objects.get(file=file)
        if request.user.user_type == 'مدقق':
            status_file = StatusFile.objects.create(
                file = file.file,
                user = file.file.user,
                status = '2',
                note = request.POST['note']
            )
        if request.user.user_type == 'مشرف':
            status_file = StatusFile.objects.create(
                file = file.file,
                user = file.file.user,
                status = '4',
                note = request.POST['note'],
                # is_proccessed = True
            )

        file.delete()
        return redirect('home')
    else:
        form = FormStatusFile()
        return render(request, 'review.html', {'form':form})

def refuse_file(request, file_id):
    if request.method == 'POST':
        file = get_object_or_404(StatusFile, pk=file_id)
        # f = StatusFile.objects.get(fiel=file)
        if request.user.user_type == 'مدقق':
            status_file = StatusFile.objects.create(
                file = file.file,
                user = file.file.user,
                status = '3',
                note = request.POST['note'],
            )
        if request.user.user_type == 'مشرف':
            status_file = StatusFile.objects.create(
                file = file.file,
                user = file.file.user,
                status = '3',
                note = request.POST['note'],
            )
        if request.user.user_type == 'مدير':
            status_file = StatusFile.objects.create(
                file = file.file,
                user = file.file.user,
                status = '3',
                note = request.POST['note'],
            )
        file.delete()
        return redirect('home')
    else:
        context = {
            'form':FormStatusFile()
        }
        return render(request, 'refuse.html', context)
    


def order_file(request):
    if request.method == 'POST':
        form = FormOrderFile(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = FormOrderFile()
    context = {
        'form' : form
    }
    return render(request, 'order_file.html', context)


def track_files(request):
    context = {
        'files' : StatusFile.objects.filter(Q(status = '1'))
    }

    return render(request, 'tracks_file.html', context)