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

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        activity = Activity.objects.create(category=category, **validated_data)
        return activity

class ScheduleSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)

    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        activities_data = validated_data.pop('activities')
        schedule = Schedule.objects.create(**validated_data)
        for activity_data in activities_data:
            category_data = activity_data.pop('category')
            category = Category.objects.create(**category_data)
            activity = Activity.objects.create(schedule=schedule, category=category, **activity_data)
        return schedule
