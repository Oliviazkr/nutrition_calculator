from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from calculator.models import FoodItem


class Command(BaseCommand):
    help = 'Initialize demo data'

    def handle(self, *args, **options):
        self.stdout.write('Creating demo data...')

        # 创建演示用户
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user(
                username='demo',
                email='demo@example.com',
                password='demo123456'
            )
            self.stdout.write('  Created demo user (username: demo, password: demo123456)')
        else:
            self.stdout.write('  Demo user already exists')

        # 创建示例食物数据
        sample_foods = [
            # 蔬菜类
            {'name': '西兰花', 'category': 'vegetables', 'calories': 34, 'protein': 2.8, 'carbs': 6.6, 'fat': 0.4,
             'fiber': 2.6, 'sugar': 1.7},
            {'name': '菠菜', 'category': 'vegetables', 'calories': 23, 'protein': 2.9, 'carbs': 3.6, 'fat': 0.4,
             'fiber': 2.2, 'sugar': 0.4},
            {'name': '胡萝卜', 'category': 'vegetables', 'calories': 41, 'protein': 0.9, 'carbs': 9.6, 'fat': 0.2,
             'fiber': 2.8, 'sugar': 4.7},
            {'name': '番茄', 'category': 'vegetables', 'calories': 18, 'protein': 0.9, 'carbs': 3.9, 'fat': 0.2,
             'fiber': 1.2, 'sugar': 2.6},
            {'name': '黄瓜', 'category': 'vegetables', 'calories': 15, 'protein': 0.7, 'carbs': 3.6, 'fat': 0.1,
             'fiber': 0.5, 'sugar': 1.7},
            {'name': '生菜', 'category': 'vegetables', 'calories': 15, 'protein': 1.4, 'carbs': 2.9, 'fat': 0.2,
             'fiber': 1.3, 'sugar': 0.8},

            # 水果类
            {'name': '苹果', 'category': 'fruits', 'calories': 52, 'protein': 0.3, 'carbs': 13.8, 'fat': 0.2,
             'fiber': 2.4, 'sugar': 10.4},
            {'name': '香蕉', 'category': 'fruits', 'calories': 89, 'protein': 1.1, 'carbs': 22.8, 'fat': 0.3,
             'fiber': 2.6, 'sugar': 12.2},
            {'name': '橙子', 'category': 'fruits', 'calories': 47, 'protein': 0.9, 'carbs': 11.8, 'fat': 0.1,
             'fiber': 2.4, 'sugar': 9.4},
            {'name': '草莓', 'category': 'fruits', 'calories': 32, 'protein': 0.7, 'carbs': 7.7, 'fat': 0.3,
             'fiber': 2.0, 'sugar': 4.9},
            {'name': '蓝莓', 'category': 'fruits', 'calories': 57, 'protein': 0.7, 'carbs': 14.5, 'fat': 0.3,
             'fiber': 2.4, 'sugar': 10.0},

            # 肉类
            {'name': '鸡胸肉', 'category': 'meat', 'calories': 165, 'protein': 31.0, 'carbs': 0, 'fat': 3.6, 'fiber': 0,
             'sugar': 0},
            {'name': '鸡腿肉', 'category': 'meat', 'calories': 209, 'protein': 26.0, 'carbs': 0, 'fat': 10.9,
             'fiber': 0, 'sugar': 0},
            {'name': '牛肉（瘦）', 'category': 'meat', 'calories': 250, 'protein': 26.0, 'carbs': 0, 'fat': 15.0,
             'fiber': 0, 'sugar': 0},
            {'name': '猪里脊', 'category': 'meat', 'calories': 242, 'protein': 27.0, 'carbs': 0, 'fat': 14.0,
             'fiber': 0, 'sugar': 0},

            # 海鲜
            {'name': '三文鱼', 'category': 'seafood', 'calories': 208, 'protein': 20.4, 'carbs': 0, 'fat': 13.4,
             'fiber': 0, 'sugar': 0},
            {'name': '虾', 'category': 'seafood', 'calories': 85, 'protein': 20.0, 'carbs': 0, 'fat': 0.5, 'fiber': 0,
             'sugar': 0},
            {'name': '鳕鱼', 'category': 'seafood', 'calories': 82, 'protein': 18.0, 'carbs': 0, 'fat': 0.7, 'fiber': 0,
             'sugar': 0},

            # 乳制品
            {'name': '牛奶（全脂）', 'category': 'dairy', 'calories': 61, 'protein': 3.2, 'carbs': 4.8, 'fat': 3.3,
             'fiber': 0, 'sugar': 5.0},
            {'name': '酸奶（原味）', 'category': 'dairy', 'calories': 59, 'protein': 3.5, 'carbs': 3.6, 'fat': 3.3,
             'fiber': 0, 'sugar': 3.2},
            {'name': '鸡蛋', 'category': 'dairy', 'calories': 143, 'protein': 12.6, 'carbs': 0.7, 'fat': 9.5,
             'fiber': 0, 'sugar': 0.4},
            {'name': '奶酪（切达）', 'category': 'dairy', 'calories': 404, 'protein': 23.0, 'carbs': 3.1, 'fat': 33.0,
             'fiber': 0, 'sugar': 0.5},

            # 谷物
            {'name': '白米饭', 'category': 'grains', 'calories': 130, 'protein': 2.4, 'carbs': 28.0, 'fat': 0.2,
             'fiber': 0.4, 'sugar': 0.1},
            {'name': '糙米饭', 'category': 'grains', 'calories': 111, 'protein': 2.6, 'carbs': 23.0, 'fat': 0.9,
             'fiber': 1.8, 'sugar': 0.4},
            {'name': '全麦面包', 'category': 'grains', 'calories': 247, 'protein': 13.0, 'carbs': 41.0, 'fat': 3.4,
             'fiber': 7.0, 'sugar': 6.0},
            {'name': '燕麦', 'category': 'grains', 'calories': 389, 'protein': 16.9, 'carbs': 66.3, 'fat': 6.9,
             'fiber': 10.6, 'sugar': 0},
            {'name': '意大利面', 'category': 'grains', 'calories': 131, 'protein': 5.0, 'carbs': 25.0, 'fat': 1.1,
             'fiber': 1.8, 'sugar': 0.6},

            # 坚果
            {'name': '杏仁', 'category': 'nuts', 'calories': 579, 'protein': 21.2, 'carbs': 21.6, 'fat': 49.9,
             'fiber': 12.5, 'sugar': 4.4},
            {'name': '核桃', 'category': 'nuts', 'calories': 654, 'protein': 15.2, 'carbs': 13.7, 'fat': 65.2,
             'fiber': 6.7, 'sugar': 2.6},
            {'name': '花生', 'category': 'nuts', 'calories': 567, 'protein': 25.8, 'carbs': 16.1, 'fat': 49.2,
             'fiber': 8.5, 'sugar': 4.7},

            # 饮料
            {'name': '咖啡（黑）', 'category': 'beverages', 'calories': 1, 'protein': 0.1, 'carbs': 0, 'fat': 0,
             'fiber': 0, 'sugar': 0},
            {'name': '绿茶', 'category': 'beverages', 'calories': 1, 'protein': 0.2, 'carbs': 0, 'fat': 0, 'fiber': 0,
             'sugar': 0},
            {'name': '橙汁', 'category': 'beverages', 'calories': 45, 'protein': 0.7, 'carbs': 10.4, 'fat': 0.2,
             'fiber': 0.2, 'sugar': 8.4},

            # 零食
            {'name': '黑巧克力（70%）', 'category': 'snacks', 'calories': 598, 'protein': 7.8, 'carbs': 45.9, 'fat': 42.6,
             'fiber': 10.9, 'sugar': 24.0},
            {'name': '薯片', 'category': 'snacks', 'calories': 536, 'protein': 7.0, 'carbs': 53.0, 'fat': 35.0,
             'fiber': 4.0, 'sugar': 0},
        ]

        created = 0
        for food_data in sample_foods:
            _, created_flag = FoodItem.objects.get_or_create(
                name=food_data['name'],
                defaults=food_data
            )
            if created_flag:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'  Created {created} new food items'))
        self.stdout.write(self.style.SUCCESS('\nDemo data initialized successfully!'))
        self.stdout.write('\nYou can now login with:')
        self.stdout.write('  Username: demo')
        self.stdout.write('  Password: demo123456')