from django.shortcuts import render, get_object_or_404, redirect
from .models import Feligres
from .forms import FeligresForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_feligreses(request):
    feligreses = Feligres.objects.all()
    return render(request, 'feligreses/lista.html', {'feligreses': feligreses})

@login_required
def detalle_feligres(request, feligres_id):
    feligres = get_object_or_404(Feligres, id=feligres_id)
    return render(request, 'feligreses/detalle.html', {'feligres': feligres})

@login_required
def agregar_feligres(request):
    if request.method == "POST":
        form = FeligresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_feligreses')
    else:
        form = FeligresForm()
    return render(request, 'feligreses/agregar.html', {'form': form})

@login_required
def editar_feligres(request, feligres_id):
    feligres = get_object_or_404(Feligres, id=feligres_id)
    if request.method == "POST":
        form = FeligresForm(request.POST, request.FILES, instance=feligres)
        if form.is_valid():
            form.save()
            return redirect('lista_feligreses')
    else:
        form = FeligresForm(instance=feligres)
    return render(request, 'feligreses/editar.html', {'form': form, 'feligres': feligres})

@login_required
def eliminar_feligres(request, feligres_id):
    feligres = get_object_or_404(Feligres, id=feligres_id)
    if request.method == "POST":
        feligres.delete()
        return redirect('lista_feligreses')
    return render(request, 'feligreses/eliminar.html', {'feligres': feligres})
