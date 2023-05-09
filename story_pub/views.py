from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create levels views here.

def get_stories( request):
    _levels = story.objects.all().values()
    _levels = list(_levels)
    for lev in _levels :
        id = lev['id']
        ref = story.objects.all().filter(id=id)[0]
        files = story_files.objects.all().filter(story=ref)
        files = [{'id':item.id ,'url': item.file.url }for item in files]
        lev['files'] = files
    return JsonResponse(_levels ,safe=False)


@csrf_exempt
def post_stories( request):
        # <view logic>
    data = request.POST
    order = data['order']
    title = data['title']
    try:
        page_de = request.FILES['page_de_gard']
        new = story(title = title , page_de_garde =page_de , order = order)
    except:
        new = story(title = title  , order = order)
        new.save()
    files = request.FILES
    keys = files.keys()
    for i in keys :
        st = story_files(file = files[i] ,story = new )
        st.save()        
    return JsonResponse({'message':'Posted Succeffuly'})

@csrf_exempt
def put_stories( request):
        # <view logic>
    data = request.POST
    id  = data['id']
    try : 
        people = story.objects.all().filter(id=id).update(title= request.POST['title'])
    except:
        pass
    try : 
        people = story.objects.all().filter(id=id).update(order= request.POST['order'])
    except:
        pass
    try : 
        people = story.objects.all().filter(id=id).update(page_de_garde= request.FILES['page_de_garde'])
    except:
        pass
    # <view logic>
    try:
        files = request.FILES
        keys = files.keys()
        people = story.objects.all().filter(id=id)
        for i in keys :
            st = story_files(file = files[i] ,story = people)
            st.save()
    except:
        pass        
    return JsonResponse({'message':'updated Succeffuly'})

@csrf_exempt
def remove_stories(request):
        # <view logic>
    data = request.POST
    id = data['id']
    print('hadi' ,id)
    fre  = story.objects.all().filter(id=id)
    print(fre)
    files = story_files.objects.all().filter(story=fre).delete()
    people = story.objects.all().filter(id=id).delete()
    return JsonResponse({'message':'removed Succeffuly'})



@csrf_exempt
def remove_stories_files(request):
        # <view logic>
    data = request.POST
    id = data['id']
    story  = story_files.objects.all().filter(id=id)
    return JsonResponse({'message':'removed Succeffuly'})


#Create your pub here.

@csrf_exempt
def get_pubs( request):
    _levels = Pub.objects.all().values()
    _levels = list(_levels)
    return JsonResponse(_levels ,safe=False)

@csrf_exempt
def post_pubs( request):
    data = request.POST
    url = data['url']
    image = request.FILES['image']
    new = Pub(url = url , image_de_garde = image)
    new.save()
    return  HttpResponse("updated succeffluy")

@csrf_exempt
def put_pubs( request):
    data = request.POST
    id = data['id']
    try : 
        people = Pub.objects.all().filter(id=id).update(url= request.POST['url'])
    except:
        pass
    try : 
        people = Pub.objects.all().filter(id=id).update(order= request.FILES['image'])
    except:
        pass
    return  HttpResponse("updated succeffluy")

@csrf_exempt
def remove_pubs( request):
    data = request.POST
    id = data['id']
    Pub.objects.all().filter(id=id).delete()
    return  HttpResponse("updated succeffluy")