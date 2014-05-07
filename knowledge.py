import json


def create_knowledge_type(kind, attrs):
    k = type(kind, (Knowledge,), attrs)
    return k


class KnowledgePool(object):

    def __init__(self, kind):
        self._type = kind.__name__
        self._pool = []

    def dump(self):
        obj = {self._type: [x._data for x in self._pool]}
        return json.dumps(obj, indent=4)

    def add(self, knowledge):
        self._pool.append(knowledge)


class Knowledge(object):

    def __init__(self):
        self._data = {}

    def dump(self):
        return json.dumps(self._data)

    def load(self, s):
        self._data = json.loads(s)
