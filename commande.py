import pandas as pd



class CommandeFournisseur():
    def __init__(self,df,df_menu_cantine,df_fiche_technique):
        # test sur une partie du menu
        self.liste_entre = df_menu_cantine["entrée"][:40]
        self.liste_entre = [item for item in self.liste_entre if not(pd.isnull(item)) == True]
        self.liste_plats = df_menu_cantine["plats"][:40]
        self.liste_plats = [item for item in self.liste_plats if not(pd.isnull(item)) == True]
        self.liste_garniture = df_menu_cantine["garniture"][:40]
        self.liste_garniture = [item for item in self.liste_garniture if not(pd.isnull(item)) == True]

        # 1 tableau avec toutes les entrées
        self.liste_commande_entre = df_fiche_technique.loc[self.liste_entre]
        # 1 tableau avec tous les plats
        self.liste_commande_plats= df_fiche_technique.loc[self.liste_plats]
        # 1 tableau avec toutes les garnitures
        self.liste_commande_garniture= df_fiche_technique.loc[self.liste_garniture]

        self.fournisseur=[self.liste_commande_garniture,
                          self.liste_commande_entre,
                          self.liste_commande_plats]
    def commande(self,a):
        commande=[]
        for item in self.fournisseur:
            for i in item[a]:
                commande.append(i)
        commande=[i for i in commande if not(pd.isnull(i)==True)]
        return commande






