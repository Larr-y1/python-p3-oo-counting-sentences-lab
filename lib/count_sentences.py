#!/usr/bin/env python3


class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
            self.value = ''
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split by sentence-ending punctuation
        import re
        sentences = re.split(r'[.!?]', self.value)
        # Remove empty strings after split and strip spaces
        filtered = [s.strip() for s in sentences if s.strip()]
        return len(filtered)


msg = MyString("Hello! How are you? I'm fine.")
print(msg.is_exclamation())  
print(msg.is_question())     
print(msg.is_sentence())     
print(msg.count_sentences())
