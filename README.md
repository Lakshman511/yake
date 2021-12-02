# Yet Another Keyword Extractor (Yake)

* In this repo I've just tweaked the YAKE algorithm so that it gives more relavent keywords.
* I used spacy POS tagger and generated the POS tags of all the words in the sentence
* The I have added more weightage to the nouns
* While filtering the keywords I have removed the keywords which contain stop words

## Steps to use this
```
#instal the library using
pip install git+https://github.com/Lakshman511/yake.git

from yake import KeywordExtractor

kwextractor = KeywordExtractor(dedupLim=0.6, dedupFunc="jaro_winkler")
kwextractor.extract_keywords("In this lesson, we will review certain fundamental concepts of electricity, electric charge, electric current, potential difference, Ohm's Law, and so on.")

"""
For the above example output is..
[('Ohm Law', 0.0008387892117202491),
 ('potential difference', 0.004634352811790328),
 ('electric charge', 0.005745539503004705),
 ('fundamental concepts', 0.033100028790236186),
 ('charge', 0.0392734209469605),
 ('difference', 0.0392734209469605)]
"""
```
