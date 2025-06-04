class App:
    def __init__(self,  root):
        self.root = root
        self.root.title("Python GUI Anwendung")
        self.root.geometry("600x400")

        self.create_menu()
        self.create_widgets()
        self.create_status_bar()

        self.progress()


    def create_menu(self):
        menu_bar = anzeige(self.root)

        file_menu = anzeige(menu_bar, tearoff=0)
        file_menu.add.command(label="Öffnen", command=self.dummy_action)
        file_menu.add_command(label="Beenden", command=self.root.quit)
        menu_bar.add_cascade(label="Datei", menu=file_menu)

        help_menu = anzeige(menu_bar, tearoff=0)
        help.menu.add_command(label="Info", command=lambda: messagebox.showinfo("Info", "Dies ist eine Demo-GUI in Python."))
        menu_bar.add_cascade(label="Hilfe", menu=help_menu)

        self.root.config(menu=menu_bar) 

