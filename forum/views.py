from django.shortcuts import render, get_object_or_404, redirect
from forum.models import Section, Topic, Post
from forum.forms import PostForm, TopicForm
from datetime import datetime

# --- Розділи форуму ---
def sections(request):
    
    sections = Section.objects.all()    
    context = {'sections': sections}
    return render(request, 'forum/sections.html', context)

# --- Теми розділу ---
def topics(request, section_id):
    
    form = TopicForm(request.POST or None)
    
    section = get_object_or_404(Section, pk=section_id)
    topics = Topic.objects.filter(section=section_id)    
    context = {'section': section, 
               'topics': topics,
               'form': form}
    return render(request, 'forum/topics.html', context)
    
# --- Пости теми ---
def posts(request, section_id, topic_id):
    
    form = PostForm(request.POST or None)
    
    section = get_object_or_404(Section, pk=section_id)
    topic = get_object_or_404(Topic, pk=topic_id)
    posts = Post.objects.filter(topic=topic_id)    
    context = {'section': section, 
               'topic': topic, 
               'posts': posts, 
               'form': form}
    return render(request, 'forum/posts.html', context)

# --- Добавити повідомлення ---
def addpost(request, section_id, topic_id):

    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.topic = get_object_or_404(Topic, pk=topic_id)
        post.timestamp = datetime.today()
        post.author = request.user.username
        post.save()
        
    return redirect(posts, section_id, topic_id)

# --- Добавити тему ---
def addtopic(request, section_id):

    form = TopicForm(request.POST or None)

    if form.is_valid():
        topic = form.save(commit=False)
        topic.section = get_object_or_404(Section, pk=section_id)
        topic.timestamp = datetime.today()
        topic.author = request.user.username
        topic.save()
        
    return redirect(topics, section_id)
  

        