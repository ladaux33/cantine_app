from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import datetime
import numpy as np
import pandas as pd
from commande import CommandeFournisseur
from envoie_email import envoie_email
from kivy.uix.tabbedpanel import TabbedPanel

# fichier d'enregistrement des commandes
fichier_melanie = "contact_melanie.txt"
fichier_bernat = "contact_bernat.txt"
fichier_cbs = "contact_cbs.txt"
temperature = "enregistrement_temperature.txt"

# import de la data
df = pd.read_excel("menus_cantine.ods")
df_menu_cantine = pd.read_excel("menus_cantine.ods")
df_fiche_technique = pd.read_excel("fiche_technique_plats.ods")
df_fiche_technique.set_index("plats", inplace=True)

commande_cbs = CommandeFournisseur(df, df_menu_cantine, df_fiche_technique)
commande_bernat = CommandeFournisseur(df, df_menu_cantine, df_fiche_technique)
commande_melanie = CommandeFournisseur(df, df_menu_cantine, df_fiche_technique)

with open(fichier_melanie, "w") as f:
    f.write("Bonjour Melanie, tu trouveras ci dessous la commande pour la suite \n"
            + str(commande_melanie.commande("melanie")))

with open(fichier_bernat, "w") as f:
    f.write("Bonjour, vous trouverez ci dessous la commande pour la suite \n"
            + str(commande_bernat.commande("bernat")))

with open(fichier_cbs, "w") as f:
    f.write("Bonjour, vous trouverez ci dessous la commande pour la suite \n"
            + str(commande_cbs.commande("cbs")))




class LayoutExempleTabs(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    with open(temperature, "r") as f:
        temperatures = f.read()
    enregistrement_temperature=StringProperty(temperatures)

    def commande_melanie_text(self, widget):
        with open(fichier_melanie, "r") as f:
            self.ids.button_commande_melanie.text = f.read()
        return self.ids.button_commande_melanie.text

    def commande_melanie_button(self,widget):
        envoie_email(self.ids.button_commande_melanie.text.encode("utf-8"))


    def commande_bernat_text(self, widget):
        with open(fichier_bernat, "r") as f:
            self.ids.button_commande_bernat.text = f.read()
        return self.ids.button_commande_bernat.text

    def commande_cbs_text(self, widget):
        with open(fichier_cbs, "r") as f:
            self.ids.button_commande_cbs.text = f.read()
        return self.ids.button_commande_cbs.text


class BoxLayoutApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def enregistrement_temperature(self, widget):
        chemin = "enregistrement_temperature.txt"
        with open(chemin, "r") as f:
            historique = f.read()
        with open(chemin, "w") as f:
            dat = datetime.date.today()
            f.write(f"{historique}\n,"
                    f"{dat},\n"
                    f"temperature chambre froide numero 1 : {str(int(self.ids.slider_chambre1.value))},\n"
                    f"temperature chambre froide numero 2 : {str(int(self.ids.slider_chambre2.value))},\n"
                    f"temperature chambre froide numero 3 : {str(int(self.ids.slider_chambre3.value))},\n"
                    f"temperature chambre froide numero 4 : {str(int(self.ids.slider_chambre4.value))},\n"
                    f"temperature chambre froide numero 5 : {str(int(self.ids.slider_chambre5.value))},\n"
                    f"temperature chambre froide numero 6 : {str(int(self.ids.slider_chambre6.value))}")






class MainApp(App):
    pass


MainApp().run()
