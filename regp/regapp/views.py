from django.shortcuts import render
from .forms import userform
from .models import usermodel
# Create your views here.

def register(req):
	registered=False
	usern="user"
	if req.method=="POST":
		user_form=userform(data=req.POST)
		if user_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			#profile = userinfo_form.save(commit=False)
			#profile.user=user
			#if 'ppic' in req.FILES:
			#	profile.ppic = req.FILES['ppic']
			#	profile.save()
			registered = True
			usern=req.POST['username']
		else:
			print(user_form.errors)
	else:
		user_form = userform()
		#userinfo_form = userinfoform()
	return render(req,"regapp/register.html",{'user_form':user_form,'registered':registered,'user':usern})
            
             
        
        # Was not an HTTP post so we just render the forms as blank.
        
    
                
		    
            
      
            
        

    

def index(req):
	toll=1320
	return render(req,"regapp/index.html",{'toll':toll})
def symp(req):
	return render(req,"regapp/symptoms.html")
def shop(req):
	return render(req,"regapp/shop.html")
def res(req):
	return render(req,"regapp/research.html")