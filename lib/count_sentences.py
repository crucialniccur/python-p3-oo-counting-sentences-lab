#!/usr/bin/env python3

# count_sentences.py

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Replace all end punctuation with "."
        text = self.value.replace("!", ".").replace("?", ".")
        # Split by "."
        segments = text.split(".")
        # Strip and filter out empty strings
        sentences = [s.strip() for s in segments if s.strip()]
        return len(sentences)
