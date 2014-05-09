import json


def create_knowledge_kind(kind, attrs):
    k = type(str(kind), (Knowledge,), attrs)
    return k


class KnowledgePool(object):

    def __init__(self, kind=None):
        try:
            self._kind = kind.__name__
        except AttributeError:
            self._kind = kind
        self._pool = []

    def dump(self):
        obj = {
            'kind': self._kind,
            'pool': [x._data for x in self._pool],
        }
        return json.dumps(obj, indent=4)

    def load(self, s):
        # TODO: make this method not so ugly
        obj = json.loads(s)
        self._kind = obj['kind']
        self._pool = []
        for x in obj['pool']:
            k = create_knowledge_kind(self._kind, {})
            k._data = x
            self.add(k)

    def add(self, knowledge):
        self._pool.append(knowledge)


class Knowledge(object):

    def __init__(self):
        self._data = {}

    def dump(self):
        return json.dumps(self._data)

    def load(self, s):
        self._data = json.loads(s)
