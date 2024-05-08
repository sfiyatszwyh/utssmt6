from rest_framework import serializers
from .models import Activity, Category, Schedule

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Activity
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)

    class Meta:
        model = Schedule
        fields = '__all__'
