square_matrix=[],[]
filas=input("inggrese el numero de filas")
filas=int(filas)

Columnas=input("inggrese el numero de filas")
Columnas=int(Columnas)

for i in range(filas):
    for j in range(Columnas):
        number = int(input("Enter a value between 1 and 16: "))
        square_matrix[i][j] = number


        <div class="form-row form-floating">
                    <div class="col form-group ">
                        <label>Nombre</label>
                        {{ form.first_name }}
                    </div> <!-- form-group end.// -->
                    <div class="col form-group ">
                        <label>Apellido</label>
                        {{ form.last_name }}
                    </div> <!-- form-group end.// -->
                </div> <!-- form-row end.// -->
                <div class="form-row form-floating">
                    <div class="col form-group">
                        <label>Numero Telefonico</label>
                        {{ form.phone_number }}
                    </div> <!-- form-group end.// -->
                    <div class="col form-group">
                        <label>Email</label>
                        {{ form.email }}
                    </div> <!-- form-group end.// -->
                </div> <!-- form-row end.// -->
                
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <label>Crear password</label>
                        {{ form.password }}
                    </div> <!-- form-group end.// -->
                    <div class="form-group col-md-6">
                        <label>Repetir password</label>
                        {{ form.confirm_password }}
                    </div> <!-- form-group end.// -->
                </div>




                def register(request):
    form= RegistrationForm()
    if request.method == 'POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user= Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username, password=password)
            user.phone_number = phone_number
            user.save()
    context = {
        'form' :form
    }