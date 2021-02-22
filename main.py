import emot

import mysqlClass
import re
from emot.emo_unicode import UNICODE_EMO, EMOTICONS


def convert_emojis(text):
    i = 0
    for emot in UNICODE_EMO:
        text = text.replace(emot, "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()))
        i = i+1
    return i

text1 = "Hilarious 😂. The feeling of making a sale 😎, The feeling of actually fulfilling orders 😒"
print(convert_emojis(text1))
def convert_emoticons(text):

    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
        i = i+1
    return i
# Example
text = "Hello :-) :-)"
#print(convert_emoticons(text))

