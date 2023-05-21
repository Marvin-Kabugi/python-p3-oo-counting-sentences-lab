#!/usr/bin/env python3

class MyString:
  def __init__(self, value="") -> None:
    self.set_value(value)
  
  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    if self.get_value().endswith("."):
      return True
    return False
  
  def is_question(self):
    if self.get_value().endswith("?"):
      return True
    return False
  
  def is_exclamation(self):
    if self.get_value().endswith("!"):
      return True
    return False
  
  def count_sentences(self):
    if len(self.value) == 0:
      return 0
    replaced_sentence = self.value.replace("!", ".")
    replaced_sentence = replaced_sentence.replace("?", ".")
    sentences = replaced_sentence.split(".")
    filtered_sentences = [sentence for sentence in sentences if len(sentence) > 0]
    return len(filtered_sentences)
  
  value = property(get_value, set_value)


x = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
x.count_sentences()