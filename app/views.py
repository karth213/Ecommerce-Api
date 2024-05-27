from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Product, Category
from . serializers import ProdocutSerializer, CategorySerializer

# Create your views here.

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()[0:4]
        serializer = ProdocutSerializer(products, many = True)
        return Response(serializer.data)

class ProductDetails(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category_slug=category_slug).get(product_slug = product_slug)
        except Product.DoesNotExits:
            raise Http404

    def get(self, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serilazer = ProdocutSerializer(product)
        return Response(serilazer.data)
    

class CategoryView(APIView):
    def get_objects(self, category_slug):
        try:
            Category.objects.get(slug = category_slug)
        except Product.DoesNotExits:
            raise Http404
        
    def get(self, category_slug, format = None):
        category = self.get_object(category_slug)
        serialzer = CategorySerializer(category)
        return Response(serialzer.data)
    

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name_icontains=query) , Q(description_icontains=query))

        serialzer = ProdocutSerializer(products, many=True)
        return Response(serialzer.data)
    else:
        return Response({'product,': []})
    