from django.shortcuts import render
from ronaldosite import models


def home(request):
    galerias = models.Galeria.objects.all()
    gal_list = []
    for galeria in galerias:
        img_list = []
        imagens = models.Imagem.objects.filter(galeria=galeria)
        for imagem in imagens:
            img_list.append(imagem.imagem.url)
        galeriadata = {'nome': galeria.nome,
                       'imagens': img_list}
        gal_list.append(galeriadata)
    data = {'galerias': gal_list}
    return render(request, 'home.html', data)

