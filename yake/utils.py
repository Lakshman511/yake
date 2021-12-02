import spacy


import spacy
def get_pos_tag(text):
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(text)
  res = [(token, token.pos_) for token in doc]
  return res 

def satisfied(text):
  text = set(text.split())
  with open("./StopwordsList/stopwords_en.txt") as file:
    stopwords = file.readlines()
  for word in stopwords:
    if(word.strip() in text):
      return False
  return True

