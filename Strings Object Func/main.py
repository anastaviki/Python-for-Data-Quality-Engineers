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


# capitalise any text
def text_capitalise(p_start_text):
    sentences = p_start_text.split('.')  # split to sentences
    for sentence in sentences:  # loop for every sentence
        if not sentence:  # check if smth exists in sentence
            continue
        sentence = sentence.strip()  # remove whitespaces in begin and in the end of sentence
        sentence_new = sentence.capitalize()  # first letter in sentence in upper case
        p_start_text = p_start_text.replace(sentence, sentence_new)  # generate new sentence
    return p_start_text


# generate sentence from words in text witch is match with regular expression
def generate_sentence_reg (p_start_text, p_reg):
    last_words = re.findall(p_reg, p_start_text)  # find all last words in every sentence
    r_last_sent = "".join(last_words).replace(".", " ").strip().capitalize() + '.'  # generate last sentence
    return r_last_sent


print("Text: \n", start_text)
start_text = text_capitalise(start_text)  # capitalise text
new_text = start_text
last_sent = generate_sentence_reg(start_text, r'\b\w+\.')  # generate new sentence
# add last sentence
new_text = new_text.replace("END OF this Paragraph.".lower(), "END OF this Paragraph! ".lower()+last_sent)
new_text = new_text.replace(" iz ", " is ")  # replace incorrect iz
print("Text after all changes: \n", new_text)
res = len(re.findall(r"\s", start_text))  # find all whitespaces
print("Number of whitespaces: ", res)
