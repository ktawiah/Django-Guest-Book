from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.views.decorators.csrf import csrf_protect


def index(request):
    comments = Comment.objects.order_by("-date_added")
    context = {"comments": comments}
    return render(request, "guest_book_app/index.html", context)


def sign(request):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CommentForm()
    return render(request, "guest_book_app/sign.html", context={"form": form})
