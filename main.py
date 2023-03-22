import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import os


class Window(tk.Frame):
    audio1: AudioSegment = None
    audio2: AudioSegment = None

    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.master.title("Fusionneur audio")
        self.pack()

        self.frame_audio1 = tk.Frame(self)

        self.label = tk.Label(self.frame_audio1, text="Sélectionner le premier fichier audio : ", width=30)
        self.label.pack(side=tk.LEFT)

        # Zone de texte pour afficher le chemin du premier fichier audio
        self.text_audio1 = tk.Text(self.frame_audio1, height=1, width=50)
        self.text_audio1.pack(side=tk.LEFT)

        # Bouton pour sélectionner le premier fichier audio
        self.btn_audio1 = tk.Button(self.frame_audio1, text="Sélectionner",
                                    command=self.select_audio1, width=15)
        self.btn_audio1.pack(side=tk.LEFT)

        self.frame_audio1.pack()

        self.frame_audio2 = tk.Frame(self)

        self.label = tk.Label(self.frame_audio2, text="Sélectionner le deuxième fichier audio : ", width=30)
        self.label.pack(side=tk.LEFT)

        # Zone de texte pour afficher le chemin du deuxième fichier audio
        self.text_audio2 = tk.Text(self.frame_audio2, height=1, width=50)
        self.text_audio2.pack(side=tk.LEFT)

        # Bouton pour sélectionner le deuxième fichier audio
        self.btn_audio2 = tk.Button(self.frame_audio2, text="Sélectionner", command=self.select_audio2, width=15)
        self.btn_audio2.pack(side=tk.LEFT)

        self.frame_audio2.pack()

        self.frame_select_folder_for_fusion = tk.Frame(self)

        self.label = tk.Label(self.frame_select_folder_for_fusion, text="Sélectionner le dossier de destination : ",
                              width=30)
        self.label.pack(side=tk.LEFT)

        # Zone de texte pour afficher le chemin du dossier de destination
        self.text_folder_for_fusion = tk.Text(self.frame_select_folder_for_fusion, height=1, width=50)
        self.text_folder_for_fusion.pack(side=tk.LEFT)

        # Bouton pour sélectionner le dossier de destination
        self.btn_folder_for_fusion = tk.Button(self.frame_select_folder_for_fusion, text="Sélectionner",
                                               command=self.select_folder_for_fusion, width=15)
        self.btn_folder_for_fusion.pack(side=tk.LEFT)

        self.frame_select_folder_for_fusion.pack()

        # Bouton pour fusionner les fichiers audio sélectionnés
        self.btn_fusionner = tk.Button(self, text="Fusionner les fichiers audio", command=self.fusionner_audio)
        self.btn_fusionner.pack()

    def select_audio1(self):
        # Ouvrir une boîte de dialogue pour sélectionner le premier fichier audio
        chemin_audio1 = filedialog.askopenfilename(title="Sélectionner le premier fichier audio")
        self.audio1 = AudioSegment.from_file(chemin_audio1, format="wav")
        self.text_audio1.delete("1.0", tk.END)  # Supprimer le texte existant
        self.text_audio1.insert(tk.END, chemin_audio1)  # Insérer le nouveau chemin d'accès
        print(f"Premier fichier audio sélectionné: {os.path.basename(chemin_audio1)}")

    def select_audio2(self):
        # Ouvrir une boîte de dialogue pour sélectionner le deuxième fichier audio
        chemin_audio2 = filedialog.askopenfilename(title="Sélectionner le deuxième fichier audio")
        self.audio2 = AudioSegment.from_file(chemin_audio2, format="wav")
        self.text_audio2.delete("1.0", tk.END)  # Supprimer le texte existant
        self.text_audio2.insert(tk.END, chemin_audio2)  # Insérer le nouveau chemin d'accès
        print(f"Deuxième fichier audio sélectionné: {os.path.basename(chemin_audio2)}")

    def select_folder_for_fusion(self):
        # Ouvrir une boîte de dialogue pour sélectionner le dossier de destination
        chemin_folder_for_fusion = filedialog.askdirectory(title="Sélectionner le dossier de destination")
        self.text_folder_for_fusion.delete("1.0", tk.END)  # Supprimer le texte existant
        self.text_folder_for_fusion.insert(tk.END, chemin_folder_for_fusion)  # Insérer le nouveau chemin d'accès
        print(f"Dossier de destination sélectionné: {os.path.basename(chemin_folder_for_fusion)}")

    def fusionner_audio(self):
        # Vérifier que les deux fichiers audio ont été sélectionnés
        if hasattr(self, "audio1") and hasattr(self, "audio2"):
            # Fusionner les fichiers audio
            fusion = self.audio1 + self.audio2

            # Nommer le fichier fusionné avec les noms des fichiers audio d'origine
            nom_audio1 = os.path.basename(self.text_audio1.get("1.0", tk.END)).strip()
            nom_audio2 = os.path.basename(self.text_audio2.get("1.0", tk.END)).strip()
            nom_fusion = f"{nom_audio1[:-4]}_{nom_audio2[:-4]}_fusion.wav"

            # Chemin d'accès du fichier fusionné
            full_path_fusion = os.path.join(self.text_folder_for_fusion.get("1.0", tk.END).strip(), nom_fusion)

            # Exporter le fichier fusionné
            fusion.export(full_path_fusion, format="wav")
            print(f"Fichier fusionné exporté: {nom_fusion}")
        else:
            print("Veuillez sélectionner deux fichiers audio.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(master=root)
    app.mainloop()
