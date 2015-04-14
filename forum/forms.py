from django.forms import ModelForm
from forum.models import Post, Topic

class PostForm(ModelForm):
     
    class Meta:
        model = Post
        #fields = ["author", "body"]
        fields = ["body"]
        
class TopicForm(ModelForm):
    
    class Meta:
        model = Topic
        #fields = ["author", "title", "description"]
        fields = ["title", "description"]