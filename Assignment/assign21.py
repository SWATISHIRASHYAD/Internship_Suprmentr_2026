# [7:31 pm, 14/4/2026] S: Assignment (26/03/2026)

# Assignment Name : Movie Review Analyzer
# Description : Build a simple sentiment analyzer and test on 5 reviews.

from textblob import TextBlob

reviews = [
    "This movie is amazing",
    "I hate this film",
    "It was okay not great",
    "Fantastic acting and story",
    "Worst movie ever"
]

for r in reviews:
    analysis = TextBlob(r)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        result = "Positive"
    elif polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"
    print(r, "->", result)










