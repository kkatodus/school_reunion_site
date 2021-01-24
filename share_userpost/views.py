from django.shortcuts import render,redirect
from django.views import generic,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.contrib import messages



from .models import UserPost
from .forms import UserPostCreationForm
# Create your views here.


class HomeView(View):
    template_name = "home.html"
    not_logged_in = reverse_lazy("user:login.html")
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts/login")
        return render(request,self.template_name)
        
class EventView(HomeView):
    template_name = "event.html"
    

class AllPostsView(View):
    template_name = "posts.html"
    queryset=UserPost.objects.all()
    success_template = "posts.html"
    failure_template = "home.html"
    
    def get_queryset(self,request):
        return self.queryset.order_by("-created_at")

    def get(self,request,*args,**kwargs):
        userpost_form = UserPostCreationForm()
        context = {"userpost_list":self.get_queryset(request),
                   "userpost_form":userpost_form}
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = UserPostCreationForm(request.POST,request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            userpost = form.save(commit=False)
            userpost.user = request.user
            userpost.save()
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
        


