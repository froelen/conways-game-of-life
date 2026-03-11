import affichage as af



def next_gen(cellules, calculees, figures):
    """Utilise les fonctions birth() et death() pour déterminer
    les naissances et morts pour la prochaine génération
    et demande à update_graph() de mettre à jour la grille en adéquation"""
    births = birth(calculees, cellules)
    deaths = death(cellules, store_living(cellules))
    cellules = update_graph(births + deaths, cellules, figures)
    
    return cellules, figures


def grid(largeur, hauteur):
    """Cadrille l'élément Graph de la fenêtre et créée une cellule (un dictionnaire) pour la case correspondante"""
    canva = af.graph
    cellules = {}

    for x in range(-1, largeur + 1):
        for y in range(-1, hauteur + 1):
            if x % 2 == 0 and y % 2 == 0 or x % 2 != 0 and y % 2 != 0:
                color = '#0A0A0A'
            else:
                color = '#141414'

            is_side = x in [-1, largeur] or y in [-1, hauteur]
            case = {
                'top_left': (x, y + 1),
                'bottom_right': (x + 1, y),
                'coordinates': (x, y),
                'color': color,
                'background': color,
                'isOnSide': is_side
            }

            cellules[(x, y)] = case
            canva.draw_rectangle(case['top_left'], case['bottom_right'], fill_color=color)

    af.window.refresh()
    return cellules

def birth(calculees, cellules):
    """Fait changer la couleur des cellules de noir à blanc si elles ont 3 voisines vivantes
    Renvoie une liste contenant toutes les nouvelles cellules"""
    births = []

    for cellule in calculees:
        if not cellule['isOnSide'] and cellule['color'] != 'white':
            voisines = neighborhood(cellules, cellule)
            voisines_vivantes = sum(1 for v in voisines if v['color'] == 'white')

            if voisines_vivantes == 3:
                new_cell = cellule.copy()
                new_cell['color'] = 'white'
                births.append(new_cell)

    return births

def death(cellules, vivantes):
    """Fait changer la couleur des cellules de blanc à noir si elles n'ont pas 2 ou 3 voisines
    Renvoie une liste contenant toutes les cellules tuées"""
    deaths = []

    for vivante in vivantes:
        voisines = neighborhood(cellules, vivante)
        if sum(1 for v in voisines if v['color'] == 'white') not in [2, 3]:
            dead_cell = vivante.copy()
            dead_cell['color'] = dead_cell['background']
            deaths.append(dead_cell)

    return deaths


def update_graph(modified_cells, cellules, figures):
    """Supprime tous les élements de la grille et redessine toutes les cellules vivantes"""
    canva = af.graph
    window = af.window

    for figure in figures:
        canva.delete_figure(figure) #Supprime toutes les cellules
    figures.clear()

    for modified_cell in modified_cells:
        coords = modified_cell['coordinates']
        cellules[coords]['color'] = modified_cell['color']
    
    for cell in cellules.values():
        if cell['color'] == 'white':
            figure = canva.draw_rectangle(cell['top_left'], cell['bottom_right'], fill_color='white')
            figures.append(figure)

    window.refresh()
    return cellules

def store_living(cellules):
    """Renvoie une liste contenant toutes les cellules vivantes"""
    return [cell for cell in cellules.values() if cell['color'] == 'white']

def neighborhood(cellules, cell):
    """Renvoie une liste contenant les 8 voisine d'une cellule donnée"""
    neighbors = []
    x, y = cell['coordinates']

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) != (0, 0):
                nx, ny = x + dx, y + dy
                if (nx, ny) in cellules:
                    neighbors.append(cellules[(nx, ny)])

    return neighbors

def living_and_neighbors(cellules):
    """Renvoie une liste de toutes les cellules vivantes et leurs voisines"""
    livneigh = {}

    for cell in cellules.values():
        if cell['color'] == 'white':
            livneigh[cell['coordinates']] = cell
            for neighbor in neighborhood(cellules, cell):
                if neighbor['coordinates'] not in livneigh:
                    livneigh[neighbor['coordinates']] = neighbor

    return livneigh.values()