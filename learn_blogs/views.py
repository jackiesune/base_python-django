from django.shortcuts import render
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def new_topic(request):
    if request.method!='POST':
        form=TopicForm()
    else:
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learn_blogs:topics'))

    context={'form':form}
    return render(request,'learn_blogs/new_topic.html',context)

def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method!='POST':
        form=EntryForm()

    else:
        form=EntryForm(request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learn_blogs:topic',args=[topic_id]))

    context={'form':form,'topic':topic}
    return render(request,'learn_blogs/new_entry.html',context)

def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if request.method!="POST":
        form=EntryForm(entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('learn_blogs:topic',args=[topic.id]))
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learn_blogs/edit_entry.html',context)










# Create your views here.
