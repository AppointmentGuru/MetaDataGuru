# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import LineItem, Note, Document, ImageDocument

admin.site.register(LineItem)
admin.site.register(Note)
admin.site.register(Document)
admin.site.register(ImageDocument)
