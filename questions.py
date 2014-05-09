import json


class Question(object):

    def __init__(self):
        self._question = {
            'kind': self.__class__.__name__,
            'stem': '',
        }

    def __str__(self):
        return self._question['stem']

    def dump(self):
        return json.dumps(self._question)

    def load(self, s):
        self._question = json.loads(s)


class MultipleChoice(Question):

    def __init__(self):
        super(MultipleChoice, self).__init__()
        self._question['keys'] = []
        self._question['distractors'] = []
