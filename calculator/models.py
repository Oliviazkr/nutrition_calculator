from django.db import models
from django.contrib.auth.models import User


class FoodItem(models.Model):
    """Food/Ingredient Model"""

    CATEGORY_CHOICES = [
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('meat', 'Meat'),
        ('seafood', 'Seafood'),
        ('dairy', 'Dairy'),
        ('grains', 'Grains'),
        ('nuts', 'Nuts'),
        ('beverages', 'Beverages'),
        ('snacks', 'Snacks'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200, unique=True, verbose_name='Name')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other', verbose_name='Category')

    # Nutrition information per 100g
    calories = models.FloatField(default=0, verbose_name='Calories (kcal/100g)')
    protein = models.FloatField(default=0, verbose_name='Protein (g/100g)')
    carbs = models.FloatField(default=0, verbose_name='Carbohydrates (g/100g)')
    fat = models.FloatField(default=0, verbose_name='Fat (g/100g)')
    fiber = models.FloatField(default=0, verbose_name='Dietary Fiber (g/100g)')
    sugar = models.FloatField(default=0, verbose_name='Sugar (g/100g)')

    # Other information
    serving_size = models.FloatField(default=100, verbose_name='Serving Size (g)')
    serving_name = models.CharField(max_length=50, default='100g', verbose_name='Serving Name')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal/100g)"

    class Meta:
        ordering = ['name']
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class CalculationHistory(models.Model):
    """Calculation History Model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, default='My Meal', verbose_name='Name')

    # Stored as JSON
    items = models.TextField(verbose_name='Food Items (JSON)')

    # Calculation results
    total_weight = models.FloatField(default=0, verbose_name='Total Weight (g)')
    total_calories = models.FloatField(default=0, verbose_name='Total Calories')
    total_protein = models.FloatField(default=0, verbose_name='Total Protein')
    total_carbs = models.FloatField(default=0, verbose_name='Total Carbohydrates')
    total_fat = models.FloatField(default=0, verbose_name='Total Fat')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.total_calories:.0f} kcal"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Calculation History'
        verbose_name_plural = 'Calculation History'
