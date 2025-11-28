"""
COMPRESSOR - Algorithme de compression LZW
Auteur : Chaima Mathlouthi
"""

import os
import json
from datetime import datetime

class LZWCompressor:
    def __init__(self):
        self.initialize_dictionary()
    
    def initialize_dictionary(self):
        """Initialise le dictionnaire avec les caractères ASCII étendus"""
        self.dictionary = {}
        self.reverse_dictionary = {}
        
        # Ajout des caractères ASCII (0-255)
        for i in range(256):
            char = chr(i)
            self.dictionary[char] = i
            self.reverse_dictionary[i] = char
        
        self.next_code = 256
        self.initial_code = 256
    
    def compress(self, text):
        """
        Compresse le texte en utilisant l'algorithme LZW
        Retourne une liste de codes compressés
        """
        if not text:
            return []
        
        self.initialize_dictionary()  # Réinitialiser pour chaque compression
        result = []
        current_string = ""
        
        print("🔍 Début de la compression...")
        print(f"Texte original: {text[:50]}{'...' if len(text) > 50 else ''}")
        print(f"Longueur originale: {len(text)} caractères")
        
        for i, char in enumerate(text):
            new_string = current_string + char
            
            if new_string in self.dictionary:
                current_string = new_string
            else:
                # Ajouter le code de la chaîne actuelle au résultat
                result.append(self.dictionary[current_string])
                
                # Ajouter la nouvelle chaîne au dictionnaire
                self.dictionary[new_string] = self.next_code
                self.next_code += 1
                
                # Affichage de progression
                if len(result) % 100 == 0:
                    print(f"📦 Codes générés: {len(result)}, Dictionnaire: {self.next_code}")
                
                current_string = char
        
        # Ajouter le dernier code
        if current_string:
            result.append(self.dictionary[current_string])
        
        print(f"✅ Compression terminée!")
        print(f"Codes générés: {len(result)}")
        print(f"Taille du dictionnaire: {self.next_code}")
        
        return result
    
    def decompress(self, compressed_data):
        """
        Décompresse les données compressées
        Retourne le texte original
        """
        if not compressed_data:
            return ""
        
        self.initialize_dictionary()  # Réinitialiser pour chaque décompression
        result = ""
        
        print("🔍 Début de la décompression...")
        print(f"Données compressées: {compressed_data[:10]}{'...' if len(compressed_data) > 10 else ''}")
        
        # Premier code
        previous_code = compressed_data[0]
        result = self.reverse_dictionary[previous_code]
        current_string = result
        
        for i, code in enumerate(compressed_data[1:]):
            if code in self.reverse_dictionary:
                entry = self.reverse_dictionary[code]
            elif code == self.next_code:
                # Cas spécial pour le dernier code
                entry = current_string + current_string[0]
            else:
                raise ValueError(f"❌ Code invalide lors de la décompression: {code}")
            
            result += entry
            
            # Ajouter la nouvelle entrée au dictionnaire
            new_string = current_string + entry[0]
            self.reverse_dictionary[self.next_code] = new_string
            self.next_code += 1
            
            current_string = entry
            
            # Affichage de progression
            if (i + 1) % 100 == 0:
                print(f"📤 Caractères décompressés: {len(result)}")
        
        print(f"✅ Décompression terminée!")
        print(f"Texte reconstitué: {len(result)} caractères")
        
        return result
    
    def calculate_compression_rate(self, original_text, compressed_data):
        """Calcule le taux de compression"""
        if not original_text:
            return 0
        
        # Taille en octets (estimation)
        original_size = len(original_text)  # 1 octet par caractère ASCII
        compressed_size = len(compressed_data) * 2  # Estimation 2 octets par code
        
        compression_rate = (1 - compressed_size / original_size) * 100
        return compression_rate
    
    def save_compressed_data(self, compressed_data, filename):
        """Sauvegarde les données compressées dans un fichier"""
        try:
            with open(filename, 'w') as f:
                # Sauvegarder en JSON pour la lisibilité
                data = {
                    'compressed_data': compressed_data,
                    'timestamp': datetime.now().isoformat(),
                    'algorithm': 'LZW'
                }
                json.dump(data, f, indent=2)
            print(f"💾 Données sauvegardées dans: {filename}")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return False
    
    def load_compressed_data(self, filename):
        """Charge les données compressées depuis un fichier"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"📂 Données chargées depuis: {filename}")
            return data['compressed_data']
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            return None
    
    def analyze_compression(self, original_text, compressed_data):
        """Analyse détaillée de la compression"""
        print("\n📊 ANALYSE DE COMPRESSION")
        print("=" * 40)
        
        original_size = len(original_text)
        compressed_size = len(compressed_data)
        compression_rate = self.calculate_compression_rate(original_text, compressed_data)
        
        print(f"Taille originale: {original_size} caractères")
        print(f"Taille compressée: {compressed_size} codes")
        print(f"Taux de compression: {compression_rate:.2f}%")
        print(f"Taille du dictionnaire: {self.next_code} entrées")
        
        if compression_rate > 0:
            print("✅ Compression efficace")
        else:
            print("⚠️  Aucune compression obtenue")
        
        return compression_rate

def demonstrate_compression():
    """Démonstration du fonctionnement de l'algorithme"""
    compressor = LZWCompressor()
    
    # Texte de démonstration
    test_text = "ABABABAABABABAABABABA"
    
    print("🎭 DÉMONSTRATION LZW")
    print("=" * 50)
    print(f"Texte de test: {test_text}")
    
    # Compression
    compressed = compressor.compress(test_text)
    print(f"\n📦 Données compressées: {compressed}")
    
    # Décompression
    decompressed = compressor.decompress(compressed)
    print(f"\n📤 Texte décompressé: {decompressed}")
    
    # Vérification
    if test_text == decompressed:
        print("✅ SUCCÈS: Texte original parfaitement reconstitué!")
    else:
        print("❌ ÉCHEC: Le texte décompressé ne correspond pas à l'original")
    
    # Analyse
    compressor.analyze_compression(test_text, compressed)

def main():
    """Fonction principale avec interface utilisateur"""
    compressor = LZWCompressor()
    
    print("📦" * 20)
    print("     COMPRESSEUR LZW - B1 Algo")
    print("📦" * 20)
    
    print("\nFonctionnalités:")
    print("1. 🔍 Compression de texte")
    print("2. 📤 Décompression de données")
    print("3. 💾 Sauvegarder données compressées")
    print("4. 📂 Charger données compressées")
    print("5. 🎭 Démonstration algorithmique")
    print("6. ❌ Quitter")
    
    while True:
        print("\n" + "=" * 50)
        choice = input("\nChoisissez une option (1-6): ").strip()
        
        if choice == '1':
            # Compression
            text = input("Entrez le texte à compresser: ")
            if text:
                compressed = compressor.compress(text)
                print(f"\n✅ Compression réussie!")
                print(f"Codes: {compressed}")
                
                # Analyse
                rate = compressor.analyze_compression(text, compressed)
                
                # Sauvegarde optionnelle
                save = input("\n💾 Sauvegarder dans un fichier? (o/n): ").lower()
                if save == 'o':
                    filename = input("Nom du fichier: ").strip() or "compressed_data.json"
                    compressor.save_compressed_data(compressed, filename)
            else:
                print("❌ Texte vide!")
        
        elif choice == '2':
            # Décompression
            data_input = input("Entrez les données compressées (ex: [65,66,256]): ").strip()
            try:
                if data_input.startswith('[') and data_input.endswith(']'):
                    compressed_data = eval(data_input)
                    decompressed = compressor.decompress(compressed_data)
                    print(f"\n✅ Texte décompressé: {decompressed}")
                else:
                    print("❌ Format invalide. Utilisez: [65,66,256]")
            except Exception as e:
                print(f"❌ Erreur: {e}")
        
        elif choice == '3':
            # Sauvegarde
            data_input = input("Entrez les données à sauvegarder (ex: [65,66,256]): ").strip()
            try:
                compressed_data = eval(data_input)
                filename = input("Nom du fichier: ").strip() or "compressed_data.json"
                compressor.save_compressed_data(compressed_data, filename)
            except Exception as e:
                print(f"❌ Erreur: {e}")
        
        elif choice == '4':
            # Chargement
            filename = input("Nom du fichier: ").strip() or "compressed_data.json"
            if os.path.exists(filename):
                compressed_data = compressor.load_compressed_data(filename)
                if compressed_data:
                    print(f"Données chargées: {compressed_data}")
                    
                    # Décompression automatique
                    decompress = input("Décompresser ces données? (o/n): ").lower()
                    if decompress == 'o':
                        decompressed = compressor.decompress(compressed_data)
                        print(f"✅ Texte décompressé: {decompressed}")
            else:
                print("❌ Fichier non trouvé!")
        
        elif choice == '5':
            # Démonstration
            demonstrate_compression()
        
        elif choice == '6':
            print("👋 Au revoir!")
            break
        
        else:
            print("❌ Option invalide!")

if __name__ == "__main__":
    main()