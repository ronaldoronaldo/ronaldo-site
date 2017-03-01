from __future__ import unicode_literals

from django.db import models


class Galeria(models.Model):
    nome = models.TextField(verbose_name="nome de galeria")

    def __unicode__(self):
        return self.nome

class Imagem(models.Model):
    imagem = models.ImageField(verbose_name="Imagem", upload_to='breno')
    galeria = models.ForeignKey(Galeria, verbose_name="galeria")
