from django.http import request
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from .models import Post,Category
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post , id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
        liked = True
    else:
        post.likes.add(request.user)
        liked = False
    return HttpResponseRedirect(reverse('article-detail',args = [str(pk)] )) 

def category_view(request, cats):
    cats = cats.replace('-',' ')
    categories_posts = Post.objects.filter(category=cats)
    cat_menu = Category.objects.all()
    return render(request,'categories.html',{'category': cats,'categories_posts':categories_posts,'cat_menu':cat_menu,})

def categoryListView(request):
    cat_menu = Category.objects.all()    # iska url add karne 
    return render(request,'category_list.html',{'cat_menu':cat_menu, })

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']
    def get_context_data(self, *args ,**kwargs) :
        cat_menu = Category.objects.all()   
        context = super(HomeView, self).get_context_data(*args ,**kwargs)
        context['cat_menu'] = cat_menu
        return context
        
class Detail_list(DetailView):
    model = Post
    template_name = 'article-details.html'
    def get_context_data(self, *args ,**kwargs) :
        cat_menu = Category.objects.all()   
        context = super(Detail_list, self).get_context_data(*args ,**kwargs)
        stuff = get_object_or_404(Post,id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id):
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
    # ye apana apne drop down ke liye daale hai 
    def get_context_data(self, *args ,**kwargs) :
        cat_menu = Category.objects.all()   
        context = super(AddPostView, self).get_context_data(*args ,**kwargs)
        # stuff = get_object_or_404(Post,id = self.kwargs['pk'])
        # total_likes = stuff.total_likes()
        context['cat_menu'] = cat_menu
        # context["total_likes"] = total_likes
        return context
    
    # fields = '__all__'  
    #fields = ['title','body','author'] can't use this with form_class so create new form class in forms.py

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    #fields = ('title','title_tag','body')

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    
    def get_context_data(self, *args ,**kwargs) :
        cat_menu = Category.objects.all()   
        context = super(AddCategoryView, self).get_context_data(*args ,**kwargs)
        context['cat_menu'] = cat_menu
        return context