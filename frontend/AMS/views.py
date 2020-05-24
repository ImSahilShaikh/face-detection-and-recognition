from django.shortcuts import render
from AMS.forms import StudentForm
from AMS.models import Student
from django.http import HttpResponse
# Create your views here.

def stud(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect()
			except:
				pass
	else:
		form = StudentForm()
	return render(request,"index.html",{'form':form})


def adminLogin(request):
	if request.method == 'POST':
		user = request.POST['username']
		passw = request.POST['password']
		if(user == 'admin' and passw=='123'):
			students = Student.objects.all()
			return render(request,"index.html",{'students':students})
		else:
			return render(request,"login.html")	

def login(request):
	return render(request,"login.html")


						