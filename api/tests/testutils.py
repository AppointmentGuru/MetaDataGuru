from ..models import LineItem, JsonBlob
from django.contrib.auth import get_user_model

from faker import Factory
FAKE = Factory.create()

def create_user(username=None, password='testtest'):
    if username is None: username = FAKE.user_name()
    return get_user_model().objects.create_user(username=username, password=password)

def create_users(count=1):
    for x in range(0, count):
        get_user_model().objects.create(id=x, username=x, password='testtest')

def get_random_user():
    return get_user_model().objects.all().order_by('?').first()

def create_line_item(owners=[], object_ids=[], **kwargs):

    data = {
        "owners": owners,
        "object_ids": object_ids,
        "fields": ["name", "description", "price"],
        "values": [
            ["foo", "bar", FAKE.random_number()],
            ["baz", "bus", FAKE.random_number()]
        ],
    }
    data.update(**kwargs)
    return LineItem.objects.create(**data)

def create_jsonblob(owners=[], objects=[]):

    return JsonBlob.objects.create(
        name=FAKE.name(),
        owners=owners,
        object_ids=objects,
        data={"foo": "bar"} #FAKE.pydict()
    )

def get_proxy_headers(user_id, consumer='joesoap', headers = {}):

    headers['HTTP_X_CONSUMER_USERNAME'] = consumer

    if user_id is None:
        headers['HTTP_X_ANONYMOUS_CONSUMER'] = 'true'
    else:
        headers['HTTP_X_AUTHENTICATED_USERID'] = str(user_id)
    return headers