import FreeSimpleGUI as sg
import fonctions as fn


taille= (sg.popup("Sélectionnez une taille de cadrillage.", custom_text=("20*20 (performances)", "40*40 (fonctionalités)")))
if taille == "20*20 (performances)":
    largeur, hauteur = (20, 20)
elif taille == "40*40 (fonctionalités)":
    largeur, hauteur = (40, 40)
else: #par défaut, par exemple si l'utilisateur ferme la popup
    largeur, hauteur = (32, 32)
generation=0

layout= [
        [sg.Text('Génération : 0', k='gen')], #k = key → permet de se réferer à l'élément
        [sg.Button('+1000'),
         sg.Button('+100'),
         sg.Button('+1'),
         sg.Button('Retour à Zéro')],
        [sg.Graph((700, 700), (0, 0), (largeur, hauteur), background_color='grey', k='g')],
        [sg.Button('Clignotant'),
         sg.Button('Planeur')],
        [sg.Button('Préconfiguration 1'),
         sg.Button('Canon à planeurs'),
         sg.Button('Galaxie de Kok')],
        ]

window= sg.Window('Jeu de la vie - Marius', layout)
window.finalize()
graph= window['g']

cellules= fn.grid(largeur, hauteur)
window.refresh()
figures= []


def oscillateur():
    """Génère un Clignotant au centre de la grille"""
    for i in range(int(hauteur/2-1), int(hauteur/2+2)):
            cellules[(int(largeur/2), i)]['color']= 'white'
            figures.append(graph.draw_rectangle(cellules[(int(largeur/2), i)]['top_left'], cellules[(int(largeur/2), i)]['bottom_right'], 'white'))

def planeur_topleft():
        """Génère un Planeur dans le coin supérieur gauche de la grille"""
        figures.append(graph.draw_rectangle((0, hauteur), (1, hauteur-1), 'white'))
        cellules[(0, hauteur-1)]['color']= 'white'
        figures.append(graph.draw_rectangle((2, hauteur), (3, hauteur-1), 'white'))
        cellules[(2, hauteur-1)]['color']= 'white'
        figures.append(graph.draw_rectangle((1, hauteur-1), (2, hauteur-2), 'white'))
        cellules[(1, hauteur-2)]['color']= 'white'
        figures.append(graph.draw_rectangle((2, hauteur-1), (3, hauteur-2), 'white'))
        cellules[(2, hauteur-2)]['color']= 'white'
        figures.append(graph.draw_rectangle((1, hauteur-2), (2, hauteur-3), 'white'))
        cellules[(1, hauteur-3)]['color']= 'white'

def canon_planeur():
    """Génère un Canon à Planeurs dans le coin inférieur gauche de la grille"""
    base_y = int(hauteur/10)

    coords = [
        (1, base_y + 4), (1, base_y + 5),
        (2, base_y + 4), (2, base_y + 5),
        (11, base_y + 4), (11, base_y + 5), (11, base_y + 6),
        (12, base_y + 3), (12, base_y + 7),
        (13, base_y + 2), (13, base_y + 8),
        (14, base_y + 2), (14, base_y + 8),
        (15, base_y + 5),
        (16, base_y + 3), (16, base_y + 7),
        (17, base_y + 4), (17, base_y + 5), (17, base_y + 6),
        (18, base_y + 5),
        (21, base_y + 2), (21, base_y + 3), (21, base_y + 4),
        (22, base_y + 2), (22, base_y + 3), (22, base_y + 4),
        (23, base_y + 1), (23, base_y + 5),
        (25, base_y + 0), (25, base_y + 1), (25, base_y + 5), (25, base_y + 6),
        (35, base_y + 2), (35, base_y + 3),
        (36, base_y + 2), (36, base_y + 3),
    ]

    for x, y in coords:
        figures.append(graph.draw_rectangle((x, y + 1), (x + 1, y), 'white'))
        cellules[(x, y)]['color'] = 'white'

def galaxie():
    """Génère une Galaxie de Kok au centre de la grille"""
    base_x = int(largeur/2)
    base_y = int(hauteur/2)

    coords = [
        (base_x-4, base_y+4), (base_x-4, base_y+3), (base_x-4, base_y+2), (base_x-4, base_y+1), (base_x-4, base_y), (base_x-4, base_y-1), (base_x-4, base_y-3), (base_x-4, base_y-4),
        (base_x-3, base_y+4), (base_x-3, base_y+3), (base_x-3, base_y+2), (base_x-3, base_y+1), (base_x-3, base_y), (base_x-3, base_y-1), (base_x-3, base_y-3), (base_x-3, base_y-4),
        (base_x-2, base_y-3), (base_x-2, base_y-4),
        (base_x-1, base_y+4), (base_x-1, base_y+3), (base_x-1, base_y-3), (base_x-1, base_y-4),
        (base_x, base_y+4), (base_x, base_y+3), (base_x, base_y-3), (base_x, base_y-4),
        (base_x+1, base_y+4), (base_x+1, base_y+3), (base_x+1, base_y-3), (base_x+1, base_y-4),
        (base_x+2, base_y+3), (base_x+2, base_y+4),
        (base_x+3, base_y+4), (base_x+3, base_y+3), (base_x+3, base_y+1), (base_x+3, base_y), (base_x+3, base_y-1), (base_x+3, base_y-2), (base_x+3, base_y-3), (base_x+3, base_y-4),
        (base_x+4, base_y+4), (base_x+4, base_y+3), (base_x+4, base_y+1), (base_x+4, base_y), (base_x+4, base_y-1), (base_x+4, base_y-2), (base_x+4, base_y-3), (base_x+4, base_y-4),
    ]

    for x, y in coords:
        figures.append(graph.draw_rectangle((x, y + 1), (x + 1, y), 'white'))
        cellules[(x, y)]['color'] = 'white'

def ajouter_gen(nombre):
    """Réalise les calculs de la prochaine génération de cellules et met à jour la grile en adéquation"""
    global cellules, generation, figures
    for i in range(nombre):
        cellules, figures= fn.next_gen(cellules, fn.living_and_neighbors(cellules), figures)

        generation+=1
        window['gen'].update(f'Génération : {generation}')

def clear_map():
    """Tue toutes les cellules et met à jour la grille en adéquation"""
    global generation, cellules
    generation=0
    for x in range(largeur):
        for y in range(hauteur):
            cellules[(x, y)]['color']= cellules[(x, y)]['background']
            graph.draw_rectangle(cellules[(x, y)]['top_left'], cellules[(x, y)]['bottom_right'], fill_color=cellules[(x, y)]['background'])


while True:
    event, values= window.read()

    if event== sg.WIN_CLOSED:
        break


    if event == '+1000':
        ajouter_gen(1000)

    if event == '+100':
        ajouter_gen(100)

    if event == '+1':
        ajouter_gen(1)

    if event == 'Retour à Zéro':
        clear_map()

    if event == 'Clignotant':
        oscillateur()

    if event == 'Planeur':
        planeur_topleft()


    if event == 'Préconfiguration 1':
        oscillateur()
        ajouter_gen(1)
        planeur_topleft()

    if event == 'Canon à planeurs':
        if largeur<38 or hauteur<38:
            sg.popup("La taille du cadrillage n'est pas suffisante. (< 38)", title="Taille insuffisante")
        else:
            canon_planeur()

    if event == 'Galaxie de Kok':
        if largeur<18 or hauteur<18:
            sg.popup("La taille du cadrillage n'est pas suffisante. (< 18)", title="Taille insuffisante")
        else:
            galaxie()