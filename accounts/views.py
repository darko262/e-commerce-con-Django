from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm,CustomUserCreationForm,AuthenticationForm
from .models import Account
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from carts.views import _cart_id
from carts.models import Cart,CartItem
# Create your views here.
def register(request):
    data={
    'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario= CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            email=formulario.cleaned_data['email']
           
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            if user is not None :
                user.is_active= False
                user.save()
            #login(request,user)
            current_site = get_current_site(request)
            mail_subject= 'Porfavor activar tu cuenta en smartpet'
            body= render_to_string('accounts/accounts_verification_email.html',{
                'user':user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            send_email=EmailMessage(mail_subject,body,to=[to_email])
            send_email.send()
            #messages.success(request,"Te has registrado correctamente")
            return redirect('/accounts/login/?command=verification&email=' +email)
        data["form" ]=formulario

    return render(request, 'accounts/register.html', data)

def login_2(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")
            usuario= authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    is_cart_item_exist = CartItem.objects.filter(cart=cart).exists()
                    if is_cart_item_exist:
                        cart_item = CartItem.objects.filter(cart=cart)
                        product_variation=[]
                        for item in cart_item:
                            varation = item.variations.all()
                            product_variation.append(list(varation))

                        cart_item=CartItem.objects.filter(user=usuario)
                        ex_va_list=[]
                        id=[]
                        for item in cart_item:
                                existing_variation= item.variations.all()
                                ex_va_list.append(list(existing_variation))
                                id.append(item.id)
                        for pr in product_variation:
                            if pr in ex_va_list:
                                index=ex_va_list.index(pr)
                                item_id= id[index]
                                item = CartItem.objects.get(id=item_id)
                                item.quantity +=1
                                item.user =usuario
                                item.save()
                            else:
                                cart_item=CartItem.objects.filter(cart=cart)
                                for item in cart_item:
                                    item.user = usuario
                                    item.save()
                except:
                    pass
                login(request, usuario)
                messages.success (request, 'Has iniciado sesion exitosamente')
                return redirect(to="dashboard")
            else:
                messages.error(request,"Usuario no valido")
        else:
            messages.error(request,"Informacion incorrecta")
    form= AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect(to="principal")


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user= None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active= True
        user.save()
        messages.success(request, 'felicidades tu cuenta esta activa!')
        return redirect('login')
    else:
        
        messages.error(request,'la activacion es invalida')
        return redirect('register')
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def forgotpassword(request):
    data2={
    'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        email =request.POST['email']
        if User.objects.filter(email=email).exists():
            user= User.objects.get(email__exact=email)
            current_site = get_current_site(request)
            mail_subject= 'Resetear Password'
            body= render_to_string('accounts/reset_password_email.html',{
                'user':user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            send_email=EmailMessage(mail_subject,body,to=[to_email])
            send_email.send()

            messages.success(request,"un email fue enviado a tu bandeja de entrada")
            return redirect('login')
        else:
            messages.success(request,"La cuenta de usuario no existe")
            return redirect('forgotpassword')

    return render(request,'accounts/forgotpassword.html',data2)


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user= None

    if user is not None and default_token_generator.check_token(user, token):
        request.session["uid"] = uid
        print(request)
        messages.success(request,"Por favor resetea tu password")
        return redirect('resetPassword')
    else:
        messages.success(request,"el link ha expirado")
        return redirect('login')

def resetPassword(request):
    data2={
    'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        password= request.POST['password1']
        confirm_password= request.POST['password2']
        if password == confirm_password:
            try:
                uid = request.session.get('uid')
                print( uid)
                user= User.objects.get(pk=uid)
                user.set_password(password)
                user.save()
                messages.success(request,"El password se reseteo correctamente")
                return redirect('login')
            except User.DoesNotExist:
                messages.success(request,"ERRORR")
                return redirect('login')
            
        else:
            messages.success(request," El password de confirmacion no concuerda")
            return redirect ('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html',data2)