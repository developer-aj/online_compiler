from django.shortcuts import render, get_object_or_404, redirect
from .models import db
from .forms import PostForm
import os

# Create your views here.
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			#calling compiler
			compiler(post.language, post.code, post.inp)
			post.out = open('./env/out', 'r').read()
			post.save()
			return render(request, 'oc/post_detail.html', {'post':post})
	else:
		form = PostForm()
	return render(request, 'oc/post_new.html', {'form':form})

def post_detail(request, pk):
	post = get_object_or_404(db, pk=pk)
	return render(request, 'oc/post_detail.html', {'post':post})

def compiler(lang, code, inp):
	proc = ""
	exec_command = " < ./env/in &> ./env/out"
	time = 0
	kill_command = " kill $! &> ./env/out"
	open('./env/in', 'w+').write(inp)
	if lang=='C':
		open('./env/code.c', 'w+').write(code)
		os.system("gcc ./env/code.c -o a.out &> ./env/out")
		time = '5'
		proc = "./env/a.out"

	elif lang=='C++':
		open('./env/code.cpp', 'w+').write(code)
		os.system("gcc ./env/code.cpp -o a.out &> ./env/out")
		time = '5'
		proc = "./env/a.out"
		
	elif lang=='Python':
		open('./env/code.py', 'w+').write(code)
		time = '10'
		proc = "python ./env/code.py"

	else :
		open('./env/out', 'w+').write('under development')
		return
	os.system(proc + exec_command + " & sleep " + time + kill_command)
		
