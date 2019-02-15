from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request,'learn_blogs/index.html')

def topics(request):
    topics=Topic.objects.order_by('date')
    context={'topics':topics}
    return render(request,'learn_blogs/topics.html',context)

def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('date')
    context={
        'topic':topic,
        'entries':entries
    }
    return render(request,'learn_blogs/topic.html',context)

# Create your views here.
