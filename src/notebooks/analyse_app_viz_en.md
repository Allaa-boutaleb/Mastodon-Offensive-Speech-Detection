# Classification Model
In order to predict whether a toot is hateful or not, we developed four models using the scikit-learn library: Logistic Regression, Random Forest, Support Vector Machine (SVM), and Naive Bayes.

Logistic Regression: This model models the probability that an instance belongs to a specific class.
Random Forest: It combines predictions from multiple decision trees to produce a more robust and accurate prediction.
Support Vector Machine (SVM): This model identifies the hyperplane that maximizes the margin between different classes.
Naive Bayes: It is based on Bayes' theorem and assumes that features are independent.
These models are then trained with the training data, and the optimal model is chosen based on the best prediction rate during testing.

Regarding the ground truth (hate, non-hate), we used the pre-trained model (facebook-roberta) from Facebook, known for its performance. It was trained on large datasets with human annotations.

# Metrics
We evaluated the performance of our models using four metrics: accuracy_score, precision_score, recall_score, and f1_score, comparing predicted values with actual values.

accuracy_score: Measures the proportion of correct predictions among all predictions. Formule : (TP + TN) / (TP + TN + FP + FN), où TP : True Positives, TN : True Negatives, FP : False Positives et FN : False Negatives.
precision_score: Measures the proportion of correct positive predictions among all positive predictions made by the model. Formule : TP / (TP + FP).
recall_score: Measures the proportion of true positives among all true positive values. Formule : TP / (TP + FN).
f1_score: The harmonic mean of precision and recall, used to find a balance between precision and recall. Formule : 2 * (precision * recall) / (precision + recall).

After training all models, the Random Forest proved to be the best predictor on the test data, achieving a perfect prediction rate of 100% on all metrics. Our model successfully classified all test examples optimally. Therefore, we use this model for future predictions regarding the classification of toots as hateful or non-hateful.

# Number of Words in Each Toot
In the figure "Histogram of Word Count in Content Column (nb_words <= 200)," we present the frequency of the number of words in toots. We observe a distribution that follows Zipf's law, where the frequency of words in a toot is inversely proportional to their rank. There is an abundance of toots with a small number of words, and this frequency decreases rapidly with an increase in the number of words.

We conducted a similar study regarding the number of characters (toot length) and found that the distribution is similar to that of the number of words, which is understandable as the number of characters increases with the number of words.

# Word Frequencies
In the figure "Histogram of Word Frequency in Content Column (nb_words <= 200)," we plotted the distribution of word frequencies in the entire database. We observed that the word frequency distribution also follows Zipf's law, meaning that the frequency of words decreases rapidly from the most frequent to the least frequent. The "Top 10 Most Common Words" figure displays the frequencies of the 10 most common words, which happen to be English stopwords.

# Word Cloud
We used WordCloud to visualize the most frequent words, noting a predominance of links to sites such as YouTube or Mastodon itself. We also observed the presence of hateful words, such as "die."