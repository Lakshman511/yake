import spacy
import os

def get_pos_tag(text):
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(text)
  res = [(token, token.pos_) for token in doc]
  return res 

def satisfied(text):
  text = set(text.split())
  dir_path = os.path.dirname(os.path.realpath(__file__))
  local_path = os.path.join("StopwordsList", "stopwords_en.txt")
  if os.path.exists(os.path.join(dir_path,local_path)) == False:
    local_path = os.path.join("StopwordsList", "stopwords_noLang.txt")
        
  resource_path = os.path.join(dir_path,local_path)
  with open(resource_path) as file:
    stopwords = file.readlines()
  stopwords = [word.strip() for word in stopwords]
  for word in stopwords:
    if(word.strip() in text):
      return False
  return True


