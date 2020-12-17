from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView
from .models import Post, Category
from .forms import PostForm ,EditForm
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect
# Create your views here.

#def home(request):
#   return render(request , 'home.html',{})

def LikeView(request , pk):
    post = get_object_or_404(Post , id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("article-detail", args = [str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self , *args , **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView , self).get_context_data(*args , **kwargs)
        context["cat_menu"] = cat_menu       
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self , *args , **kwargs):
        cat_menu = Category.objects.all()
        context = super( ArticleDetailView, self).get_context_data(*args , **kwargs)
        stuff = get_object_or_404(Post , id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
       
        return context

class AddPostView(CreateView):
    model = Category
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def CategoryView(request , cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request , 'categories.html' , {'cats':cats.title() , 'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request , 'category_list.html' , {'cat_menu_list':cat_menu_list})