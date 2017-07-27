# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import LineItem

import json

class LineItemCreateTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='joe')

    def test_create(self):

        data = {
            "id": 1,
            "object_ids": ["apointment:123", "user:456"],
            "fields": ["name", "description", "price"],
            "values": [
                ["foo", "bar", "1000"],
                ["baz", "bus", "3000"]
            ],
            "owner": 1
        }

        headers = {
            'HTTP_X_ANONYMOUS_CONSUMER': 'false',
            'HTTP_X_AUTHENTICATED_USERID': '1',
            'HTTP_X_CONSUMER_USERNAME': 'jimminy-the-cricket'
        }

        url = reverse('lineitem-list')
        result = self.client.post(url, json.dumps(data), content_type='application/json', **headers)
        assert result.status_code == 201, \
            'Expected 201 CREATED. Got: {}: {}'.format(result.status_code, result.content)

