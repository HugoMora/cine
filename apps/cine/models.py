
from django.db import models

# Create your models here.
class Distrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)        
    ubigeo = models.IntegerField()
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    direccion = models.CharField(max_length=220, blank=False, null=False)    
    distrito_id = models.OneToOneField(Distrito, on_delete=models.CASCADE)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)   
    local_id = models.ManyToManyField(Local)     
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=False, null=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=False, null=False)
    avatar = models.ImageField(upload_to='pictures/actor', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    inicio = models.CharField(max_length=30, blank=False, null=False)
    fin = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['inicio']

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, blank=False, null=False)
    trailer = models.CharField(max_length=220, blank=False, null=False)
    genero = models.ManyToManyField(Genero)
    categoria = models.ManyToManyField(Categoria)
    actor = models.ManyToManyField(Actor)
    duracion = models.CharField(max_length=30, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    imagen = models.ImageField(upload_to='pictures/pelicula', max_length=255, null=True, blank=True)
    idioma = models.CharField(max_length=30, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
