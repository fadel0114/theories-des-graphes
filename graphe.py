# --- Imports ---
import networkx as nx
import matplotlib.pyplot as plt

# --- Création du graphe ---
G = nx.DiGraph()

# Nœuds du graphe
nodes = [
    "GESTIONNAIRE",
    "CLIENT:pharmacien 1", "CLIENT:pharmacien 2", "CLIENT:pharmacien 3",
    "VILLE:bobo dioulasso", "VILLE:kaya", "VILLE:ouagadougou", "VILLE:koudougou",
    "PHARMATIE:pharmacie A", "PHARMATIE:pharmacie B", "PHARMATIE:pharmacie C",
    "entrepot pharmaceutique", "produit pharmaceutique",
    "EXPEDITEUR:Expediteur1", "EXPEDITEUR:Expediteur2", "EXPEDITEUR:Expediteur3"
]
G.add_nodes_from(nodes)

# Arêtes avec leurs relations
edges = [
    ("CLIENT:pharmacien 1", "VILLE:bobo dioulasso", "vit à"),
    ("CLIENT:pharmacien 3", "VILLE:kaya", "vit à"),
    ("CLIENT:pharmacien 2", "VILLE:koudougou", "vit à"),
    ("VILLE:bobo dioulasso", "PHARMATIE:pharmacie A", "est situé"),
    ("VILLE:kaya", "PHARMATIE:pharmacie C", "est situé"),
    ("VILLE:ouagadougou", "PHARMATIE:pharmacie B", "est situé"),
    ("GESTIONNAIRE", "CLIENT:pharmacien 1", "COMMANDE"),
    ("GESTIONNAIRE", "CLIENT:pharmacien 3", "COMMANDE"),
    ("GESTIONNAIRE", "CLIENT:pharmatien 2", "COMMANDE"),  # 🐞 Attention à "pharmatien" ici
    ("GESTIONNAIRE", "entrepot pharmaceutique", "TRANSMET LA COMMANDE"),
    ("entrepot pharmaceutique", "produit pharmaceutique", "stocke"),
    ("entrepot pharmaceutique", "EXPEDITEUR:Expediteur1", "donne la commande"),
    ("entrepot pharmaceutique", "EXPEDITEUR:Expediteur2", "donne la commande"),
    ("entrepot pharmaceutique", "EXPEDITEUR:Expediteur3", "donne la commande"),
    ("EXPEDITEUR:Expediteur1", "VILLE:kaya", "livre les produits"),
    ("EXPEDITEUR:Expediteur2", "VILLE:koudougou", "livre les produits"),
    ("EXPEDITEUR:Expediteur3", "VILLE:bobo dioulasso", "livre les produits")
]
for source, target, label in edges:
    G.add_edge(source, target, label=label)

# --- Interface interactive ---
def explorer_graphe():
    print("📋 Entités disponibles dans le graphe :\n")
    for i, entite in enumerate(G.nodes):
        print(f"{i+1}. {entite}")
    
    try:
        choix = int(input("\n👉 Choisis le numéro de l'entité à explorer : "))
        entite_choisie = list(G.nodes)[choix - 1]
    except (ValueError, IndexError):
        print("❌ Choix invalide. Réessaye avec un numéro valide.")
        return

    print(f"\n🔎 Exploration de l'entité : {entite_choisie}")
    print("\n➡️ Relations sortantes :")
    for succ in G.successors(entite_choisie):
        label = G.edges[entite_choisie, succ]['label']
        print(f" - {entite_choisie} --[{label}]--> {succ}")

    print("\n⬅️ Relations entrantes :")
    for pred in G.predecessors(entite_choisie):
        label = G.edges[pred, entite_choisie]['label']
        print(f" - {pred} --[{label}]--> {entite_choisie}")
    print("\n" + "-"*40 + "\n")

# --- Visualisation du graphe ---
def afficher_graphe():
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'label')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="#AEEEEE",
            font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("🕸️ Visualisation du graphe pharmaceutique")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# --- Boucle principale ---
while True:
    explorer_graphe()
    continuer = input("🔁 Voulez-vous explorer une autre entité ? (oui/non/afficher) : ")
    if continuer.lower() == "afficher":
        afficher_graphe()
    elif continuer.lower() != "oui":
        print("🫡 Merci pour l'exploration ! À bientôt, ")
        break
