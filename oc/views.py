from django.shortcuts import render, get_object_or_404, redirect
from .models import db
from .forms import PostForm

# Create your views here.
def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.out = "sample output"
			post.save()
			return render(request, 'oc/post_detail.html', {'post':post})
		else:
			form = PostForm()
		return render(request, 'oc/post_new.html', {'form':form})

def post_detail(request, pk):
	post = get_object_or_404(db, pk=pk)
	return render(request, 'oc/post_detail.html', {'post':post})


