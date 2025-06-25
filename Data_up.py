import os
import string

class Data_up:
    def __init__(self):
        self.PATH = os.path.dirname(os.path.realpath(__file__))
        self.path_correcter()
        self.verif_dossier()

    def path_correcter(self) -> None:
        if os.getcwd() != self.PATH:
            os.chdir(self.PATH)
            print("Changement de répertoire")
        else:
            print("Répertoire déjà bon")

    def verif_dossier(self) -> None:
        if not os.path.exists("Data"):
            os.mkdir("Data") 

    def open_data(self, path:str) -> set[str]:
        try:
            with open(path, "r",encoding="utf-8") as file:
                data = file.read()
            data = self.mise_en_forme(data)
            if self.verif_data(data):
                data = data.split("\n")
                while "" in data:
                    data.remove("")
                return set(data)
        except:
            pass
        return set()
    
    def save_data_dict(self, data_dict: dict[int, list[str]]) -> None:
        for taille_mot, mots in data_dict.items():
            try:
                file = open(f"Data/mot{taille_mot}.txt", "r")
                data_mot = file.read().split("\n")
            except:
                data_mot = []
            with open(f"Data/mot{taille_mot}.txt", "a") as file:
                for mot in mots:
                    if mot not in data_mot:
                        file.write(mot + "\n")


    def save_data_list(self, data: list[str]) -> None:
        sorted_data = {len(mot): [] for mot in data}
        for mot in data:
            sorted_data[len(mot)].append(mot)
        self.save_data_dict(sorted_data)

    def save_data_set(self, data: set[str]) -> None:
        sorted_data = {len(mot): [] for mot in data}
        for mot in data:
            sorted_data[len(mot)].append(mot)
        self.save_data_dict(sorted_data)

    def save_data(self, data: list[str] | dict[int, list[str]] | set[str]) -> None:
        if isinstance(data, list):
            self.save_data_list(data)
        elif isinstance(data, dict):
            self.save_data_dict(data)
        elif isinstance(data, set):
            self.save_data_set(data)
        else:
            print("Type de data non reconnu dans save_data")

    def mise_en_forme(self, data: str) -> str:
        data = data.lower()
        # data = data.replace("-", " ")
        # data = data.replace("'", " ")
        data = data.replace(".", "")
        data = data.replace("!", "")
        data = data.replace(";", "")
        data = data.replace(":", "")
        data = data.replace("?", "")
        data = data.replace(",", "")
        data = data.replace("’", " ")
        data = data.replace("«", "")
        data = data.replace("»", "")
        data = data.replace("à", "a")
        data = data.replace("â", "a")
        data = data.replace("é", "e")
        data = data.replace("è", "e")
        data = data.replace("ê", "e")
        data = data.replace("ë", "e")
        data = data.replace("î", "i")
        data = data.replace("ï", "i")
        data = data.replace("ô", "o")
        data = data.replace("ö", "o")
        data = data.replace("ù", "u")
        data = data.replace("û", "u")
        data = data.replace("ü", "u")
        data = data.replace("ç", "c")
        data = data.replace("œ", "oe")
        data = data.replace("æ", "ae")
        data = data.replace(" ", "\n")
        data = data.replace("\n\n", "\n")
        return data
    
    def verif_data(self, data: str) -> bool:
        if len(data) != sum(map(data.count, list(string.ascii_lowercase+'\n\'-'))):
            return False
        return True

            

    def start(self):
        path = input("Entrez le chemin du fichier à importer: ")
        data = self.open_data(path)
        if data:
            self.save_data(data)
            print("Importation réussie")
        else:
            print("Erreur lors de l'importation")


if __name__ == "__main__":
    data_up = Data_up()
    data_up.start()