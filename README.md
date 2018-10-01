# A simple sentence segment tools

This is a simple sentence segment tools based on a decision tree. It is designed for some complicated sentence segment
tasks such as reports with fix width line breaks.


Example:

```python
from simple_sentence_segment import sentence_segment

sample_text = """Admission Date:  1-1-01      
Discharge Date:  1-1-01
Date of Birth: 1-1-01  
Sex: F

HISTORY OF PRESENT ILLNESS: Lorem ipsum dolor sit amet, consectetuer 
adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum 
sociis natoque penatibus et magnis dis parturient montes, nascetur
ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, 
pretium quis, sem.
 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel,
aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet 
a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. 

Summary:

1. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
 
2. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. 

3. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus."""

for s, t in sentence_segment(sample_text):
    print(repr(sample_text[s:t].strip()))
```

The output is
```
'Admission Date:  1-1-01'
'Discharge Date:  1-1-01'
'Date of Birth:'
'1-1-01'
'Sex: F'
'HISTORY OF PRESENT ILLNESS: Lorem ipsum dolor sit amet, consectetuer \nadipiscing elit.'
'Aenean commodo ligula eget dolor.'
'Aenean massa.'
'Cum \nsociis natoque penatibus et magnis dis parturient montes, nascetur\nridiculus mus.'
'Donec quam felis, ultricies nec, pellentesque eu, \npretium quis, sem.'
'Nulla consequat massa quis enim.'
'Donec pede justo, fringilla vel,\naliquet nec, vulputate eget, arcu.'
'In enim justo, rhoncus ut, imperdiet \na, venenatis vitae, justo.'
'Nullam dictum felis eu pede mollis pretium.'
'Summary:'
'1.'
'Integer tincidunt.'
'Cras dapibus.'
'Vivamus elementum semper nisi.'
'Aenean vulputate eleifend tellus.'
'2.'
'Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.'
'3.'
'Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.'
```

The model is trained based on some reports shown as examples using some hand-craft rules by the author. Feedback is 
always welcome so that the author can add more rules in generating training examples and have a better model.