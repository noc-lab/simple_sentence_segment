import spacy
from simple_sentence_segment import SentenceSegmenter

def main():
  sample_text = """Admission Date:  1-1-01               Discharge Date:  1-1-01
Date of Birth: 1-1-01        Sex:  F

HISTORY OF PRESENT ILLNESS: Lorem ipsum dolor sit amet, consectetuer 
adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum 
sociis natoque penatibus et magnis dis parturient montes, nascetur
ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, 
pretium quis, sem.

Nulla consequat massa quis enim. Donec pede justo, fringilla vel,
aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet 
a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. 

Summary:

1. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi.
Aenean vulputate eleifend tellus.

2. Aenean leo ligula, porttitor eu, consequat
vitae, eleifend ac, enim. 

3. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus."""

  nlp = spacy.load('en')
  nlp.add_pipe(SentenceSegmenter().set_sent_starts, name='sentence_segmenter', before='parser')
  doc = nlp(sample_text)

  for sen in doc.sents:
      print(repr(sen.string))


if __name__ == '__main__':
  main()
