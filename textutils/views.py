# # I have created his file - sejal
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse(" ")
# def About(request):
#     return HttpResponse(" ")

# # def ex1(request):
# #     s = '''<h1>Navigation Bar<br></h2>
# #     <h2><a href="https://www.instagram.com/">Instagram Login Page</h2></a><br>
     
# #     <h2><a href="https://www.amazon.com/">Amazon Page</h2></a><br>
# #     <h2><a href="https://www.google.com/">Google Logo</h2></a><br>
# #     <h2><a href="https://www.snapchat.com/">Snapchat</h2></a><br>
# #       <h2><a href="https://www.linkedin.com/feed/">My Linkdin Profile</h2></a><br>
# #     '''
#     # return HttpResponse(s)

# from django.shortcuts import render
# def index(request): 
#     return render(request,'index.html')
#     # return HttpResponse((sites)) 

# def analyze(request):
# # Get the text
#     djtext=(request.POST.get('text','default'))
#     print(djtext)

# # check the all checkboxs
#     removepunc =(request.POST.get('removepunc','off'))
#     fullcaps =(request.POST.get('fullcaps','off')) 
#     Newlineremover =(request.POST.get('Newlineremover','off'))
#     Extraspaceremover =(request.POST.get('Extraspaceremover','off'))
#     Charactercounter =(request.POST.get('Charactercounter','off'))   
# # check which check box is on 
#     if removepunc=="on":
#         punctuations = '''!{}()[]-;:'"\,<>./?@#$%^&*_'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char

#         params = {'purpose':'Removed punctuation','Analyzed_text':analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
    
#     if(fullcaps=="on"):
#         analyzed=""
#         for char in djtext:
#             analyzed=analyzed+char.upper()
#         params = {'purpose':'Changed to upper case','Analyzed_text':analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)

#     if(Newlineremover=="on"):
#         analyzed=""
#         for char in djtext:
#             if char!="\n":
#                 analyzed=analyzed+char
#         params = {'purpose':'Removerd Newlineremove','Analyzed_text':analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
    
#     if(Extraspaceremover=="on"):
#         analyzed=""
#         for index, char in enumerate(djtext):
#             if not (djtext[index]==" " and djtext[index+1]==" "):
#                 analyzed=analyzed+char
#         params = {'purpose':'Removerd Extraspace','Analyzed_text':analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
    
#     if(Charactercounter=="on"):
#         analyzed=('No. of characters in the text:'+str(len(djtext)))
#         params = {'purpose':'I want a Charactercount','Analyzed_text':analyzed}
#         print(params)

#         return render(request, 'analyze.html', params)

#     # if(removepunc!="on" and Newlineremover!="on" and fullcaps!="on" and Extraspaceremover!="on" and Charactercounter!="on"):    
#     #     return HttpResponse('Error')

# # def capitalizefirst(request):
# #     return HttpResponse("capitalizefirst <a href='/'>back</a>")

# # def Newlineremove(request):
# #     return HttpResponse("Newline remove <a href='/'>back</a>")

# # def Spaceremove(request):
# #     return HttpResponse("Space remove <a href='/'>back</a>")

# # def Charcount(request):
# #     return HttpResponse("Charcount <a href='/'>back</a>")

# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char   
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("Error")
