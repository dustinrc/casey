import json


def create_knowledge_type(kind, attrs):
    k = type(kind, (Knowledge,), attrs)
    return k


class Knowledge(object):

    def __init__(self):
        self._data = {}

    def dump(self):
        return json.dumps(self._data)

    def load(self, s):
        self._data = json.loads(s)
