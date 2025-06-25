import os
from itertools import permutations
import string
import tkinter as tk
from tkinter import messagebox
import threading
import time


class Decodeur:
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
        if not os.path.exists("In"):
            os.mkdir("In")
        if not os.path.exists("Out"):
            os.mkdir("Out")
        

    def open_data(self, taille_mot: int) -> set[str]:
        try:
            with open(f"Data/mot{taille_mot}.txt", "r") as file:
                data = file.read()
            data = data.split("\n")
            while "" in data:
                data.remove("")
            return set(data)
        except:
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


    def save_data_list_or_set(self, data: list[str]|set[str]) -> None:
        sorted_data = {len(mot): [] for mot in data}
        for mot in data:
            sorted_data[len(mot)].append(mot)
        self.save_data_dict(sorted_data)

    
    def save_data(self, data: list[str] | dict[int, list[str]] | set[str]) -> None:
        if isinstance(data, list) or isinstance(data, set):
            self.save_data_list_or_set(data)
        elif isinstance(data, dict):
            self.save_data_dict(data)
        else:
            print("Type de data non reconnu dans save_data")


    def import_code(self)->tuple[list[str], list[str]]:
        list_file_code = []
        list_code = []
        list_file = os.listdir("In")
        for file in list_file:
            if ".txt" in file:
                list_file_code.append(file)
            with open("In/" + file, "r",encoding="utf-8") as file:
                list_code.append(self.code_mise_en_forme(file.read()))
        return list_code, list_file_code


    def verif_mot_possible(self, code: str) -> set[str]:
        sortie = set()
        taille_mot = len(code)
        data = self.open_data(taille_mot)
        for dmot in data:
            copy_mot = list(code)
            list_modif = {}
            ok = True
            for i in range(taille_mot):
                if (
                    code[i] not in list_modif.keys()
                    and code[i] in string.ascii_lowercase
                    and dmot[i] in string.ascii_lowercase
                ):
                    list_modif[code[i]] = dmot[i]
                    copy_mot[i] = dmot[i]
                elif code[i] in list_modif.keys() and list_modif[code[i]] == dmot[i]:
                    copy_mot[i] = list_modif[code[i]]
                elif code[i] == dmot[i] and code[i] not in string.ascii_lowercase:
                    pass
                else:
                    ok = False
                    break
            if ok:
                sortie.add(dmot)
        return sortie


    def code_motcode(self, code: str) -> list[str]:
        return code.split(" ")


    def remove_double(self, mot: str) -> str:
        sortie = ""
        for lettre in mot:
            if lettre not in sortie:
                sortie += lettre
        return sortie


    def remove_double_et_autre(self, mot: str) -> str:
        sortie = ""
        for lettre in mot:
            if lettre not in sortie and lettre in string.ascii_lowercase:
                sortie += lettre
        return sortie


    def mot_possible_inconu(self, word: str) -> set[str]:
        unique_letters = list(set(word))
        all_permutations = permutations(string.ascii_lowercase, len(unique_letters))

        possibilities = set()
        for perm in all_permutations:
            letter_mapping = dict(zip(unique_letters, perm))
            new_word = "".join(letter_mapping[letter] for letter in word)
            possibilities.add(new_word)

        return possibilities
    
    def interface(self)->None:
        Interface()

    def possibilite_dict(self, code:str, mots:set[str]) -> dict[str, set[str]]:
        sortie = {lettre: set() for lettre in code}
        for i in range(len(code)):
            for mot in mots:
                sortie[code[i]].add(mot[i])
        return sortie


    def sort_mot_taille(self, mots:set[str]|list[str]) -> list[str]:
        return sorted(mots, key=len)
    
    def code_mise_en_forme(self, code:str) -> str:
        code = code.lower()
        code = code.replace(".", "")
        return code
    
    def solution_commun(self,code:str)->dict[str, set[str]]:
        dico = {}
        for code_mot in self.sort_mot_taille(code.split(" ")):
            data = self.verif_mot_possible(code_mot)
            if not data:
                data = self.mot_possible_inconu(code_mot)
            temp_dico = self.possibilite_dict(code_mot, data)
            for lettre, set_ in temp_dico.items():
                if lettre not in dico.keys():
                    dico[lettre] = set_
                elif not dico[lettre] and set_:
                    dico[lettre] = set_
                elif dico[lettre].intersection(set_):
                    dico[lettre] = dico[lettre].intersection(set_)
        return dico
    
    def sort_dico(self, dico:dict[str, set[str]]) -> dict[str, set[str]]:
        sorted_dico = {}
        for key in sorted(dico.keys(), key=lambda x: len(dico[x])):
            sorted_dico[key] = dico[key]
        return sorted_dico
    

    def start(self):
        codes, files = self.import_code()
        for code in codes:
            print(code)
            dico = self.solution_commun(code)
            dico = self.sort_dico(dico)
            # print(dico)
            sortie = list(" " * len(code))
            deja_utiliser = set()
            for lettre, set_ in dico.items():
                for change in set_:
                    if change not in deja_utiliser:
                        index = 0
                        for i in range(code.count(lettre)):
                            index = code.find(lettre, index)
                            sortie[index] = change
                            index += 1
                        deja_utiliser.add(change)
                        break
            print("".join(sortie))




class Interface():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Decodeur Interface")

        tk.Label(self.root, text="Entrez une phrase:").pack(pady=10)
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        phrase_button = tk.Button(self.root, text="phrase", command=self.generate_phrase)
        phrase_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Etat du système: |")
        self.status_label.pack(pady=10)
        self.animation = True
        self.start_animation()

        self.root.mainloop()

    def start_animation(self):
        threading.Thread(target=self.animate, daemon=True).start()

    def animate(self):
        while self.animation:
            for frame in ["|", "/", "-", "\\"]:
                self.status_label.config(text=f"Etat du système: {frame}")
                time.sleep(0.1)

    def generate_phrase(self):
        generated_phrase = "Ceci est une phrase générée par le système."
        self.entry.delete(0, tk.END)
        self.entry.insert(0, generated_phrase)
        if messagebox.askyesno("Confirmation", f"Est-ce correct? \n\n{generated_phrase}"):
            messagebox.showinfo("Information", "Phrase enregistrée!")
        else:
            messagebox.showwarning("Attention", "Phrase non enregistrée!")



if __name__ == "__main__":
    decodeur = Decodeur()
    decodeur.start()
    
    