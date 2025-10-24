# 🎨 Image-To-Ascii

Un script Python pour convertir n'importe quelle image en **ASCII Art en couleur** directement affichable dans votre terminal.

## ✨ Fonctionnalités

* **Conversion en ASCII Art** : Utilise la luminosité des pixels pour sélectionner le caractère ASCII approprié.
* **Couleur Rétablie** : Affiche l'ASCII Art avec la couleur originale de chaque pixel grâce aux codes d'échappement ANSI (couleur 24 bits / True Color).
* **Jeux de Caractères Personnalisables** : Choisissez parmi des jeux de caractères prédéfinis ou utilisez votre propre chaîne.
* **Largeur Maximale Définissable** : Limitez la largeur de l'image ASCII générée.

## 🚀 Installation

### Prérequis

Ce script nécessite Python 3 et la librairie `Pillow` (PIL Fork).

1.  **Installez Python 3** (si ce n'est pas déjà fait).
2.  **Installez Pillow** :

    ```bash
    pip install Pillow
    ```

### Utilisation

1.  Enregistrez le code fourni sous un nom de fichier
2.  Rendez-le exécutable (facultatif) :

    ```bash
    chmod +x ascii_converter.py
    ```
3. Pour l'utiliser comme une commande dans directement dans le terminale suivre les étapes suivantes :
    *  
    ```bash
    mkdir -p ~/.local/bin
    mv imageToAscii ~/.local/bin
    ```

## 💻 Usage

La syntaxe de base est :

```bash
python3 imageToAscii.py <chemin_vers_image> [option]...
# ou si exécutable
imageToAscii <chemin_vers_image> [option]..
```

Les options sont les suivantes : 


[jeu de caractère] Valeurs possibles : default, math, number, alphabet.

Si aucun des jeux de caractères ne plait, utiliser le paramètre suivant pour utiliser les caractères de votre choix:
```bash
-c <chaîne>
```
Si rien n'est mis, c'est le set default par défaut.


Le prochain paramètre permet de régler la taille :
```bash
-s <taille>,Définit la largeur maximale de l'image ASCII (en caractères). Par défaut : 80.
```






