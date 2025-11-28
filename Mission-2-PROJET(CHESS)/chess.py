"""
CHESS - Jeu d'échecs complet
Auteur : Chaima Mathlouthi
"""

class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "white"
        self.game_over = False
        self.score_white = 0
        self.score_black = 0
        self.move_history = []
        
        self.piece_values = {
            'P': 1, 'p': 1,    # Pions
            'N': 3, 'n': 3,    # Cavaliers  
            'B': 3, 'b': 3,    # Fous
            'R': 5, 'r': 5,    # Tours
            'Q': 9, 'q': 9,    # Dames
            'K': 0, 'k': 0     # Rois
        }
    
    def initialize_board(self):
        """Initialise le plateau d'échecs avec la position de départ"""
        # Notation : majuscule = blanc, minuscule = noir
        board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # Ligne 0 (noir)
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # Ligne 1
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],   # Ligne 2
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],   # Ligne 3
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],   # Ligne 4
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],   # Ligne 5
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Ligne 6 (blanc)
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']   # Ligne 7 (blanc)
        ]
        return board
    
    def display_board(self):
        """Affiche le plateau dans la console avec un formatage clair"""
        print("\n    a   b   c   d   e   f   g   h")
        print("  ┌───┬───┬───┬───┬───┬───┬───┬───┐")
        
        for i in range(8):
            print(f"{8-i} │", end="")
            for j in range(8):
                piece = self.board[i][j]
                if piece == ' ':
                    print("   │", end="")
                else:
                    print(f" {piece} │", end="")
            print(f" {8-i}")
            
            if i < 7:
                print("  ├───┼───┼───┼───┼───┼───┼───┼───┤")
        
        print("  └───┴───┴───┴───┴───┴───┴───┴───┘")
        print("    a   b   c   d   e   f   g   h")
    
    def notation_to_indices(self, notation):
        """Convertit la notation échecs (ex: 'e4') en indices tableau (ligne, colonne)"""
        if len(notation) != 2:
            return None, None
        
        colonne = ord(notation[0]) - ord('a')
        ligne = 8 - int(notation[1])
        

        if 0 <= ligne < 8 and 0 <= colonne < 8:
            return ligne, colonne
        return None, None
    
    def indices_to_notation(self, ligne, colonne):
        """Convertit les indices tableau en notation échecs"""
        if 0 <= ligne < 8 and 0 <= colonne < 8:
            lettre = chr(colonne + ord('a'))
            chiffre = 8 - ligne
            return f"{lettre}{chiffre}"
        return None
    
    def get_legal_moves(self, position):
        """Retourne tous les coups légaux pour une position donnée"""
        ligne, colonne = self.notation_to_indices(position)
        if ligne is None or colonne is None:
            return []
        
        piece = self.board[ligne][colonne]
        if piece == ' ':
            return []
        
        # Vérifier que la pièce appartient au bon joueur
        if (self.current_player == "white" and piece.islower()) or \
           (self.current_player == "black" and piece.isupper()):
            return []
        
        legal_moves = []
        piece_type = piece.lower()
        
        # Générer les coups selon le type de pièce
        if piece_type == 'p':  # Pion
            legal_moves = self.get_pawn_moves(ligne, colonne, piece)
        elif piece_type == 'r':  # Tour
            legal_moves = self.get_rook_moves(ligne, colonne)
        elif piece_type == 'n':  # Cavalier
            legal_moves = self.get_knight_moves(ligne, colonne)
        elif piece_type == 'b':  # Fou
            legal_moves = self.get_bishop_moves(ligne, colonne)
        elif piece_type == 'q':  # Dame
            legal_moves = self.get_queen_moves(ligne, colonne)
        elif piece_type == 'k':  # Roi
            legal_moves = self.get_king_moves(ligne, colonne)
        
        return legal_moves
    
    def get_pawn_moves(self, ligne, colonne, piece):
        """Génère les coups légaux pour un pion"""
        moves = []
        direction = -1 if piece.isupper() else 1  # Blanc: -1, Noir: +1

        new_ligne = ligne + direction
        if 0 <= new_ligne < 8 and self.board[new_ligne][colonne] == ' ':
            moves.append(self.indices_to_notation(new_ligne, colonne))
            

            start_row = 6 if piece.isupper() else 1
            if ligne == start_row and self.board[new_ligne + direction][colonne] == ' ':
                moves.append(self.indices_to_notation(new_ligne + direction, colonne))
        

        for offset in [-1, 1]:
            new_colonne = colonne + offset
            if 0 <= new_ligne < 8 and 0 <= new_colonne < 8:
                target = self.board[new_ligne][new_colonne]
                if target != ' ' and ((piece.isupper() and target.islower()) or 
                                    (piece.islower() and target.isupper())):
                    moves.append(self.indices_to_notation(new_ligne, new_colonne))
        
        return moves
    
    def get_rook_moves(self, ligne, colonne):
        """Génère les coups légaux pour une tour"""
        moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # droite, bas, gauche, haut
        
        for dx, dy in directions:
            for distance in range(1, 8):
                new_ligne = ligne + dx * distance
                new_colonne = colonne + dy * distance
                
                if not (0 <= new_ligne < 8 and 0 <= new_colonne < 8):
                    break
                
                target = self.board[new_ligne][new_colonne]
                if target == ' ':
                    moves.append(self.indices_to_notation(new_ligne, new_colonne))
                else:
                    piece = self.board[ligne][colonne]
                    if (piece.isupper() and target.islower()) or \
                       (piece.islower() and target.isupper()):
                        moves.append(self.indices_to_notation(new_ligne, new_colonne))
                    break
        return moves
    
    def get_knight_moves(self, ligne, colonne):
        """Génère les coups légaux pour un cavalier"""
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        piece = self.board[ligne][colonne]
        
        for dx, dy in knight_moves:
            new_ligne = ligne + dx
            new_colonne = colonne + dy
            
            if 0 <= new_ligne < 8 and 0 <= new_colonne < 8:
                target = self.board[new_ligne][new_colonne]
                if target == ' ' or (piece.isupper() and target.islower()) or \
                   (piece.islower() and target.isupper()):
                    moves.append(self.indices_to_notation(new_ligne, new_colonne))
        
        return moves
    
    def get_bishop_moves(self, ligne, colonne):
        """Génère les coups légaux pour un fou"""
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dx, dy in directions:
            for distance in range(1, 8):
                new_ligne = ligne + dx * distance
                new_colonne = colonne + dy * distance
                
                if not (0 <= new_ligne < 8 and 0 <= new_colonne < 8):
                    break
                
                target = self.board[new_ligne][new_colonne]
                if target == ' ':
                    moves.append(self.indices_to_notation(new_ligne, new_colonne))
                else:
                    piece = self.board[ligne][colonne]
                    if (piece.isupper() and target.islower()) or \
                       (piece.islower() and target.isupper()):
                        moves.append(self.indices_to_notation(new_ligne, new_colonne))
                    break
        return moves
    
    def get_queen_moves(self, ligne, colonne):
        """Génère les coups légaux pour une dame (tour + fou)"""
        return self.get_rook_moves(ligne, colonne) + self.get_bishop_moves(ligne, colonne)
    
    def get_king_moves(self, ligne, colonne):
        """Génère les coups légaux pour un roi"""
        moves = []
        king_moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        piece = self.board[ligne][colonne]
        
        for dx, dy in king_moves:
            new_ligne = ligne + dx
            new_colonne = colonne + dy
            
            if 0 <= new_ligne < 8 and 0 <= new_colonne < 8:
                target = self.board[new_ligne][new_colonne]
                if target == ' ' or (piece.isupper() and target.islower()) or \
                   (piece.islower() and target.isupper()):
                    moves.append(self.indices_to_notation(new_ligne, new_colonne))
        
        return moves
    
    def make_move(self, start, end):
        """Exécute un mouvement sur le plateau"""
        start_ligne, start_colonne = self.notation_to_indices(start)
        end_ligne, end_colonne = self.notation_to_indices(end)
        
        if start_ligne is None or end_ligne is None:
            return False, "Position invalide"
        

        legal_moves = self.get_legal_moves(start)
        if end not in legal_moves:
            return False, "Coup illégal"
        

        piece_moved = self.board[start_ligne][start_colonne]
        piece_captured = self.board[end_ligne][end_colonne]
        self.move_history.append(f"{start}→{end}")
        

        if piece_captured != ' ':
            value = self.piece_values.get(piece_captured, 0)
            if self.current_player == "white":
                self.score_white += value
            else:
                self.score_black += value
        

        self.board[end_ligne][end_colonne] = piece_moved
        self.board[start_ligne][start_colonne] = ' '
        

        self.current_player = "black" if self.current_player == "white" else "white"
        
        return True, "Coup exécuté avec succès"
    
    def display_game_info(self):
        """Affiche les informations de la partie"""
        print(f"\n=== TOUR DU JOUEUR {self.current_player.upper()} ===")
        print(f"Score - Blanc: {self.score_white} | Noir: {self.score_black}")
        if self.move_history:
            print(f"Dernier coup: {self.move_history[-1]}")
        print("=" * 40)

def main():
    """Fonction principale du jeu"""
    game = ChessGame()
    
    print("♟️" * 20)
    print("    JEU D'ÉCHECS ")
    print("♟️" * 20)
    print("\nInstructions:")
    print("- Entrez les coups en notation échecs (ex: 'e2 e4')")
    print("- 'coups e2' pour voir les coups légaux de la case e2")
    print("- 'score' pour voir les scores")
    print("- 'quit' pour quitter")
    print("- 'reset' pour recommencer")
    print("\n" + "=" * 50)
    
    while not game.game_over:
        game.display_board()
        game.display_game_info()
        
        user_input = input("\nEntrez votre commande: ").strip().lower()
        
        if user_input == 'quit':
            print("Merci d'avoir joué !")
            break
        
        elif user_input == 'score':
            print(f"\nSCORE ACTUEL:")
            print(f"Blanc: {game.score_white} points")
            print(f"Noir: {game.score_black} points")
            continue
        
        elif user_input == 'reset':
            game = ChessGame()
            print("\n🎮 Nouvelle partie !")
            continue
        
        elif user_input.startswith('coups '):
            position = user_input[6:].strip()
            legal_moves = game.get_legal_moves(position)
            if legal_moves:
                print(f"Coup légaux pour {position}: {', '.join(legal_moves)}")
            else:
                print(f"Aucun coup légal pour {position}")
            continue
        
        try:
            start, end = user_input.split()
            success, message = game.make_move(start, end)
            print(f"\n{'✅' if success else '❌'} {message}")
            
            if not success:
                print("💡 Astuce: Utilisez 'coups [position]' pour voir les coups possibles")
                
        except ValueError:
            print("❌ Format invalide. Utilisez: 'position_départ position_arrivée'")
        except Exception as e:
            print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()