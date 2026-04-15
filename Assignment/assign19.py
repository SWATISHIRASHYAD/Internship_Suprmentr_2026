# Assignment (21/03/2026)

# Assignment Name : Build a Text Cleaner
# Description : Write code to remove punctuation, lowercase text, remove stopwords and test it.

import string

text = "OMG!!! This is sooo COOL 😂😂"

stopwords = ["is", "this", "a", "the"]

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()
cleaned = [w for w in words if w not in stopwords]

result = " ".join(cleaned)

print(result)