from rest_framework import serializers
from .models import WorkProcessModel
from .models import HomeTestimonialModel
from .models import TeamModel
from .models import Services
from .models import SingleService
from .models import Blog, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'thumbnail', 'excerpt',
            'content', 'category', 'tags', 'created_at', 'views'
        ]
        
class WorkProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProcessModel
        fields=['id', 'title', 'desc', 'inactiveIcon', 'activeIcon']

class HomeTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTestimonialModel
        fields=['id', 'title', 'desc', 'user', 'image', 'prof']       

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields=['id', 'users', 'prof', 'image', 'fburl', 'instaurl', 'linkdinurl', 'twitterurl'] 

class ServicesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Services
        fields = '__all__'

class SingleServiceSerializer(serializers.ModelSerializer):
    service = ServicesSerializer(read_only=True)
    class Meta:
        model = SingleService
        fields = [
            'id',
            'service',
            'slug',
            'featuredimg',
            'moreimg',
            'fulldesc',
            'featureone',
            'featuretwo',
            'process',
            'pricing',
            'processicon1',
            'processicon2',
            'processicon3',
            'moretext'
        ]