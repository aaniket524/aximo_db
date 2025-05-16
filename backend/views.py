
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import WorkProcessModel
from .serializers import WorkProcessSerializer
from .models import HomeTestimonialModel
from .serializers import HomeTestimonialSerializer
from .models import TeamModel
from .serializers import TeamSerializer
# Create your views here.


from .models import Services, SingleService
from .serializers import ServicesSerializer, SingleServiceSerializer
from .models import Blog, Category, Tag
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_all_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_blog_detail(request, category_slug, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug, category__slug=category_slug)
    blog.views += 1
    blog.save()
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['GET'])
def get_blogs_by_category(request, category_slug):
    blogs = Blog.objects.filter(category__slug=category_slug)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_blogs_by_tag(request, tag_slug):
    blogs = Blog.objects.filter(tags__slug=tag_slug)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

# Get all services
@api_view(['GET'])
def get_all_services(request):
    services = Services.objects.all().order_by('order')
    serializer = ServicesSerializer(services, many=True)
    return Response(serializer.data)

# Get a single service by slug
@api_view(['GET'])
def get_single_service_by_slug(request, slug):
    try:
        service = Services.objects.get(slug=slug)
        serializer = ServicesSerializer(service)
        return Response(serializer.data)
    except Services.DoesNotExist:
        return Response({"error": "Service not found"}, status=404)

# Get all single service detail pages
@api_view(['GET'])
def get_all_single_services(request):
    singles = SingleService.objects.all()
    serializer = SingleServiceSerializer(singles, many=True)
    return Response(serializer.data)

# Get single service detail by the linked service slug
@api_view(['GET'])
def get_single_service_detail(request, slug):
    try:
        single = SingleService.objects.select_related('service').get(service__slug=slug)
        serializer = SingleServiceSerializer(single)
        return Response(serializer.data)
    except SingleService.DoesNotExist:
        return Response({"error": "SingleService not found"}, status=404)
@api_view(['GET'])
def get_workprocess_data(request):
    workprocess = WorkProcessModel.objects.all().order_by('id')
    serializer = WorkProcessSerializer(workprocess, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_htesti_data(request):
    htesti = HomeTestimonialModel.objects.all().order_by('id')
    serializer = HomeTestimonialSerializer(htesti, many = True)
    return Response(serializer.data) 

@api_view(['GET'])
def get_team_data(request):
    team = TeamModel.objects.all().order_by('id')
    serializer = TeamSerializer(team, many = True)
    return Response(serializer.data)

