from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Китай')
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class GamingMouse(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    sensor_type = models.CharField(
        max_length=50,
        choices=[
            ('optical', 'Оптичний'),
            ('laser', 'Лазерний')
        ],
        default='optical'
    )
    dpi = models.PositiveIntegerField(default=800)
    weight = models.PositiveIntegerField(help_text="В грамах")
    color = models.CharField(max_length=50, default='Чорний')
    is_wireless = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=10)
    release_date = models.DateField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"
