# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import LineItem
from .testutils import create_line_item, create_users, get_proxy_headers

import json

class LineItemCreateTestCase(TestCase):

    def setUp(self):
        object_ids = [
            [ 'appointment:1' ],
            [ 'appointment:2' ],
            [ 'appointment:2', 'appointment:3' ],
            [ 'appointment:3' ],
            [ 'appointment:3' ],
            [ 'appointment:1', 'appointment:2', 'appointment:3', 'appointment:4' ],
        ]

        for li in object_ids:
            create_line_item(owners=['1'], object_ids=li)
        create_line_item(owners=['2'])

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

    def test_only_returns_results_for_logged_in_user(self):

        users_expected_count = [
            (1, 6),
            (2, 1)
        ]
        for user_id, expected_count in users_expected_count:

            url = reverse('lineitem-list')
            result = self.client.get(url, **get_proxy_headers(user_id))
            assert len(result.json()) == expected_count

            for li in result.json():
                assert str(user_id) in li.get('owners')


    def test_filter_find_line_items_for_appointments(self):

        args_expected_count = [
            ('1', 2),
            ('3', 4),
            ('5', 0),
            ('1,2', 4),
            ('3,4,5', 4)
        ]

        for args, expected_count in args_expected_count:
            url = "{}?objects_appointment={}".format(reverse('lineitem-list'), args)
            result = self.client.get(url, **get_proxy_headers(1))
            actual_count = len(result.json())
            assert actual_count == expected_count, \
                'Expected {}. got: {}. Result: {}'.format(expected_count, actual_count, result.json())

