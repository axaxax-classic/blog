from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.utils import timezone

def post_list(request):
    posts = models.Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    context = {'posts': posts,
               'user': request.user}
    return render(request, 'app/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, "app/post_detail.html", {"post": post})


def post_add(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponse(status=401)
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', post_id=post.id)
    else:
        form = forms.PostForm()
    return render(request, 'app/post_add.html', {'form': form})