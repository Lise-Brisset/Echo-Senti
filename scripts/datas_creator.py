"""
Deuxième étape : 
On va créer des avis fictifs pour les 20 000 données, en utilisant des phrases générées par un LLM, sur un thème précis.

Liens utiles ou d'inspiration : 
- https://blog.stephane-robert.info/docs/developper/programmation/python/ollama/
- https://ollama.com/library/mistral-nemo ou https://ollama.com/library/mistral (LLM utilisé dans notre cas)
"""

import litellm # permet de faire des appels à des LLMs de manière simple et unifiée, sans se soucier de la configuration spécifique de chaque modèle.
               # Très pratique pour tester différents modèles et générer rapidement beaucoup de données.
import time
import datetime

# on affichera le temps pris par le script pour générer les données, afin d'avoir une idée de la performance de notre approche.
start_time = time.time()

print("Début du programme. \nGénération des avis clients fictifs pour la marque Chocotte...")

def generer_avis(nombre_avis):
    """
    Cette fonction permet de générer un avis fictif sur une marque de chocolat 
    fictive à partir d'un prompt envoyé à Llama3.2.

    args:
        nombre_avis (int): Le nombre d'avis à générer.
    returns:
        None: Les avis sont directement sauvegardés dans un fichier texte.
    """
    for i in range(nombre_avis):
        try:
            response = litellm.completion(
                model="ollama/llama3.2",
                messages=[{"content": """
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

                TA RÉPONSE :""", 
                "role": "user"}],
                api_base="http://localhost:11434",
                # Quelques paramètres :
                temperature=0.9, # Règle la créativité de la réponse. Plus la température est élevée, plus les réponses seront variées et créatives. Une température de 0.8 est un bon compromis pour générer des avis diversifiés.
                max_tokens=150 # Limite la longueur de la réponse pour économiser de la puissance
                #stop=["\n"] # Arrête la génération après une ligne pour éviter d'avoir plusieurs avis dans une même réponse
                )
            
            avis = response.choices[0].message.content.strip()
            
            # Sauvegarde immédiate dans un fichier
            with open("./datas/generated_reviews.txt", "a", encoding="utf-8") as f:
                f.write(avis + "\n")
            
            print(f"{datetime.datetime.now()} :\tAvis {i+1} généré et sauvegardé : \t{avis}")
            
        except Exception as e:
            print(f"{datetime.datetime.now()} :\tErreur à l'avis {i}: {e}")
            time.sleep(2) # Petite pause avant de réessayer

# Lancer la génération
generer_avis(1000)

# Affiche le temps pris pour générer les données
end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nTemps pris pour générer les données : {elapsed_time:.2f} secondes")