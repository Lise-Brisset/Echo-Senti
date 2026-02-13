"""
Première étape de ce projet :
Nous allons générer les pseudos pour 20 000 données fictives.
"""

import random

# Ces deux listes ont été générées à partir de Gemini.
# 150 noms d'animaux variés et rigolos
animaux = [
    "Axolotl", "Blobfish", "Capybara", "Dahu", "Echidne", "Fennec", "Glouton", "Hamster", "Iguane", "Jaguar",
    "Kakapo", "Lemurien", "Marmotte", "Narval", "Ocelot", "Pangolin", "Quokka", "RatonLaveur", "Suricate", "Tardigrade",
    "Urubu", "Varan", "Wombat", "Xenope", "Yack", "Zebre", "Alpaga", "Bernache", "Chinchilla", "Dingo",
    "Ecureuil", "Flamant", "Gibbon", "Herisson", "Ibis", "Jerboa", "Kiwi", "Lama", "ManteReligieuse", "Numbat",
    "Oryx", "Paresseux", "Quetzal", "RequinMarteau", "Saola", "Tapir", "Unau", "Vipere", "Wallaby", "Xerus",
    "Yeti", "Zorille", "Abeille", "Bousier", "Cigale", "Drosophile", "Ecrevisse", "Fourmi", "Grillon", "Hanneton",
    "Isopode", "Jars", "Krill", "Libellule", "Moustique", "Nereide", "Oursin", "Puce", "QueueFourchue", "Rosalie",
    "Scarabee", "Tique", "Unicorne", "Vrillette", "Wapiti", "Xylocope", "Yohimbe", "Zygene", "Anchois", "Baracouda",
    "Carpe", "Daurade", "Eperlan", "Fletan", "Goujon", "Hareng", "Ide", "Joinville", "Kawakawa", "Lotte",
    "Mulet", "Nason", "Omble", "Perche", "Quinnat", "Raie", "Saumon", "Tanche", "Uranoscope", "Vandoise",
    "Whiptail", "Xiphophore", "Yellowtail", "Zander", "Albatros", "Buse", "Condor", "Driade", "Epervier", "Faucon",
    "Goglu", "Hieron", "Indicateur", "Jaco", "Kestrel", "Linotte", "Merle", "Noctuelle", "Outarde", "Perruche",
    "Quiscale", "Rousserolle", "Sittelle", "Trogon", "Upupa", "Vanneau", "Whydah", "Xema", "Yuhina", "Zosterops",
    "Agouti", "Babouin", "Coati", "Damalisque", "Elan", "Fouine", "Genette", "Hyene", "Isatis", "Jubarte",
    "Koudou", "Loris", "Moufette", "Nilgaut", "Okapi", "Panda", "Roussette", "Serval", "Tarsier", "Vison"
]

# 150 adjectifs variés, un peu loufoques ou épiques
adjectifs = [
    "Acrobate", "Bavard", "Cinglé", "Dodu", "Effronté", "Farfelu", "Grondeur", "Hagard", "Intrépide", "Jovial",
    "Kitch", "Lunaire", "Malicieux", "Nebuleux", "Optimiste", "Pétillant", "Quadrillé", "Radieux", "Saugrenu", "Timoré",
    "Utopiste", "Vaporeux", "Woke", "Xylophone", "Yéyé", "Zélé", "Atomique", "Bigarré", "Cosmique", "Déjanté",
    "Électrique", "Flamboyant", "Galactique", "Héroïque", "Invisible", "Jubilatoire", "Kryptonique", "Légendaire", "Mystique", "Nomade",
    "Onirique", "Psychédélique", "Quantique", "Robotique", "Solaire", "Tellurique", "Universel", "Volcanique", "Watté", "Xénon",
    "Yoga", "Zen", "Ambitieux", "Brillant", "Captivant", "Dynamique", "Éclatant", "Fringant", "Généreux", "Habile",
    "Ingénieux", "Joueur", "Kokasse", "Lucide", "Magnétique", "Noble", "Opulent", "Prestigieux", "Qualitatif", "Robuste",
    "Savant", "Tenace", "Unique", "Valeureux", "Western", "Xxl", "Yogi", "Zigzag", "Astucieux", "Bagarreur",
    "Chafouin", "Dodelinant", "Ébouriffé", "Frénétique", "Goguenard", "Hilare", "Impertinent", "Jongleur", "Karatéka", "Loufoque",
    "Mirobolant", "Nonchalant", "Outrancier", "Pantois", "Quinteux", "Rêveur", "Sifflotant", "Turbulent", "Urbain", "Vagabond",
    "Whiskas", "Xérophile", "Yéménite", "Zinzolin", "Alambiqué", "Baroque", "Chimerique", "Diaphane", "Évanescent", "Feutré",
    "Gracile", "Harmonieux", "Insolite", "Jaspé", "Kitschissime", "Laconique", "Moelleux", "Nacré", "Onctueux", "Placide",
    "Quintessencié", "Rutilant", "Satiné", "Ténu", "Unicolore", "Velouté", "Wagnérien", "Xanthique", "YeuxBleus", "Zoné",
    "Affamé", "Bondissant", "Câlin", "Duveteux", "Éveillé", "Farouche", "Gourmand", "Hirsute", "Inquiet", "Jaunissant",
    "Kandinsky", "Lustré", "Mignon", "Nerveux", "Observateur", "Pataud", "Râleur", "Solitaire", "Tacheté", "Vif"
]

# ==> offre 22 500 possibilités 

liste_pseudos = []
nbr_pseudos = 0
while nbr_pseudos != 20000:
    pseudo = random.choice(animaux) + "_" + random.choice(adjectifs)
    liste_pseudos.append(pseudo)
    nbr_pseudos += 1

print(f"Nombre de pseudos générés : {nbr_pseudos}")
print("Exemples de pseudos générés :")
print(liste_pseudos[:10])

# on sauve la liste dans un fichier texte simple : 
with open("./datas/pseudos.txt", "w") as f:
    for pseudo in liste_pseudos:
        f.write(pseudo + "\n")

print("La liste de pseudos a été sauvegardée dans le fichier 'pseudos.txt'.")
print("Fin du programme de génération de pseudos.")