from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Category, Location
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    """
        This function takes:
            1. request object as a parameter, that is by the URLconf.
        This functions retrieves all images and renders them to index.html in homepage folder.   
    """
    images = Image.objects.all()
    locations = []
    locations_all = Location.objects.all()
    for i in locations_all:
        if i.name not in locations:
            locations.append(i.name)  
    return render(request,'homepage/index.html', {'images':images, 'locations':locations})
    
def search_results(request):
    """
        This function takes request instance as a parameter from URLconf.
        This function is responsible for extracting the value entered by the user from the search form. 
        The function then uses that value and cross checks it with category, after querying all names of Category.
        If a match is found the id for that particular category is extracted and is used to query the Image table.
    """
    if 'category' in request.GET and request.GET['category']:
            try: 
                search_term_original = request.GET.get('category') 
                search_term = search_term_original.lower()
                category_all = Category.objects.all()
                images_final = []
                for i in category_all:
                    if search_term == i.name:
                        searched_images = Image.search_image(i.id)
                        images_final.append(searched_images)
                message = f'{search_term_original}'
                return render(request, 'search/search_results.html', {'message':message, 'searched_images':searched_images, 'images_final':images_final })
            except:
                raise Http404()               
    else: 
        message = 'You haven\'t searchded for any term'
        return render(request, 'search/search_results.html', {'message':message})

