from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .analysis import detect_labels_local_file

# Create your views here.

def home(request):
  try:
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filesize = fs.size(filename)
        print(filesize)
        if filesize > 5000000:
          res = "Too Big"
          return render(request, 'home.html', {'res': res})
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        res = detect_labels_local_file('/Users/hongdotcom/Desktop/Sites/django-imgsearch/imgsearch/' + uploaded_file_url)
        print(res)
        if res != "No Match":
          page = res+'.html'
          return render(request, page, {
              'res': res,
              'uploaded_file_url': uploaded_file_url,
          })
        if res:
          return render(request, 'home.html', {'res': res, 'uploaded_file_url': uploaded_file_url,})
  except: 
    res = "Unknown"
    return render(request, 'home.html', {'res': res})
    
  return render(request, 'home.html')

