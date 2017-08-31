# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import LineItem, JsonBlob

class LineItemModelTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='joe')

    def test_create(self):

        fields = ['name', 'description', 'price']
        line_items = [
            ['foo', 'bar', '1000'],
            ['baz', 'bus', '3000']
        ]

        li = LineItem.objects.create(owners=[self.user], fields=fields, values=line_items)

class JsonBlobTestCase(TestCase):

    def test_create_blob(self):

        obj = JsonBlob.objects.create(
            name='test',
            owners=[1,2,3],
            object_ids=[4,5,6],
            data={"foo": "bar"}
        )
        assert obj.id is not None
