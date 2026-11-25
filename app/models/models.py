# pizzas/models.py
from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField("descripción", blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("pizzas:categoria_detail", kwargs={"pk": self.pk})


class Pizza(models.Model):
    class Tamano(models.TextChoices):
        PERSONAL = "PERSONAL", "Personal"
        MEDIANA = "MEDIANA", "Mediana"
        FAMILIAR = "FAMILIAR", "Familiar"

    nombre = models.CharField(max_length=80)
    descripcion = models.TextField("descripción", blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    tamano = models.CharField(
        "tamaño",
        max_length=10,
        choices=Tamano.choices,
        default=Tamano.MEDIANA,
    )
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="pizzas",
    )
    creada_en = models.DateTimeField("creada en", auto_now_add=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.get_tamano_display()})"

    def get_absolute_url(self):
        return reverse("pizzas:pizza_detail", kwargs={"pk": self.pk})