from django.shortcuts import render, redirect
from .forms import AdvancedUserCreationForm,UserInfoForm, UserBioForm, UserImgForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(req):
    form = AdvancedUserCreationForm()
    if req.method == 'POST':
        form = AdvancedUserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Account has been created!')
            return redirect('login')
        else:
            for fields, error in form.errors.items():
                messages.warning(req, f'{error}')
    return render(req, 'users/register.html', {'form': form})



@login_required(login_url='login')
def profile(req):
    return render(req, 'users/profile.html')


@login_required(login_url='login')
def update_profile(req):
    if req.method == 'POST':
        uinfo = UserInfoForm(req.POST, instance=req.user)
        ubio = UserBioForm(req.POST, instance=req.user.profile)
        uimg = UserImgForm(req.POST, req.FILES, instance=req.user.profile)
        if uinfo.is_valid() or ubio.is_valid() or uimg.is_valid():
            uinfo.save()
            ubio.save()
            uimg.save()
            messages.info(req, 'Profile has been changed!')
            return redirect('profile')
    else:
        uinfo = UserInfoForm(instance=req.user)
        ubio = UserBioForm(instance=req.user.profile)
        uimg = UserImgForm(req.FILES, instance=req.user.profile)
    data = {
        'uinfo': uinfo,
        'ubio': ubio,
        'uimg': uimg
    }
    return render(req, 'users/profile_update.html', data)


