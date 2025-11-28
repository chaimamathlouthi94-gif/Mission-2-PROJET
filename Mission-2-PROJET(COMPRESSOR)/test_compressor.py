"""
Tests unitaires pour le compresseur LZW
"""

import unittest
import sys
import os
import json
import tempfile

# Ajouter le chemin pour importer le module compressor
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from compressor import LZWCompressor

class TestLZWCompressor(unittest.TestCase):
    """Tests complets pour la classe LZWCompressor"""
    
    def setUp(self):
        """Initialisation avant chaque test"""
        self.compressor = LZWCompressor()
    
    def test_initial_dictionary(self):
        """Test l'initialisation correcte du dictionnaire"""
        # Vérifier les caractères ASCII de base
        self.assertEqual(self.compressor.dictionary['A'], 65)
        self.assertEqual(self.compressor.dictionary['a'], 97)
        self.assertEqual(self.compressor.dictionary['0'], 48)
        
        # Vérifier le dictionnaire inverse
        self.assertEqual(self.compressor.reverse_dictionary[65], 'A')
        self.assertEqual(self.compressor.reverse_dictionary[97], 'a')
        
        # Vérifier le code suivant
        self.assertEqual(self.compressor.next_code, 256)
    
    def test_compress_empty_text(self):
        """Test la compression d'un texte vide"""
        compressed = self.compressor.compress("")
        self.assertEqual(compressed, [])
    
    def test_compress_single_character(self):
        """Test la compression d'un caractère unique"""
        compressed = self.compressor.compress("A")
        self.assertEqual(compressed, [65])  # Code ASCII de 'A'
    
    def test_compress_repetitive_text(self):
        """Test la compression d'un texte répétitif"""
        text = "ABABABA"
        compressed = self.compressor.compress(text)
        
        # Vérifier que la compression produit des codes
        self.assertTrue(len(compressed) > 0)
        
        # Vérifier la décompression
        decompressed = self.compressor.decompress(compressed)
        self.assertEqual(text, decompressed)
    
    def test_compress_unique_text(self):
        """Test la compression d'un texte sans répétition"""
        text = "ABCDEF"
        compressed = self.compressor.compress(text)
        decompressed = self.compressor.decompress(compressed)
        
        self.assertEqual(text, decompressed)
    
    def test_decompress_empty_data(self):
        """Test la décompression de données vides"""
        decompressed = self.compressor.decompress([])
        self.assertEqual(decompressed, "")
    
    def test_compression_rate_calculation(self):
        """Test le calcul du taux de compression"""
        # Texte répétitif devrait avoir un bon taux
        text = "ABABABA" * 10
        compressed = self.compressor.compress(text)
        rate = self.compressor.calculate_compression_rate(text, compressed)
        
        self.assertIsInstance(rate, float)
        self.assertTrue(0 <= rate <= 100)
    
    def test_compression_rate_empty(self):
        """Test du taux de compression avec texte vide"""
        rate = self.compressor.calculate_compression_rate("", [])
        self.assertEqual(rate, 0)
    
    def test_save_and_load_compressed_data(self):
        """Test la sauvegarde et le chargement des données compressées"""
        # Créer un fichier temporaire
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_filename = f.name
        
        try:
            # Données de test
            test_data = [65, 66, 256, 257]
            
            # Sauvegarder
            success = self.compressor.save_compressed_data(test_data, temp_filename)
            self.assertTrue(success)
            
            # Vérifier que le fichier existe
            self.assertTrue(os.path.exists(temp_filename))
            
            # Charger
            loaded_data = self.compressor.load_compressed_data(temp_filename)
            self.assertEqual(loaded_data, test_data)
            
        finally:
            # Nettoyer
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_compression_analysis(self):
        """Test l'analyse de compression"""
        text = "TEST" * 5
        compressed = self.compressor.compress(text)
        
        # L'analyse ne devrait pas lever d'exception
        try:
            rate = self.compressor.analyze_compression(text, compressed)
            self.assertIsInstance(rate, float)
        except Exception as e:
            self.fail(f"L'analyse a levé une exception: {e}")

class TestLZWAlgorithm(unittest.TestCase):
    """Tests spécifiques à l'algorithme LZW"""
    
    def test_lzw_known_sequence(self):
        """Test avec une séquence connue de LZW"""
        compressor = LZWCompressor()
        
        # Séquence classique "ABABABA"
        text = "ABABABA"
        compressed = compressor.compress(text)
        
        # La compression devrait être efficace
        self.assertLess(len(compressed), len(text))
        
        # Vérifier la reconstruction
        decompressed = compressor.decompress(compressed)
        self.assertEqual(text, decompressed)
    
    def test_lzw_dictionary_growth(self):
        """Test la croissance du dictionnaire pendant la compression"""
        compressor = LZWCompressor()
        initial_size = compressor.next_code
        
        text = "ABABABAABABABA"
        compressed = compressor.compress(text)
        
        # Le dictionnaire devrait avoir grandi
        self.assertGreater(compressor.next_code, initial_size)
        
        # Vérifier que tous les codes sont valides
        for code in compressed:
            self.assertIn(code, compressor.reverse_dictionary)
    
    def test_lzw_special_case(self):
        """Test le cas spécial de décompression LZW"""
        compressor = LZWCompressor()
        
        # Ce test vérifie le cas où un code n'est pas encore dans le dictionnaire
        # pendant la décompression (cas spécial de l'algorithme LZW)
        compressed = [65, 66, 256]  # "A", "B", "AB"
        
        decompressed = compressor.decompress(compressed)
        expected = "ABAB"
        
        self.assertEqual(decompressed, expected)

def run_compressor_tests():
    """Lance tous les tests du compresseur"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLZWCompressor)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLZWAlgorithm))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Afficher le résumé
    print(f"\n{'='*50}")
    print(f"TESTS COMPRESSEUR TERMINÉS")
    print(f"Réussis: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    print(f"{'='*50}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_compressor_tests()