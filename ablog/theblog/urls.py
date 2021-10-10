
from django.urls import path
from . import views
from .views import HomeView,Detail_list,AddPostView,UpdatePostView,DeletePost,AddCategoryView,category_view,categoryListView,LikeView

urlpatterns = [

    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',Detail_list.as_view(),name="article-detail"),
    path('add_posts',AddPostView.as_view(),name="add_post"),
    path('add_category',AddCategoryView.as_view(),name="add_category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/delete/<int:pk>',DeletePost.as_view(),name="delete_post"),
    path('category/<str:cats>',category_view,name='categories'),
    path('category_list',categoryListView,name='category_list'),
    path('like/<int:pk>',LikeView,name='like_post'),

]
