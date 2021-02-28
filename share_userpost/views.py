from django.shortcuts import render,redirect
from django.views import generic,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.contrib import messages

from .models import UserPost, Picture
from .forms import UserPostCreationForm, PictureCreationForm
from .decorators import login_required, open_to_user_groups
# Create your views here.

class HomeView(View):
    template_name = "home.html"
    @login_required
    @open_to_user_groups(user_groups=["admin","authorized_user"],redirect_html="no_access.html")
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
        
class EventView(HomeView):
    template_name = "event.html"
    
class AllPostsView(View):
    template_name = "posts.html"
    queryset = UserPost.objects.all()
    success_template = "posts.html"
    failure_template = "home.html"
    
    def get_queryset(self,request):
        return self.queryset.order_by("-created_at")

    def get_unique_pictures(self):
        pictures = Picture.objects.all()
        output_pictures = []
        output_pictures_post_ids = []
        for picture in pictures:
            if picture.post.id in output_pictures_post_ids:
                continue
            else:
                output_pictures.append(picture)
                output_pictures_post_ids.append(picture.post.id)
        return output_pictures

    
    @login_required
    @open_to_user_groups(user_groups=["admin","authorized_user"],redirect_html="no_access.html")
    def get(self,request,*args,**kwargs):
        userpost_form = UserPostCreationForm()
        context = {"userpost_list":self.get_queryset(request),
                   "userpost_form":userpost_form,
                   "pictures":self.get_unique_pictures()}
        return render(request, self.template_name, context) 

    def post(self,request,*args,**kwargs):
        post_form = UserPostCreationForm(request.POST,request.FILES)
        images = request.FILES.getlist("image")
        picture_form = PictureCreationForm(request.POST, request.FILES)     
        if post_form.is_valid():	            
            userpost = post_form.save(commit=False)
            userpost.user = request.user
            userpost.save()
            for image in images:
                picture_form = PictureCreationForm(request.POST,{"image":image})
                picture = picture_form.save()
                picture.post = userpost
                picture.save()              
            messages.success(request,"投稿しました")    
            return redirect("share_userpost:all_posts")
        else:
            messages.error(request,"投稿に失敗しました")
            print("failed")	
            return render(request,self.failure_template)

class SelfPostsView(AllPostsView):
    success_template = "posts.html"
    def get_queryset(self,request):
        queryset = self.queryset.filter(user = request.user).order_by("-created_at")
        return queryset
        
class PostDetailView(View):
    post_detail_template = "post_detail.html"

    def get_post_photos(self, post_id):
        pictures = [photo for photo in Picture.objects.all() if photo.post.id == post_id]
        return pictures
    
    @login_required
    @open_to_user_groups(user_groups=["admin","authorized_user"],redirect_html="no_access.html")
    def get(self,request,post_id=None,*args,**kwargs):
        post = UserPost.objects.get(id=post_id)
        photos = self.get_post_photos(post_id)
        context = {"post":post,
                   "photos":self.get_post_photos(post_id)}
        return render(request,self.post_detail_template,context)

class DeletePostView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = UserPost.objects.get(id=post_id)
        if post:
            post.delete()
        return redirect("share_userpost:all_posts")


