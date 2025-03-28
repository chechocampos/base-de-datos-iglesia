from django.shortcuts import render, redirect, get_object_or_404
from .models import Feligres
from .forms import FeligresForm
from django.contrib.auth.decorators import login_required

# Vista principal: lista de iglesias protegida con login
@login_required
def lista_iglesias(request):
    iglesias = Feligres.objects.all()
    return render(request, 'feligreses/lista_iglesias.html', {'iglesias': iglesias})

# Añadir feligrés
@login_required
def agregar_feligres(request):
    if request.method == 'POST':
        form = FeligresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_iglesias')
    else:
        form = FeligresForm()
    return render(request, 'feligreses/agregar.html', {'form': form})

# Editar feligrés
@login_required
def editar_feligres(request, pk):
    feligres = get_object_or_404(Feligres, pk=pk)
    if request.method == 'POST':
        form = FeligresForm(request.POST, instance=feligres)
        if form.is_valid():
            form.save()
            return redirect('lista_iglesias')
    else:
        form = FeligresForm(instance=feligres)
    return render(request, 'feligreses/editar.html', {'form': form})

# Eliminar feligrés
@login_required
def eliminar_feligres(request, pk):
    feligres = get_object_or_404(Feligres, pk=pk)
    if request.method == 'POST':
        feligres.delete()
        return redirect('lista_iglesias')
    return render(request, 'feligreses/eliminar.html', {'feligres': feligres})
