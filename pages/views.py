from django.shortcuts import render

def mainpages(request):
    return  render(request, 'pages/mainpage.html')

def company(requset):
    return render(requset, 'pages/company_info.html')