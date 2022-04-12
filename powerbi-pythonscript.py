
# Used to categorize polarity and subjectivity
import matplotlib.pyplot as plt
pol = dataset['Polarity']
sentiment = []
for p in pol:

    if p > 0.7:
        sentiment.append('highly positive')
    elif p > 0.5:
        sentiment.append('positive')
    elif p > 0.2:
        sentiment.append('somewhat positive')
    elif p > -0.2:
        sentiment.append('neutral')
    elif p > -0.5:
        sentiment.append('somewhat negative')
    elif p > -0.7:
        sentiment.append('negative')
    else:
        sentiment.append('very negative')

dataset['sentiment'] = sentiment

sub = dataset['Subjectivity']
subjectivity = []
for s in sub:

    if s > 0.7:
        subjectivity.append('highly subjective')
    elif s > 0.5:
        subjectivity.append('subjective')
    elif s > 0.2:
        subjectivity.append('somewhat subjective')
    else:
        subjectivity.append('not subjective')

dataset['Sujective_cat'] = subjectivity


# Used to plot histogram of polarity in powerbi

plt.hist(dataset['Value.Polarity'])
plt.title('Distribution of the Polarity')
plt.show
