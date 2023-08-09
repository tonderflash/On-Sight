""" Test for Recipe API """
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import (RecipeSerializer,
                                RecipeDetailSerializer,)

RECIPES_URL = reverse('recipe:recipe-list')

def detail_url(recipe_id):
    """create and return a recipe detail url"""
    return reverse('recipe:recipe-detail', args=[recipe_id])

def create_recipe(user, **params):
    """Helper function to create a recipe"""
    defaults = {
        'title': 'Sample Recipe',
        'description': 'Sample Description',
        'time_minutes': 10,
        'price': Decimal('5.00'),
        'link': 'https://www.example.com/recipe'
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe

class PublicRecipeAPITests(TestCase):
    """Test unauthenticated recipe API access"""
    
    def setUp(self):
        self.client = APIClient()
        
    def test_auth_required(self):
        """Test that authentication is required"""
        res = self.client.get(RECIPES_URL)
        
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        
class PrivateRecipeApiTests(TestCase):
    """Test authenticated recipe API access"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'test123',
        )
        self.client.force_authenticate(self.user)
        
    def test_retrieve_recipes(self):
        """ Test retrieving a list of recipes"""
        create_recipe(user=self.user)
        create_recipe(user=self.user)
        
        res = self.client.get(RECIPES_URL)
        
        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    
    def test_recipes_limited_to_user(self):
        """Test retrieving recipes for user"""
        other_user = get_user_model().objects.create_user(
            'other@example.com',
            'test123'
        )
        create_recipe(user=other_user)
        create_recipe(user=self.user)
        
        res = self.client.get(RECIPES_URL)
        
        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    def test_get_recipe_detail(self):
        """Test retrieving a recipe detail"""
        recipe = create_recipe(user=self.user)
        
        url = detail_url(recipe.id)
        res = self.client.get(url)
        
        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(res.data, serializer.data)
       