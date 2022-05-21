from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def analyze(request):
    Analysing = request.POST.get('text', 'default')
    #return text which we input in textarea, if we only navigate to Atext it will return default value
    Removepunctuation = request.POST.get('Removepunc', 'off')  
    Capitalise = request.POST.get('Capitalize', 'off')
    Char_count = request.POST.get('Charcount', 'off')
    
    analyzed = ""
    if Removepunctuation == "on" and Capitalise == "on" and Char_count == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        count = 0
        for char in Analysing:
            count+=1
            if char not in punctuations:
                analyzed = analyzed + char.upper()  
        params = {'sentence': analyzed, 'characters': count}
        return render(request, 'text.html', params)
    elif Removepunctuation == "on" and Capitalise == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in Analysing:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
            params = {'sentence': analyzed}
        return render(request, 'text.html', params)
    elif Capitalise == "on" and Char_count == "on":
        count = 0
        for char in Analysing:
            analyzed = char + analyzed
            count+=1
            params = {"sentence": analyzed, "characters": count}
        return render(request,"text.html", params) 
    elif Removepunctuation == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in Analysing:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"sentence": analyzed}
        return render(request, "text.html", params)
    elif Char_count == "on":
        count = 0
        char_len = len(Analysing)
        for i in range(char_len):
            count+=1
        params = {'sentence': count} 
        return render(request, 'text.html', params)
    else:
        return HttpResponse('Error')