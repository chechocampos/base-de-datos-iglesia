from django.shortcuts import render, redirect, get_object_or_404
from .models import Feligres, Iglesia
from .forms import FeligresForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_iglesias(request):
    iglesias = Iglesia.objects.all()
    return render(request, 'feligreses/lista_iglesias.html', {'iglesias': iglesias})


@login_required
def lista_feligreses(request, iglesia_id):
    iglesia = get_object_or_404(Iglesia, id=iglesia_id)
    feligreses = Feligres.objects.filter(iglesia=iglesia)

    query = request.GET.get('q')
    if query:
        feligreses = feligreses.filter(nombre__icontains=query)

    return render(request, 'feligreses/lista.html', {
        'feligreses': feligreses,
        'iglesia': iglesia
    })


@login_required
def agregar_feligres(request, iglesia_id):
    iglesia = get_object_or_404(Iglesia, id=iglesia_id)

    if request.method == 'POST':
        form = FeligresForm(request.POST)
        if form.is_valid():
            feligres = form.save(commit=False)
            feligres.iglesia = iglesia
            feligres.save()
            return redirect('lista_feligreses', iglesia_id=iglesia.id)
    else:
        form = FeligresForm()

    return render(request, 'feligreses/agregar.html', {'form': form, 'iglesia': iglesia})


@login_required
def editar_feligres(request, iglesia_id, feligres_id):
    iglesia = get_object_or_404(Iglesia, id=iglesia_id)
    feligres = get_object_or_404(Feligres, id=feligres_id, iglesia=iglesia)

    if request.method == 'POST':
        form = FeligresForm(request.POST, instance=feligres)
        if form.is_valid():
            form.save()
            return redirect('lista_feligreses', iglesia_id=iglesia.id)
    else:
        form = FeligresForm(instance=feligres)

    return render(request, 'feligreses/editar.html', {
        'form': form,
        'iglesia': iglesia,
        'feligres': feligres
    })


@login_required
def eliminar_feligres(request, iglesia_id, feligres_id):
    iglesia = get_object_or_404(Iglesia, id=iglesia_id)
    feligres = get_object_or_404(Feligres, id=feligres_id, iglesia=iglesia)

    if request.method == 'POST':
        feligres.delete()
        return redirect('lista_feligreses', iglesia_id=iglesia.id)

    return render(request, 'feligreses/eliminar.html', {
        'feligres': feligres,
        'iglesia': iglesia
    })

