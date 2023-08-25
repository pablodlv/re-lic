from django import forms

class remateForm(forms.Form):
    bien=forms.CharField(max_length=80)
    base=forms.IntegerField()
    fecha=forms.DateField()
    lugar=forms.CharField()

class licitacionForm(forms.Form):
    objeto=forms.CharField(max_length=80)
    referencia=forms.CharField(max_length=30)
    fecha=forms.DateField()
    link=forms.URLField()

class martilleroForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    matricula=forms.IntegerField()
    email=forms.EmailField()
    
class clienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    numero_de_cliente=forms.IntegerField()
    email=forms.EmailField()

class operadorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    