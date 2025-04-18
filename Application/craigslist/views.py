from django.shortcuts import render,redirect
from requests.compat import quote_plus
from .models import Search
from bs4 import BeautifulSoup
import requests
from .models import userreg
# Create your views here.


BASE_CRAIGSLIST_URL='https://delhi.craigslist.org/search/bbb?query={}&lang=es&cc=es'
BASE_IMAGE_URL='https://images.craigslist.org/{}_300x300.jpg'


def index(request):
	return render(request,'index.html')

def home(request):
	return render(request,'base.html')

def register(request):
    if request.method=="POST":
       username=request.POST.get('username')
       email=request.POST.get('email')
       password=request.POST.get('password')
       userreg(username=username,email=email,password=password).save()
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def log(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        stud=userreg.objects.filter(username=username,password=password)
        if stud:
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request,'register.html')

def new_search(request):
	search=request.POST.get('search')
	Search.objects.create(search=search)
	final_url=BASE_CRAIGSLIST_URL.format(quote_plus(search))
	response=requests.get(final_url)
	data=response.text

	soup=BeautifulSoup(data,features='html.parser')
	post_listings=soup.find_all('li',{'class':'result-row'})

	final_postings=[]

	for post in post_listings:
		post_title=post.find(class_='result-title hdrlnk').text
		post_url=post.find('a').get('href')
		
		if post.find(class_='result-price'):
			post_price=post.find(class_='result-price').text
		else:
			post_price='N/A'

		if post.find(class_='result-image').get('data-ids'):
			post_image_id=post.find(class_='result-image').get('data-ids').split(':')[1]
			post_image_url=BASE_IMAGE_URL.format(post_image_id)
		else:
			post_image_url='https://craigslist.org/images/peace.jpg'

		final_postings.append((post_title,post_url,post_price,post_image_url))

	stuff_for_frontend={
		'search':search,
		'final_postings':final_postings,
	}
	
	return render(request,'craigslist/new_search.html',stuff_for_frontend)








	