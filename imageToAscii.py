#!/usr/bin/env python3
import os
import sys
from PIL import Image

ASCII_SETS = {
    "math": "∂∆αβγδεμφπ∅ℝ∑∏∫∯", 
    "number": "0123456789", 
    "default": "@%#*+=-:. " ,
    "alphabet":"abcdefghijklmnopqrstuvwxyz"
}
CUSTOM_CHAIN_ARG = "-c" 
MAX_SIZE_ARG = "-s"

def get_terminal_width(max_size=80):
   
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = max_size
    return min(width, max_size)

def resize_image_to_terminal(img, max_size):
    
    term_width = get_terminal_width(max_size)
    w, h = img.size
    ratio = h / w
    new_width = term_width
    # Le facteur 0.55 compense la différence de hauteur/largeur des caractères
    new_height = int(new_width * ratio * 0.55) 
    return img.resize((new_width, max(1, new_height)))

def rgb_to_ascii(r, g, b, char_set):
   
    brightness = 0.299*r + 0.587*g + 0.114*b
    
    
    index = int((brightness / 255) * (len(char_set) - 1))
    return char_set[index]

def print_ascii_color(width, height, image, char_set):
   
    for y in range(height):
        line = ""
        for x in range(width):
            r, g, b = image[y * width + x]
            
        
            char = rgb_to_ascii(r, g, b, char_set)
            
           
            line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        print(line)

def main():
    # USAGE: <script> <chemin_image> [type_caractere | -c <chaîne_perso> | -s <size>]
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <chemin_vers_image> [option]...")
        print("Options:")
        print(f"  [type_caractere]   : Utilise un jeu prédéfini ({', '.join(ASCII_SETS.keys())})")
        print(f"  {CUSTOM_CHAIN_ARG} <chaîne> : Utilise une chaîne personnalisée pour l'ASCII art.")
        print(f"  {MAX_SIZE_ARG} <taille>     : Définit la largeur maximale (ex: -s 120, par défaut 80).")
        sys.exit(1)

    image_path = sys.argv[1]
    selected_char_set = ASCII_SETS["default"] 
    max_size = 80 


    args = sys.argv[2:]
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == MAX_SIZE_ARG:
          
            if i + 1 < len(args):
                try:
                    
                    max_size = int(args[i+1])
                    if max_size <= 0:
                        raise ValueError
                    i += 1 
                except ValueError:
                    print(f"Erreur: '{MAX_SIZE_ARG}' nécessite un entier positif valide pour la taille.")
                    sys.exit(1)
            else:
                print(f"Erreur: L'option '{MAX_SIZE_ARG}' nécessite une valeur de taille.")
                sys.exit(1)

        elif arg == CUSTOM_CHAIN_ARG:
       
            if i + 1 < len(args):
                custom_chain = args[i+1]
                if not custom_chain:
                     print("Erreur: La chaîne de caractères personnalisée ne peut pas être vide.")
                     sys.exit(1)
                selected_char_set = custom_chain
                i += 1 
            else:
                print(f"Erreur: L'option '{CUSTOM_CHAIN_ARG}' nécessite une chaîne de caractères après.")
                sys.exit(1)

        elif arg in ASCII_SETS:
            
            selected_char_set = ASCII_SETS[arg]
            
        else:
          
            print(f"Erreur: Argument optionnel non reconnu '{arg}'.")
            print(f"Types prédéfinis: {', '.join(ASCII_SETS.keys())}")
            sys.exit(1)
            
        i += 1


    try:
        img = Image.open(image_path).convert("RGB")

        img_resized = resize_image_to_terminal(img, max_size=max_size)
 
        width, height = img_resized.size
        image_pixels = list(img_resized.getdata()) 

        print_ascii_color(width, height, image_pixels, selected_char_set)

    except FileNotFoundError:
        print(f"Erreur: Fichier non trouvé à l'emplacement '{image_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur s'est produite lors du traitement de l'image: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
