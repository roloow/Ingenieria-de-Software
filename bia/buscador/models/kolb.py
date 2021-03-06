# -*- coding: utf-8 -*-

from django.db import models

class KolbModel(models.Model):
    ASIMILADOR = 1
    DIVERGENTE = 2
    ACOMODADOR = 3
    CONVERGENTE = 4

    nombre = models.CharField(max_length=15)
    description = models.CharField(max_length=100, blank=True, null=True)
    tags = models.ManyToManyField('TagModel',
                                   through='KolbTagModel',
                                   through_fields=('kolb', 'tag'),
                                   related_name='kolb_profiles')

    def __unicode__(self):
        return self.nombre
