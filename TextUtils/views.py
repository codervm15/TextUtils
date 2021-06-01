from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    #Check box values check
    checkbutton1 = request.POST.get('checkbutton1', 'off')
    checkbutton2 = request.POST.get('checkbutton2', 'off')
    checkbuton3 = request.POST.get('checkbutton3','off')
    checkbuton4 = request.POST.get('checkbutton4', 'off')
    checkbuton5 = request.POST.get('checkbutton5', 'off')

    #Required functionalities for functions
    punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    count=0


    #Checking which checkbox is on and performning actions

    #First function removes the punctuation from the text
    if(checkbutton1=='on'):
        analyzedtext=""
        for i in djtext:
            if i not in punctuations:
                analyzedtext=analyzedtext+i
        context = {"purpose": "All punctuations removed","data": analyzedtext}
        djtext=analyzedtext

    #second function count the nubers of characters in text
    if(checkbutton2=='on'):
        analyzedtext=""
        for i in djtext:
            count = count + 1
        context = { "purpose": "Number of characters in text",'data': count}
        djtext=analyzedtext

    #Third function capitalize the whole text
    if(checkbuton3=='on'):
        analyzedtext=""
        for i in djtext:
            analyzedtext=analyzedtext+i.upper()
        context={"purpose": "Text is Capitalized" ,"data": analyzedtext}
        djtext=analyzedtext

    #Fourth function removes the new line
    if (checkbuton4 == 'on'):
        analyzedtext=""
        for i in djtext:
            if i !="\n" and i !="\r":
                analyzedtext=analyzedtext+i
        context={"purpose": "Remove New Line" ,"data": analyzedtext}
        djtext=analyzedtext

    #Fifth function remove extra space from line
    if (checkbuton5 == 'on'):
        analyzedtext=""
        for index,i in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzedtext=analyzedtext+i
        context={"purpose": "Remove extra space" ,"data": analyzedtext}
        djtext=analyzedtext

    if(checkbutton1!='on' and checkbutton2!='on' and checkbuton3!='on' and checkbuton4!='on' and checkbuton5!='on'):
        context={"purpose": "Error", "data":"Try Again"}
        return render(request,'output.html',context)

    return render(request,'output.html',context)





