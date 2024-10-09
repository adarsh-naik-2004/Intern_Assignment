from textblob import TextBlob

# Sample comments ---> there was only one comment in the article that was given
comments = [
    "One of the best articles ever written on the topic. It clearly reflects the differences without any unnecessary details and is really to the point. Great job, Shweta!"
]

# Sentiment analysis
positive, negative = 0, 0

for comment in comments:
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        positive += 1
    else:
        negative += 1

print(f'Positive comments: {positive / len(comments) * 100:.2f}%')
print(f'Negative comments: {negative / len(comments) * 100:.2f}%')
