# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class LineItem(models.Model):

    # the object to which this lineitem is attached
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=255, db_index=True, verbose_name='The remote object to which this field belongs')

    fields = models.ArrayField(models.CharField)
    values = models.ArrayField(models.ArrayField(models.CharField))

class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    object_ids = models.ArrayField(models.CharField, db_index=True)

    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True))

    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

class Document(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)

    file = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

class ImageDocument(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    file = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

class NoteDocumentRelationship(models.Model):

    note = models.ForeignKey(Note, blank=True, null=True))
    image = models.ForeignKey(ImageDocument, blank=True, null=True))
    document = models.ForeignKey(Document, blank=True, null=True))

