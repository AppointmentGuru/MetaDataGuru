# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class LineItem(models.Model):

    # the object to which this lineitem is attached
    owners = ArrayField(models.CharField(max_length=36), default=[])
    object_ids = ArrayField(models.CharField(max_length=100), default=[])

    fields = ArrayField(models.CharField(max_length=100))
    values = ArrayField(ArrayField(models.CharField(max_length=100)))

class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    object_ids = ArrayField(models.CharField(max_length=100), default=[], blank=True, null=True)

    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

class Document(models.Model):

    owners = ArrayField(models.CharField(max_length=36), default=[])
    object_ids = ArrayField(models.CharField(max_length=100), default=[], blank=True, null=True)
    note = models.ForeignKey(Note, blank=True, null=True)


    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)

    file = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

class ImageDocument(models.Model):
    owners = ArrayField(models.CharField(max_length=36), default=[])
    object_ids = ArrayField(models.CharField(max_length=100), default=[], blank=True, null=True)
    note = models.ForeignKey(Note, blank=True, null=True)

    name = models.CharField(max_length=50)

    file = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

"""
class MetaDataItem(models.Model):

    note = models.ForeignKey(Note, blank=True, null=True)
    image = models.ForeignKey(ImageDocument, blank=True, null=True)
    document = models.ForeignKey(Document, blank=True, null=True)
"""