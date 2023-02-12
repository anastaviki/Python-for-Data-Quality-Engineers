# homEwork:
#
#   tHis iz your homeWork, copy these Text to variable.
#
#
#
#   You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
#
#
#
#   it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
#
#
#
#   last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

import re  # import module

# initialise new line
start_text = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


print("Text: \n", start_text)
sentences = start_text.split('.')  # split to sentences
for sentence in sentences:  # loop for every sentence
    if not sentence:  # check if smth exists in sentence
        continue
    sentence = sentence.strip()  # remove whitespaces in begin and in the end of sentence
    sentence_new = sentence.capitalize()  # first letter in sentence in upper case
    start_text = start_text.replace(sentence, sentence_new)  # generate new sentence

last_words = re.findall(r'\b\w+\.', start_text)  # find all last words in every sentence
last_sent = "".join(last_words).replace(".", " ").strip().capitalize() + '.'  # generate last sentence
new_text = start_text + " " + last_sent  # add last sentence to existing sentence
new_text = new_text.replace(" iz ", " is ")  # replace incorrect iz
print("Text after all changes: \n",new_text)
res = len(re.findall(r"\s", start_text))  # find all whitespaces
print("Number of whitespaces: ", res)
