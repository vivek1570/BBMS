from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm ,person_form,donor_form,receive_form,search_form
from .models import person,stock,donor,receive


import datetime

# Get the current date
current_date = datetime.date.today()


# Create your views here.
def home(request): 
    return render(request, 'authenticate/home.html', {})

def baser(request):
    return render(request, 'authenticate/main_open.html', {})

def camp_info(request):
    return render(request, 'authenticate/camp.html')


def account(request):
    if request.user.is_authenticated:
        username=request.user.username
        useremail=request.user.email
        data= person.objects.get(p_name=username)
        return render(request, 'authenticate/account.html', {'data':data})

# return render(request,'authenticate/account.html',{})



def login_user (request):
    if request.method == 'POST': #if someone fills out form , Post it 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:# if user exist
            login(request, user)
            # messages.success(request,('Youre logged in'))
            return redirect('baser') #routes to 'home' on successful login  
        else:
            # messages.success(request,('Error logging in'))
            return redirect('login') #re routes to login page upon unsucessful login
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    # messages.success(request,('Youre now logged out'))
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            # messages.success(request, ('Youre now registered'))
            return redirect('baser')
    else: 
        form = SignUpForm() 

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, ('You have edited your profile'))
            return redirect('home')
    else: 		#passes in user information 
        form = EditProfileForm(instance= request.user) 

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)
    #return render(request, 'authenticate/edit_profile.html',{})



def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # messages.success(request, ('You have edited your password'))
            return redirect('home')
    else: 		#passes in user information 
        form = PasswordChangeForm(user= request.user) 

    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)



def add_person(request):
    if request.method=="POST":
        form=person_form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            form.save()
            obj1=person.objects.get(p_name=data['p_name'])
            dict2={
                'person':obj1
            }
            return render(request,'authenticate/confirmation.html',dict2)
    form=person_form()
    dict_form={
        'form':form
    }
    return render(request,'authenticate/person.html',dict_form)

def add_donor(request):
    if request.method=="POST":
        form=donor_form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            q=data['d_quantity']
            try:
                obj4=donor.objects.get(p_id=data['p_id'])
            except donor.DoesNotExist:
                    obj4 = None 
            if obj4 is None:
                obj2=donor()
                data1=person.objects.get(id=data['p_id'])
                setattr(obj2,'d_name',data1.p_name)
                setattr(obj2,'d_phone',data1.p_phone)
                setattr(obj2,'d_b_group',data1.p_b_group)
                setattr(obj2,'d_quantity',q)
                setattr(obj2,'d_date',current_date)
                setattr(obj2,'d_loc',data1.p_loc)
                setattr(obj2,'p_id',data['p_id'])
                obj2.save()
                obj=stock.objects.get(b_group=data1.p_b_group)
                obj.b_quantity+=q
                obj.save()
                id_dic={
                    'obj2':obj2
                }
                return render(request,'authenticate/conf_donor.html',id_dic)
            else:
                data1=person.objects.get(id=data['p_id'])
                obj4.d_quantity+=q
                obj4.save()
                obj=stock.objects.get(b_group=data1.p_b_group)
                obj.b_quantity+=q
                obj.save()
                id_di={
                    'obj2':obj4
                }
                return render(request,'authenticate/conf_donor.html',id_di)
    form=donor_form()
    dict_form={
        'form':form
    }
    return render(request,'authenticate/donor.html',dict_form)

def stock_show(request):
    data=stock.objects.all()
    return render(request,'authenticate/stock.html',{'data':data})

def request_blood(request):
    if request.method=="POST":
        form=receive_form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            b_g_need=data['r_b_group']
            b_need=data['r_quantity']
            obj1=stock.objects.get(b_group=b_g_need)
            if obj1.b_quantity>=b_need:
                try:
                    obj2 = donor.objects.get(d_b_group=b_g_need)
                except donor.DoesNotExist:
                    obj2 = None 
                if obj2 is None:
                    return render(request,'authenticate/rejected.html')
                else:
                    obj1.b_quantity-=b_need
                    obj1.save()
                    context={
                        'obj2':obj2
                    }
                    username=request.user.username
                    data1= person.objects.get(p_name=username)
                    obj3=receive()
                    setattr(obj3, 'r_name', data1.p_name)
                    setattr(obj3, 'r_phone', data1.p_phone)
                    setattr(obj3, 'r_b_group', data1.p_b_group)
                    setattr(obj3, 'r_quantity', b_need)
                    setattr(obj3, 'r_loc', data1.p_loc)
                    obj3.save()
                    dict={
                        'obj2':obj2
                    }
                    return render(request,'authenticate/assigned_person.html',dict)
            else:
                return render(request,'authenticate/rejected.html')
    form=receive_form()
    dict_form={
        'form':form
    }
    return render(request,'authenticate/receive.html',dict_form)

def search_blood(request):
    if request.method=="POST":
        form=search_form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            bgroup=data['d_b_group']
            # persons = []
            persons = donor.objects.all()
            # stock_b=stock.objects.filter(b_group=bgroup)
            data=stock.objects.all()
            dict={
                'persons':persons,
                'blood':bgroup,
                'data':data
            }
            return render(request,'authenticate/search_show.html',dict)
    form=search_form()
    dict_form={
        'form':form
    }
    return render(request,'authenticate/search.html',dict_form)

def person_info(request):
    data=person.objects.all()
    return render(request,'authenticate/person_info.html',{'data':data})

def donor_info(request):
    data=donor.objects.all()
    return render(request,'authenticate/donor_info.html',{'data':data})