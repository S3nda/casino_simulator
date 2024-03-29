#   pour revenir au menu :
from main import menu_principal

#   fonctions primaires du module roulette
from modules import jeu, data, GUI

#   pour les couleurs
from colorama import Fore, Style


def session_solo():
    """Fonction principale du mode solo"""
    nom_joueur = jeu.nom('solo')
    joueur = Joueur(nom_joueur)
    joueur.entree()
    print(f'{Fore.YELLOW}{nom_joueur}{Style.RESET_ALL}... Enchanté !')
    GUI.attend()
    joueur.mise_max()
    while True:
        joueur.paris()  # on demande au joueur de parier
        result_roulette = jeu.result_roulette()
        joueur.resultats(result_roulette)
        if not jeu.continuer(joueur.nom, joueur.argent, 'solo'):
            break
    data.crea_dico_dans_csv(joueur.stats(), )
    GUI.attend()
    menu_principal()


def session_multi():
    """Fonction principale du mode multi"""
    joueurs = [Joueur(jeu.nom(index_jr)) for index_jr in range(1, jeu.nbr_joueur() + 1)]  # liste des joueurs
    joueurs_temp = joueurs
    for joueur in joueurs:  # on initialise les joueurs
        joueur.entree()
        joueur.mise_max()
    while joueurs:  # tant qu'il y a des joueurs, on continue la partie
        for joueur in joueurs:
            joueur.paris()
        result = jeu.result_roulette()
        for joueur in joueurs:
            joueur.resultats(result)
        joueurs = [joueur for joueur in joueurs if jeu.continuer(joueur.nom, joueur.argent, 'multi')]
    for joueur in joueurs_temp:  # on sauvegarde les stats de tous les joueurs
        data.crea_dico_dans_csv(joueur.stats())
    print("il n'y a à présent plus personne...")
    GUI.attend(2)
    print("à la prochaine !")
    GUI.attend()
    menu_principal()


def regles():
    jeu.regles()


class Joueur:
    def __init__(self, nom):
        stats = data.search_nom(nom)  # on cherche le joueur dans le csv
        if stats is not None:  # si on trouve le joueur dans le csv, on lui attribue ses stats
            self.nom, self.num_entree, self.nbr_tour_total, self.argent_total, self.gain_total, self.premiere_entree = stats.values()
        else:  # si on ne trouve pas le joueur, on lui attribue des stats par défaut
            self.nom, self.num_entree, self.nbr_tour_total, self.argent_total, self.gain_total, self.premiere_entree = data.default().values()
            self.nom = nom
        self.mise_tour = 0
        self.argent_debut = None
        self.argent = None
        self.resultat = None
        self.pari = {}
        self.gain_tour = None
        self.re_parier = True

    def entree(self):
        self.num_entree += 1
        pass

    def mise_max(self):
        self.argent = jeu.mise_maximale(self.nom)
        pass

    def paris(self):
        self.argent_debut = self.argent  # on sauvegarde l'argent du joueur au début du tour (utilisé à la l.94)
        self.nbr_tour_total += 1
        self.re_parier = True
        while self.re_parier:  # tant que le joueur veut parier, on continue
            self.pari, self.argent = jeu.pari_choix(self.pari, self.argent, self.nom)
            self.re_parier = jeu.re_parier(self.argent)
        jeu.resume_pari(self.pari)  # on affiche le résumé des paris

    def resultats(self, resultat):
        for choix in self.pari:  # pour chaque pari, on va changer l'argent du joueur
            # via la fonction passage_a_la_caisse et du resultat de la roulette
            self.argent_total += self.pari[choix]  # Pour les stats
            self.argent = jeu.passage_a_la_caisse(self.pari[choix], resultat, self.argent, choix, self.nom)
            GUI.attend(0.5)
        self.pari = {}  # on réinitialise les paris pour pouvoir en refaire au prochain tour
        self.gain_tour = self.argent - self.argent_debut  # on calcule le gain du tour grâce à
        # l'argent du début et de la fin du tour
        self.gain_total += self.gain_tour
        GUI.attend()

    def stats(self):
        """Retourne un dictionnaire contenant les stats du joueur"""
        return {
            'nom': self.nom,
            'num_entree': self.num_entree,
            'nbr_tours_total': self.nbr_tour_total,
            'argent_total': self.argent_total,
            'gain_total': self.gain_total,
            'premiere_entree': self.premiere_entree
        }
