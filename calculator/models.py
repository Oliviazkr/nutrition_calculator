from django.db import models
from django.contrib.auth.models import User


class FoodItem(models.Model):
    """食物/食材模型"""

    CATEGORY_CHOICES = [
        ('vegetables', '蔬菜'),
        ('fruits', '水果'),
        ('meat', '肉类'),
        ('seafood', '海鲜'),
        ('dairy', '乳制品'),
        ('grains', '谷物'),
        ('nuts', '坚果'),
        ('beverages', '饮料'),
        ('snacks', '零食'),
        ('other', '其他'),
    ]

    name = models.CharField(max_length=200, unique=True, verbose_name='名称')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other', verbose_name='分类')

    # 每100g的营养信息
    calories = models.FloatField(default=0, verbose_name='卡路里 (kcal/100g)')
    protein = models.FloatField(default=0, verbose_name='蛋白质 (g/100g)')
    carbs = models.FloatField(default=0, verbose_name='碳水化合物 (g/100g)')
    fat = models.FloatField(default=0, verbose_name='脂肪 (g/100g)')
    fiber = models.FloatField(default=0, verbose_name='膳食纤维 (g/100g)')
    sugar = models.FloatField(default=0, verbose_name='糖 (g/100g)')

    # 其他信息
    serving_size = models.FloatField(default=100, verbose_name='标准份量(g)')
    serving_name = models.CharField(max_length=50, default='100g', verbose_name='份量名称')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal/100g)"

    class Meta:
        ordering = ['name']
        verbose_name = '食物'
        verbose_name_plural = '食物'


class CalculationHistory(models.Model):
    """计算历史记录"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, default='My Meal', verbose_name='名称')

    # 存储为 JSON
    items = models.TextField(verbose_name='食物列表(JSON)')

    # 计算结果
    total_weight = models.FloatField(default=0, verbose_name='总重量(g)')
    total_calories = models.FloatField(default=0, verbose_name='总卡路里')
    total_protein = models.FloatField(default=0, verbose_name='总蛋白质')
    total_carbs = models.FloatField(default=0, verbose_name='总碳水')
    total_fat = models.FloatField(default=0, verbose_name='总脂肪')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.total_calories:.0f} kcal"

    class Meta:
        ordering = ['-created_at']
        verbose_name = '计算历史'
        verbose_name_plural = '计算历史'