"""Auteur: Ezerskis Andrius
   Matricule: 000542698
   Section: B1-INFO
   Jeu: Breakthrough
   """


def init_board(n):  # 1 = white, 2 = black
    """ Construit et renvoie la liste de listes qui représente le plateau de taille n × n de départ """

    board = []
    board[0:2] = [[2 for i in range(n)] for i in range(2)]
    board[2:n - 2] = [[0 for i in range(n)] for i in range(n - 3)]
    board[n - 2:n] = [[1 for i in range(n)] for i in range(2)]

    return board


def print_board(board):
    """ Affiche le plateau de jeu """

    espace = ""
    chiffre = longueur = len(board)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    b = "B"
    w = 'W'
    case_vide = "."
    lettre = ""
    separateur = "|"
    if len(board) < 10:  # si le n rentré est inférieur à 10
        print(espace, espace, espace, espace, espace, end="")  # espaces du début avant les tirets

        for i in range(len(board)):  # imprimer les tirets
            print(espace, "—", end="")
        print(espace, end=" ")
        print()
        for elem in board:
            for num in elem:  # détermine la lettre (ou le .) qu'il faut mettre dans chaque emplacement
                for i in range(longueur):
                    if elem[num] == 2:  # si black
                        lettre = b
                    elif elem[num] == 0:  # si case vide
                        lettre = case_vide
                    else:  # si white
                        lettre = w

            print(espace, chiffre, separateur, end="")  # imprime les chiffres déterminant chaque ligne
            chiffre -= 1
            for i in range(longueur):  # imprime la lettre déterminée plus haut sur l'échiquier
                print(espace, lettre, end="")
            print(espace, separateur)  # imprime le séparateur de fin

        print(espace, espace, espace, espace, espace, end="")  # espaces avant les tirets
        for i in range(len(board)):  # imprime les tirets en bas
            print(espace, "—", end="")
        print(espace, end=" ")

        print()
        print(espace, espace, espace, espace, espace, end="")
        for i in range(longueur):  # imprime les lettres de l'alphabet désignant les colonnes
            print(espace, alphabet[i], end="")
        print(espace, end=" ")

        print()

    elif 9 < len(board) < 26:  # si le n rentré est égal à 10 ou plus, il faut gérer les décalages causés par les nombres à 2 chiffres
        print(espace, espace, espace, espace, espace, end="")  # espaces du début avant les tirets

        for i in range(len(board)):  # imprimer les tirets
            print(espace, "—", end="")
        print(espace, end=" ")
        print()

        for elem in board:
            for num in elem:  # détermine la lettre (ou le .) qu'il faut mettre dans chaque emplacement
                for i in range(longueur):
                    if elem[num] == 2:
                        lettre = b
                    elif elem[num] == 0:
                        lettre = case_vide
                    else:
                        lettre = w
            if chiffre > 9:
                print(chiffre, separateur,
                      end="")  # imprime les chiffres déterminant chaque ligne (ici pour les nombres à 2 chiffres)
                chiffre -= 1
            else:
                print(espace, espace, end="")
                print(chiffre, separateur, end="")  # imprime les chiffres déterminant chaque ligne (chiffres)
                chiffre -= 1

            for i in range(longueur):  # imprime la lettre déterminée plus haut sur l'échiquier (B, W ou .)
                print(espace, lettre, end="")
            print(espace, separateur)
        print(espace, espace, espace, espace, espace, end="")
        for i in range(len(board)):  # imprime les tirets en bas
            print(espace, "—", end="")
        print(espace, end=" ")

        print()

        print(espace, espace, espace, espace, espace, end="")
        for i in range(longueur):  # imprime les lettres de l'alphabet désignant les colonnes
            print(espace, alphabet[i], end="")
        print(espace, end="")
        print("")

print_board(init_board(12))

def winner(board):  # 1 = white, 2 = black
    """ Étant donné le plateau de jeu board, vérifie si l’un des deux joueurs a gagné. Renvoie 1
si le joueur blanc a gagné ; 2 si le joueur noir a gagné ; None si la partie n’est pas encore
terminée """
    n = len(board)
    if 1 in board[0]:
        return 1
    elif 2 in board[n-1]:
        return 2


def is_in_board(n, pos):
    """ Renvoie True si la position pos est valide pour un plateau de taille n × n ; renvoie False
sinon."""
    if (pos[0] < 0) or (pos[0] > (n-1)) or (pos[1] < 0) or (pos[1] > (n-1)):
        return False
    else:
        return True


def input_move():
    """ Demande au joueur d'entrer un coup et continue de lui demander tant que le coup n'est pas valide """
    global coup_joueur
    valeur_sentinelle = False
    pacman = ">"
    while not valeur_sentinelle:
        coup_joueur = input("Entrez un mouvement: ")  # exemple : a6>b5
        if coup_joueur.islower():
            if len(coup_joueur) == 5:  # si 1 seul chiffre après chaque lettre
                if coup_joueur[0].isalpha():
                    if coup_joueur[1].isnumeric():
                        if coup_joueur[2] == pacman:
                            if coup_joueur[3].isalpha():
                                if coup_joueur[4].isnumeric():
                                    valeur_sentinelle = True
            elif len(coup_joueur) == 6:  # si 2 chiffres après une des lettres ou après les deux
                if coup_joueur[0].isalpha():  # pyramide de if
                    if coup_joueur[1].isnumeric():
                        if coup_joueur[2].isnumeric():  # exemple: a14>b5
                            if coup_joueur[3] == pacman:
                                if coup_joueur[4].isalpha():
                                    if coup_joueur[5].isnumeric():
                                        valeur_sentinelle = True
                        elif coup_joueur[2] == pacman:  # exemple: a5>b14
                            if coup_joueur[3].isalpha():
                                if coup_joueur[4].isnumeric():
                                    if coup_joueur[5].isnumeric():
                                        valeur_sentinelle = True

            elif len(coup_joueur) == 7:  # exemple: a15>b16 --> si 2 chiffres après chaque lettre
                if coup_joueur[0].isalpha():
                    if coup_joueur[1].isnumeric():
                        if coup_joueur[2].isnumeric():
                            if coup_joueur[3] == pacman:
                                if coup_joueur[4].isalpha():
                                    if coup_joueur[5].isnumeric():
                                        if coup_joueur[6].isnumeric():
                                            valeur_sentinelle = True
            elif len(coup_joueur) > 7:
                valeur_sentinelle = False

    return coup_joueur


def extract_pos(n, str_pos):
    """ Traduit une position str_pos donnée en format notation échecs (ex : ’b5’) en la paire
d’indices (i, j) correspondante. Le paramètre n correspond à la taille du plateau """
    # on nous donne une case (ex: b4) et on doit transformer la case en un tuple
    # axe x et y inversés --> b4 en position (3, 1)
    alphab = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
              'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
              'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    # tup = (0, 0)  # initialise le tuple
    tup = [0, 0]
    for key in alphab.keys():  # clés du dico
        for i in str_pos:  # chaque élément du string
            if i == key:  # si l'élément du string correspond à la lettre dans le dico
                tup[0] = n - int(str_pos[1])
                tup[1] = alphab.get(key)  # tup[1] est le chiffre correspondant à la lettre du dico

    return tuple(tup)


def check_move(board, player, str_move):  # 1 = white, 2 = black, ex: str_move = "a7>b2"
    """ Prend en entrée le plateau de jeu et un mouvement proposé par l’un des joueurs """
    pacman = ">"
    n = len(board)
    pos_init = 0
    pos_fin = 0
    if str_move[2] == pacman:
        pos_init = extract_pos(n, str_move[0:2])  # (int, int)
        pos_fin = extract_pos(n, str_move[3:])  # (int, int)
    elif str_move[3] == pacman:
        pos_init = extract_pos(n, str_move[0:3])  # (int, int)
        pos_fin = extract_pos(n, str_move[4:])  # (int, int)

    if is_in_board(n, pos_init) and is_in_board(n, pos_fin):
        if player == 1:  # player white
            if board[pos_init[0]][pos_init[1]] == 1:
                if board[pos_fin[0]][pos_fin[1]] == 0 or board[pos_fin[0]][pos_fin[1]] == 2:
                    if pos_fin[1] == (pos_init[1] - 1) or pos_fin[1] == (pos_init[1] + 1):
                        if pos_fin[0] == (pos_init[0] - 1):
                            if board[pos_fin[0]][pos_fin[1]] == 0:
                                return True
                            if board[pos_fin[0]][pos_fin[1]] == 2:
                                return True
                    if pos_fin[1] == (pos_init[1]):
                        if pos_fin[0] == (pos_init[0] - 1):
                            if board[pos_fin[0]][pos_fin[1]] == 0:
                                return True

        if player == 2:  # player black
            if board[pos_init[0]][pos_init[1]] == 2:
                if board[pos_fin[0]][pos_fin[1]] == 0 or board[pos_fin[0]][pos_fin[1]] == 1:
                    if pos_fin[1] == (pos_init[1] + 1) or pos_fin[1] == (pos_init[1] - 1):
                        if pos_fin[0] == (pos_init[0] + 1):
                            if board[pos_fin[0]][pos_fin[1]] == 0:
                                return True
                            if board[pos_fin[0]][pos_fin[1]] == 1:
                                return True
                    if pos_fin[1] == pos_init[1]:
                        if pos_fin[0] == (pos_init[0] + 1):
                            if board[pos_fin[0]][pos_fin[1]] == 0:
                                return True

        return False


def play_move(board, move, player):
    """ Modifie le plateau de jeu board en effectuant un coup donné pour un joueur donné."""
    board[move[1][0]][move[1][1]] = player
    board[move[0][0]][move[0][1]] = 0
    return board


def main(n):
    """ La fonction principale du programme. Elle contient d’abord une phase d’initialisation du
plateau de jeu, de taille n × n, puis une boucle qui permet successivement aux joueurs
de proposer des coups, jusqu’à ce que la condition de victoire soit satisfaite pour l’un des
joueurs et que la partie s’arrête """
    leboard = init_board(n)
    print_board(leboard)
    while winner(leboard) is None:
        joueur = 1
        print("Joueur 1")
        input_joueur1 = input_move()
        while not check_move(leboard, joueur, input_joueur1):
            print("Mouvement incorrect, réessayez.")
            input_joueur1 = input_move()
        input_split1 = input_joueur1.split(">")
        print(input_split1)
        pos_init_joueur1 = extract_pos(n, input_split1[0])  # tuple(int,int)
        pos_fin_joueur1 = extract_pos(n, input_split1[1])
        play_move(leboard, (pos_init_joueur1, pos_fin_joueur1), joueur)
        print_board(leboard)
        if winner(leboard) is None:
            joueur = 2
            print("Joueur 2")
            input_joueur2 = input_move()
            while not check_move(leboard, joueur, input_joueur2):
                print("Mouvement incorrect, réessayez.")
                input_joueur2 = input_move()
            input_split2 = input_joueur2.split(">")
            pos_init_joueur2 = extract_pos(n, input_split2[0])
            pos_fin_joueur2 = extract_pos(n, input_split2[1])
            play_move(leboard, (pos_init_joueur2, pos_fin_joueur2), joueur)
            print_board(leboard)
        winner(leboard)

if __name__ == "__main__":
    n = int(input())
    main(n)