from rest_framework import serializers
from .models import Workout

# 把数据库数据转JSON，DRF自动处理，返回符合要求的JSON响应
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'  # 所有字段都转JSON，包括自动生成的ID
