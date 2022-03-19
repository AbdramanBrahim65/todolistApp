from django.shortcuts import render,redirect

from .models import TacheModel

def creation_affichage(request):
    if request.method == "POST":
        tache = request.POST['tache']
        form = TacheModel(tache=tache)
        form.save()
        return redirect('/')
    form = TacheModel.objects.all()
    context ={
        'form':form,
    }
    return render(request,'todo.html',context)
def detail(request,pk):
    form =TacheModel.objects.get(id=pk)
    context ={
        'form':form,
    }
    return render(request,'details.html',context)
def supprimer_views(request,pk):
    form = TacheModel.objects.get(id=pk)
    
    form.delete()
    return redirect('/')
    context={
        'form':form,
    }
    return render(request,'todo.html',context)
