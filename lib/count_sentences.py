#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Value must be a string")
        self._value = new_value
    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        
        text = re.sub(r'[.!?]+', '.', self._value)
       
        sentences = [s for s in text.split('.') if s.strip()]
        return len(sentences)

