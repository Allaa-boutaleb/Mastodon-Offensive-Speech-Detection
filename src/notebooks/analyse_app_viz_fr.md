# Modéle de classification

Afin de prédire si un toot est haineux ou non, nous avons développé quatre modèles à l'aide de la bibliothèque scikit-learn : Régression logistique, Forêt aléatoire, Machine à vecteurs de support (SVM) et Naive Bayes.

Régression logistique : Ce modèle modélise la probabilité qu'une instance appartienne à une classe spécifique.
Forêt aléatoire : Il combine les prédictions de plusieurs arbres de décision pour produire une prédiction plus robuste et précise.
Machine à vecteurs de support (SVM) : Ce modèle identifie l'hyperplan qui maximise la marge entre différentes classes.
Naive Bayes : il repose sur le théorème de Bayes et suppose que les caractéristiques sont indépendantes.
Ensuite, ces modèles sont entraînés avec les données d'entraînement, et le modèle optimal est choisi en fonction du meilleur taux de prédiction lors du test.

En ce qui concerne la groundtruth (haine, non-haine), nous avons utilisé le modèle model pré-entrainé (facebook-roberta) de Facebook, réputé pour sa performance. Il a été entraîné sur des données volumineuses avec des annotations humaines.

# métriques
Nous avons évalué les performances de nos modèles en utilisant quatre métriques : accuracy_score, precision_score, recall_score et f1_score, qui comparent les valeurs prédites avec les valeurs réelles.

accuracy_score : Mesure la proportion de prédictions correctes parmi l'ensemble des prédictions. Formule : (TP + TN) / (TP + TN + FP + FN), où TP : True Positives, TN : True Negatives, FP : False Positives et FN : False Negatives.
precision_score : Mesure la proportion de prédictions positives correctes parmi l'ensemble des prédictions positives faites par le modèle. Formule : TP / (TP + FP).
recall_score : Mesure la proportion de vrais positifs parmi l'ensemble des valeurs réelles positives. Formule : TP / (TP + FN).
f1_score : La moyenne harmonique de la précision et du rappel. Utilisé pour trouver un équilibre entre la précision et le rappel. Formule : 2 * (precision * recall) / (precision + recall).
Après l'entraînement de tous les modèles, la Random Forest s'est avérée être le meilleur prédicteur sur les données de test, avec un taux de prédiction parfait de 100% sur toutes les métriques. Notre modèle a réussi à classer de manière optimale tous les exemples de test. Par conséquent, c'est ce modèle que nous utilisons pour les prédictions futures concernant la classification des toots en tant que haineux ou non haineux.

# Nombre de mots dans chaque toot
Dans la figure "Histogramme du nombre de mots dans la colonne du contenu (nb_mots <= 200)", nous présentons la fréquence du nombre de mots dans les toots. 
Nous observons une distribution du nombre de mots dans un toot qui suit la loi de Zipf. Cette loi stipule que, dans une distribution donnée, 
la fréquence d'un élément est inversement proportionnelle à son rang. Il y a une abondance de toots avec un faible nombre de mots, 
et cette fréquence diminue rapidement avec l'augmentation du nombre de mots.

Nous avons également effectué la même étude en ce qui concerne le nombre de caractères (longueur du toot) et avons constaté que la distribution est similaire 
à celle du nombre de mots. Cela est compréhensible car le nombre de caractères augmente avec le nombre de mots.


# Fréquences des mots
Dans la figure "Histogramme de la fréquence des mots dans la colonne du contenu (nb_mots <= 200)", nous avons représenté la distribution des fréquences des 
des 200 mots les plus fréquent dans l'ensemble de la base de données. Nous avons observé que la distribution de la fréquence des mots suit également la loi de Zipf, ce qui signifie que 
la fréquence des mots diminue rapidement des mots les plus fréquents aux moins fréquents. La figure "Top 10 des mots les plus fréquents" présente les fréquences 
des 10 mots les plus courants, qui se révèlent être des stopwords de la langue anglaise.

# Word Cloud
Nous avons utilisé WordCloud pour visualiser les mots les plus fréquents. Nous avons noté une prédominance de liens vers des sites tels que YouTube ou Mastodon lui-même. 
Nous avons également observé la présence de mots haineux tels que "die".