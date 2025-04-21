from django.db import models

class Usuario(models.Model):
    id_usu = models.AutoField(primary_key=True, help_text="ID único")
    correo = models.EmailField(max_length=254, help_text="Correo electrónico")
    contraseña = models.CharField(max_length=50, help_text="Contraseña")
    genero_uno = models.CharField(max_length=50)
    genero_dos = models.CharField(max_length=50, blank=True, null=True)

class libro(models.Model):
    id_libro = models.AutoField(primary_key=True, help_text="Id único")
    titulo = models.CharField(max_length=250, help_text="titulo")
    genero = models.CharField(help_text="genero")
    descripcion = models.CharField(max_length=3000, help_text="descripcion")
    publicacion = models.IntegerField(help_text="publicacion")
    puntuacion = models.IntegerField(help_text="puntuacion")

class recomendacion(models.Model):
    id_recomendacion = models.AutoField(primary_key=True, help_text="Id único")
    id_usu = models.ForeignKey("usuario", verbose_name=("usuario"), on_delete=models.CASCADE)
    id_libro = models.ForeignKey("libro", verbose_name=("libro"), on_delete=models.CASCADE)
    motivo = models.CharField(help_text="motivo") # solo dos opciones genero o sentimiento

class interaccion(models.Model):
    id_interaccion = models.AutoField(primary_key=True, help_text="Id único")
    id_usu = models.ForeignKey("usuario", verbose_name=("usuario"), on_delete=models.CASCADE)
    id_libro = models.ForeignKey("libro", verbose_name=("libro"), on_delete=models.CASCADE)
    interaccion = models.CharField(help_text="interaccion") 
    calificacion = models.IntegerField(help_text="calificacion")

    

