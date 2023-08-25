from django.db import models

# Create your models here.

# Clase remate con algunos de los datos de un remate judicial
 
class Remate(models.Model):

    bien = models.CharField(max_length=90)
    base = models.IntegerField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.bien} - ${self.base} - {self.fecha} - {self.lugar}'

# La clase Licitaciones tiene los campos de la convocatoria
    
class Licitacion(models.Model):

    objeto = models.CharField(max_length=90)
    referencia = models.CharField(max_length=60)
    fecha = models.DateField()
    link = models.URLField()
    def __str__(self):
        return f'{self.objeto} - {self.referencia} - {self.fecha} - {self.link}'


# El cliente usuario del frontend
class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_de_cliente = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.numero_de_cliente} - {self.email}'

# El data-entry que carga remates y licitaciones

class Operador(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email}'

# Usuario de la app y puede cargar remates

class Martillero(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    matricula = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.matricula} - {self.email}'