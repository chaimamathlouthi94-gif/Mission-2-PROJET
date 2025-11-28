"""
Tests unitaires pour le jeu d'échecs
"""

import unittest
import sys
import os




sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from chess import ChessGame

class TestChess(unittest.TestCase):
    """Tests complets pour la classe ChessGame"""
    
    def setUp(self):
        """Initialisation avant chaque test"""
        self.game = ChessGame()
    
    def test_initial_board(self):
        """Test l'initialisation correcte du plateau"""
        # Vérifier les pièces noires
        self.assertEqual(self.game.board[0][0], 'r')  # Tour noire
        self.assertEqual(self.game.board[0][4], 'k')  # Roi noir
        
        # Vérifier les pièces blanches
        self.assertEqual(self.game.board[7][0], 'R')  # Tour blanche
        self.assertEqual(self.game.board[7][4], 'K')  # Roi blanc
        
        # Vérifier les cases vides
        for i in range(2, 6):
            for j in range(8):
                self.assertEqual(self.game.board[i][j], ' ')
    
    def test_notation_conversion(self):
        """Test la conversion notation échecs ↔ indices"""
        # Test de positions valides
        self.assertEqual(self.game.notation_to_indices('a1'), (7, 0))
        self.assertEqual(self.game.notation_to_indices('h8'), (0, 7))
        self.assertEqual(self.game.notation_to_indices('e4'), (4, 4))
        
        # Test de positions invalides
        self.assertEqual(self.game.notation_to_indices('i1'), (None, None))
        self.assertEqual(self.game.notation_to_indices('a9'), (None, None))
        
        # Test conversion inverse
        self.assertEqual(self.game.indices_to_notation(7, 0), 'a1')
        self.assertEqual(self.game.indices_to_notation(0, 7), 'h8')
        self.assertEqual(self.game.indices_to_notation(4, 4), 'e4')
    
    def test_pawn_moves_white(self):
        """Test les déplacements des pions blancs"""
        # Pion blanc en e2
        moves = self.game.get_legal_moves('e2')
        self.assertIn('e3', moves)
        self.assertIn('e4', moves)  # Premier coup double
        
        # Pion blanc ne peut pas reculer
        self.assertNotIn('e1', moves)
    
    def test_pawn_moves_black(self):
        """Test les déplacements des pions noirs"""
        # Changer de joueur pour tester les noirs
        self.game.current_player = "black"
        
        # Pion noir en e7
        moves = self.game.get_legal_moves('e7')
        self.assertIn('e6', moves)
        self.assertIn('e5', moves)  # Premier coup double
        
        # Pion noir ne peut pas reculer
        self.assertNotIn('e8', moves)
    
    def test_knight_moves(self):
        """Test les déplacements du cavalier"""
        # Cavalier blanc en g1
        moves = self.game.get_legal_moves('g1')
        self.assertIn('f3', moves)
        self.assertIn('h3', moves)
        
        # Positions invalides pour cavalier
        self.assertNotIn('g2', moves)
        self.assertNotIn('g3', moves)
    
    def test_illegal_moves(self):
        """Test le rejet des coups illégaux"""
        # Case vide
        moves = self.game.get_legal_moves('e4')
        self.assertEqual(moves, [])
        
        # Pièce adverse
        self.game.current_player = "black"
        moves = self.game.get_legal_moves('e2')  # Pion blanc
        self.assertEqual(moves, [])
    
    def test_move_execution(self):
        """Test l'exécution d'un coup valide"""
        # Déplacer pion blanc e2→e4
        success, message = self.game.make_move('e2', 'e4')
        self.assertTrue(success)
        self.assertEqual(message, "Coup exécuté avec succès")
        
        # Vérifier que le pion s'est déplacé
        self.assertEqual(self.game.board[4][4], 'P')  # e4
        self.assertEqual(self.game.board[6][4], ' ')  # e2 vide
        
        # Vérifier changement de joueur
        self.assertEqual(self.game.current_player, "black")
    
    def test_illegal_move_execution(self):
        """Test le rejet d'un coup invalide"""
        # Coup illégal : déplacement impossible
        success, message = self.game.make_move('e2', 'e5')  # Trop loin
        self.assertFalse(success)
        self.assertEqual(message, "Coup illégal")
    
    def test_score_calculation(self):
        """Test le calcul du score après une prise"""
        # Configuration pour une prise
        self.game.board[4][4] = 'p'  # Pion noir en e4
        self.game.board[6][4] = 'P'  # Pion blanc en e2
        
        # Prendre le pion noir
        success, message = self.game.make_move('e2', 'e4')
        self.assertTrue(success)
        
        # Vérifier le score
        self.assertEqual(self.game.score_white, 1)  # Pion = 1 point
    
    def test_move_history(self):
        """Test l'historique des coups"""
        # Exécuter quelques coups
        self.game.make_move('e2', 'e4')
        self.game.make_move('e7', 'e5')
        
        # Vérifier l'historique
        self.assertEqual(len(self.game.move_history), 2)
        self.assertIn('e2→e4', self.game.move_history)
        self.assertIn('e7→e5', self.game.move_history)

class TestChessIntegration(unittest.TestCase):
    """Tests d'intégration pour le jeu complet"""
    
    def test_complete_game_flow(self):
        """Test un flux complet de jeu"""
        game = ChessGame()
        
        # Coup 1: Blanc joue
        success, message = game.make_move('e2', 'e4')
        self.assertTrue(success)
        self.assertEqual(game.current_player, "black")
        
        # Coup 2: Noir joue
        success, message = game.make_move('e7', 'e5')
        self.assertTrue(success)
        self.assertEqual(game.current_player, "white")
        
        # Vérifier l'état final
        self.assertEqual(game.board[4][4], 'P')  # Pion blanc en e4
        self.assertEqual(game.board[3][4], 'p')  # Pion noir en e5

def run_tests():
    """Lance tous les tests"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChess)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestChessIntegration))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Afficher le résumé
    print(f"\n{'='*50}")
    print(f"TESTS TERMINÉS")
    print(f"Réussis: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    print(f"{'='*50}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_tests()