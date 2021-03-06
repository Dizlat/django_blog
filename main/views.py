from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import Category, Post


# def index_page(request):
#     categories = Category.objects.all()
#     return render(request,
#                   'main/index.html',
#                   {'categories': categories})
#TODO: Переписать при помощи классов ++

# class IndexPageView(View):
#     def get(self, request):
#         categories = Category.objects.all()
#         return render(request,
#                       'main/index.html',
#                       {'categories': categories})

class IndexPageView(View):
    # queryset = Category.objects.all()
    # template_name = 'main/index.html'
    # context_object_name = 'categories'

    def get(self, request):
        # categories = Category.objects.all()
        posts = Post.objects.all()
        return render(request, 'main/index.html', locals())


class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category_id=category_id)


class CatDetailView(DetailView):
    queryset = Category.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'category'


class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'
    context_object_name = 'post'


class CreateNewPostView(LoginRequiredMixin, CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    form_class = CreatePostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('post-details', args=(self.object.id, ))


class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_authenticated and self.request.user == post.author


class EditPostView(IsAuthorMixin, UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/edit_post.html'
    form_class = UpdatePostForm

    def get_success_url(self):
        return reverse('post-details', args=(self.object.id, ))


class DeletePostView(IsAuthorMixin, DeleteView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'

    def get_success_url(self):
        return reverse('index-page')

class SearchResultView(View):
    pass


#TODO: Список постов по категориям++++
#TODO: Переход по страницам++++
#TODO: Регистрация, активация, логин, логаут++++
#TODO: смена и востановления пароля++
#TODO: создание, редактирование и удаление постов+
#TODO: больше постов++++
#TODO: HTML - письмо++++
#TODO: Фильтрация, поиск, сортировка
#TODO: Пагинация
#TODO: Переиспользование шаблонов
#TODO: Проверка прав
#TODO: Избранное
#TODO: Дизайн
#TODO: Описание (README)