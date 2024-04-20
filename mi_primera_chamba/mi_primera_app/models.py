from django.db import models

# Create your models here.
class Topic(models.Model):
    #Definir los campos que tiene la tabla
    top_name = models.CharField(max_length=100,unique=True)

    #Representar el registro como cadena de texto
    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    #Definir los campos que tiene la tabla
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

     #Representar el registro como cadena de texto
    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    webname = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    #Representar el registro como cadena de texto
    def __str__(self):
        return str(self.date)
    
class ElProfe(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email

class nombre_del_equipo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email

class Comments(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    text = models.CharField(max_length=100)


    def __str__(self):
        return self.email