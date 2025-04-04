from django.shortcuts import render, get_object_or_404, redirect
from .models import Feligres
from .forms import FeligresForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # ✅ Esto está bien

@login_required
def lista_hermanos(request):
    query = request.GET.get('q', '')
    if query:
        hermanos = Feligres.objects.filter(
            Q(nombres__icontains=query) |
            Q(apellidos__icontains=query) |
            Q(documento_identidad__icontains=query)
        )
    else:
        hermanos = Feligres.objects.all()

    return render(request, 'feligreses/lista_hermanos.html', {'hermanos': hermanos})

@login_required
def detalle_hermano(request, pk):
    hermano = get_object_or_404(Feligres, pk=pk)
    return render(request, 'feligreses/detalle.html', {'hermano': hermano})

@login_required
def agregar_hermano(request):
    if request.method == 'POST':
        print("✅ Se envió un POST")
        print("📄 Datos enviados:")
        print(request.POST)
        print(request.FILES)

        form = FeligresForm(request.POST, request.FILES)
        if form.is_valid():
            print("✅ Formulario válido. Guardando...")
            form.save()
            return redirect('lista_hermanos')
        else:
            print("❌ Formulario inválido")
            print(form.errors)
    else:
        form = FeligresForm()

    return render(request, 'feligreses/agregar.html', {'form': form})

@login_required
def editar_hermano(request, pk):
    hermano = get_object_or_404(Feligres, pk=pk)

    if request.method == 'POST':
        form = FeligresForm(request.POST, request.FILES, instance=hermano)
        if form.is_valid():
            form.save()
            return redirect('lista_hermanos')
    else:
        form = FeligresForm(instance=hermano)

    return render(request, 'feligreses/editar.html', {'form': form})

@login_required
def eliminar_hermano(request, pk):
    hermano = get_object_or_404(Feligres, pk=pk)
    if request.method == 'POST':
        hermano.delete()
        return redirect('lista_hermanos')
    return render(request, 'feligreses/eliminar.html', {'hermano': hermano})

