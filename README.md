J'ai lancé un promt à Gemini pour lui demander de me générer une consigne pour un projet type projet de fin d'année. Celui-ci devra mobiliser les principaux outils de mon parcours académique. Voici ci-dessous la consigne détaillée : 

Projet : "Echo-Senti" – Système de Monitoring et d'Analyse de Réputation en Temps Réel

##### 1. La Problématique

Une marque (ou une entité publique) souhaite comprendre non seulement ce que l'on dit d'elle sur le web, mais aussi comment on en parle et quels sont les thèmes émergents qui déclenchent des réactions passionnées. Ton objectif est de construire un pipeline complet, de la collecte à la visualisation.


##### 2. Le Cahier des Charges
Phase A : Acquisition et Structuration (Le "Data Engineering")

    Source : Choisir une plateforme (Reddit, NewsAPI, ou un scrapeur de commentaires d'un site de presse).

    Action : Récupérer dynamiquement des données textuelles sur un mot-clé spécifique.

    Stockage : Organiser ces données de manière tabulaire pour permettre des manipulations statistiques ultérieures (dates, auteurs, corps du texte, métadonnées).

Phase B : Prétraitement et Analyse Linguistique (Le "Core NLP")

    Nettoyage : Mise en place d'une chaîne de traitement robuste (normalisation, gestion du bruit spécifique au web).

    Enrichissement : Pour chaque document, tu devras extraire :

        La polarité (Sentiment Analysis).

        Les entités nommées (NER) pour identifier les acteurs clés cités.

        La morphosyntaxe (POS tagging) pour filtrer, par exemple, uniquement les adjectifs qualificatifs.

Phase C : Modélisation Avancée (Le "Machine Learning")

    Clustering / Topic Modeling : Ne te contente pas de lire les textes. Ton système doit regrouper automatiquement les messages par thématiques (ex: "Prix", "Service Client", "Innovation").

    Classification : Entraîne un modèle capable de catégoriser la "toxicité" ou l'urgence d'un message pour alerter un modérateur.

Phase D : Restitution et Interface (Le "Déploiement")

    Visualisation : Créer des graphiques dynamiques (évolution du sentiment dans le temps, nuages de mots-clés par thématique).

    Interface Utilisateur : Développer une application web légère où l'utilisateur tape un mot-clé et voit le tableau de bord se mettre à jour.

##### 3. Les Livrables attendus pour ton CV

    Le Code Source : Propre, documenté (Docstrings), avec un fichier listant les dépendances.

    Le README : Une explication de tes choix de modèles (Pourquoi ce transformeur plutôt qu'un modèle statistique classique ? Comment as-tu géré le déséquilibre des classes ?).

    L'Application : Un lien vers l'outil fonctionnel (hébergé gratuitement par exemple).

##### 4. Pourquoi ce projet ?

    Pandas sera ton meilleur ami pour la phase A et B.

    Scikit-learn / Transformers seront au cœur de la phase C.

    Le Web (API/Framework) validera ta capacité à rendre ton travail accessible.




### Les Grandes étapes : 

#### 1. La génération automatique de données avec LLM

- J'ai généré une liste de 20 000 pseudonymes distincts les uns des autres.

- Génération du prompt.

- Génération des avis fictifs avec Mistral Nemo d'ollama. En utilisant la librairie LiteLLM de Python car elle est plus adaptée à une génération massive et rapide de données (Scripts de masse, tests rapides) que LangChain (Agents IA, RAG, Apps complexes). Mistral Nemo est assez légé (16 Go de RAM) et fluide en français, c'est l'un des meilleurs pour comprendre l'argot, les tournures de phrases locales et la ponctuation française.


Notes diverses sur les LLMs : 

Pour envisager utiliser le LLM le plus adapté à notre demande (génération d'avis), nous avons tester différents LLMs capable de générer du texte en français et aussi de tourner sur notre machine (24Go de RAM).

| Modèle | Paramètres LiteLLM | Retour sur la génération de 50 avis |
| :--- | :--- | :--- |
| **Mistral** | `temp: 0.8`, `max_tokens: 200`, `stop: ["\n"]` | 12 minutes, Les avis générés sont assez redondants dans le vocabulaire utilisé et le message passé. Le paramètre stop permet d'arrêter le modèle s'il génère plusieurs avis et n'en avoir qu'un. |
| **Mistral-Nemo (12B)** | `temp: 0.8`, `max_tokens: 200`, `stop: ["\n"]` | 20 minutes, Même remarque qu'avec le LLM Mistral sauf qu'il est plus lent probablement car il nécessite une plus grnade puissance de RAM pour tourner. |
| **Phi3** | `temp: 0.8`, `max_tokens: 200`, `stop: ["\n"]` | 1min30, ne respecte pas bien la consigne de format. Beaucoup d'erreur de génération (ex : lignes vides) |
| **Llama3.2** | `temp: 0.8`, `max_tokens: 200`| 16 minutes, Semble donner des résultats beaucoup plus naturels, il ne semble pas y avoir d'erreur d'accord que chez les modèles Mistral et Mistral-Nemo, le français est plus naturel. Sans paramètre stop le modèle génère beaucoup plus d'avis que demander, faudrait-il revoir le prompt pour l'obliger à ne générer qu'un unique avis. |


**Après cette expérience à part, nous choisissons de prendre le LLM Llama3.2 qui a permis de générer de nombreux avis très variés, dans un français naturel et en un temps relativement correct.**


Après de nombreux ajustement du prompt, voici celui qui génère le mieux ce que nous lui demandons et qui fait le moins d'erreur de format : 

```
RÔLE : Tu es un générateur de données de test pour une application d'analyse de sentiments.

TÂCHE : Génère un seul avis client fictif pour une marque de chocolat imaginaire nommée "Chocotte". Cette marque fait tout type de chocolat : tablettes de chocolat, chocolat en poudre, biscuits et gâteaux au chocolat.

CONSIGNES DE RÉDACTION :
    Varie les sentiments : L'avis peut-être aléatoirement positif, neutre ou négatif.
    Varie la longueur des commentaires : L'avis peut-être très court ("Super !"), ou détaillé expliquant la texture, le goût, la livraison ou tout autre avis spécifique à ces produits.
    Utilise une date aléatoire répartie entre le 01/01/2024 et le 31/12/2025.

CONTRAINTES STRICTES :
1. Génère UN SEUL avis.
2. NE METS PAS d'entête (pas de "date \t commentaire").
3. NE FAIS AUCUNE introduction ("Voici l'avis...") ou conclusion.
4. FORMAT : date[TAB]commentaire
5. DATE : entre 01/01/2024 et 31/12/2025.

RÉPONSE ATTENDUE (exemple) :
25/12/2024\tLe chocolat noir est incroyable, je recommanderai !

TA RÉPONSE :
```

Voici la réponse donnée avec ce prompt : 

```
22/02/2025	J'ai acheté des tablettes de chocolat au goût vanille pour mes enfants et j'ai été vraiment déçu par la qualité et la texture du chocolat. Cela ressemble à du papier mouillé plutôt qu'à du chocolat frais et cuit !
24/02/2025	Moi j'ai acheté un gâteau au chocolat de Chocotte et c'était absolument délicieux ! Le chocolat était très fondu et le goût était parfaitement équilibré. Je me sens vraiment satisfait de ma décision d'acheter ce gâteau et je vais certainement en commander à nouveau !
02/03/2025
C'est une déception, j'attendais plus de créativité et de personnalisation dans ces biscuits. Le goût du chocolat était bon mais rien d'étonnant !
20/04/2025	J'ai acheté les tablettes de chocolat au fromage pour mon anniversaire et j'en ai mangé 3 dans la journée ! La texture était parfaite, légèrement croustillante et pas trop tendre. Le goût est intense mais pas trop acide ou trop sucré, juste parfait ! J'ai été impressionné par la qualité du chocolat.
10/04/2025
J'ai acheté le délicieux gâteau au chocolat de Chocotte pour le mariage de ma fille et j'en ai été très satisfait ! La texture était légère mais savoureuse, et la quantité de chocolat ajoutée avait une saveur intense. Je l'ai servi aux invités avec succès.
```

Il reste des ajustements à faire tel que mettre une tabulation au lieu d'un retour à la ligne entre la date et l'avis. Ceci sera possible avec une Expression Regulière après la génération de l'ensemble des données. 



##### Prochaines étapes :

- Faire le nettoyage des données générées
- Mettre en forme les données : Pseudo / Date / Avis
- Peut être faire une petite analyse des différences entre les données 1 et 2 car les paramètres ont un peu changés. (Données générées 1 : 0.8 de température / 200 tokens max et Données générées 2 : 0.9 de température / 150 tokens max)
