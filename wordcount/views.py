from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def counter(request):
    words = request.GET['words']
    wordslist = words.split()
    wordsdict = {}
    for word in wordslist:
        if word in wordsdict:
            wordsdict[word] += 1    
        else:
            wordsdict[word] = 1
    
    sortedwords = sorted(wordsdict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'counter.html',   {'words':sortedwords})

def about(request):
    return render(request,'about.html')