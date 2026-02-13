"""
Deuxième étape : 
On va créer des avis fictifs pour les 20 000 données, en utilisant des phrases générées par un LLM, sur un thème précis.
"""

import litellm # permet de faire des appels à des LLMs de manière simple et unifiée, sans se soucier de la configuration spécifique de chaque modèle.
               # Très pratique pour tester différents modèles et générer rapidement beaucoup de données.


# Configuration : utiliser Ollama en local
response = litellm.completion(
    model="ollama/mistral-nemo",    # Format : ollama/nom-du-modele
    messages=[
        {"role": "user", "content": """
        Rôle : Tu es un générateur de données de test pour une application d'analyse de sentiments.

        Tâche : Génère une liste de 20 avis clients fictifs pour une marque de chocolat imaginaire nommée "Chocotte".

        Consignes de rédaction :

            Varie les sentiments : 50% d'avis positifs, 20% d'avis neutres, 30% d'avis négatifs.

            Varie la longueur des commentaires : certains très courts ("Super !"), d'autres détaillés expliquant la texture ou la livraison.

            Utilise des dates aléatoires réparties sur l'année 2025.

        Format de sortie : Génère uniquement du texte brut sous format tabulé : date [TAB] commentaire. Ne mets pas d'entête de colonne.

        Exemple de format attendu :
        12/01/2025	La livraison était un peu lente mais les croquettes sont de qualité.
        05/02/2025	Mon chat adore, je recommande vivement cette marque ! 
        """}
    ]
)

# affiche le résultat
print(response.choices[0].message.content)