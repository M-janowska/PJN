import tkinter as tk
from tkinter import messagebox
from table import adjectives, verbs, nouns, zaimki

selected_words = []
O = False

def show_frame(frame):
    frame.tkraise()

def select_O():
    choice = O_var.get()
    if choice == "zaimek":
        show_frame(zaimek_frame)
    elif choice == "rzeczownik":
        show_frame(przymiotnik_frame)

def select_przymiotnik_option():
    choice = przymiotnik_var.get()
    if choice == "z przymiotnikiem":
        show_frame(adjective_frame) 
    else:
        show_frame(liczba_frame)

def select_liczba():
    global O
    liczba = liczba_var.get()
    noun = noun_var.get()

    if liczba == "mnoga":
        noun += "i"
    if not O: 
        selected_words.append(noun)
        show_frame(verb_frame)
    else:
        if liczba != "mnoga":
            noun += "n"
        selected_words.append(noun)
        display_result()

def select_zaimek():
    global O
    zaimek = zaimek_var.get()
    if zaimek:
        if not O:
            selected_words.append(zaimek)
            show_frame(verb_frame)
        else:
            if zaimek == "il":
                zaimek += "u"
            zaimek += "n"
            selected_words.append(zaimek)
            display_result()

def select_adjective():
    adjective = adjective_var.get()
    if adjective:
        selected_words.append(adjective)
        show_frame(liczba_frame)

def select_verb():
    global O
    czas = czas_var.get()
    verb = verb_var.get()
    pos = pos_var.get()
    verb = verb[:-2]
    if czas == "teraźniejszy":
        verb += "as"
    elif czas == "przeszły":
        verb += "is"
    else:
        verb += "os"
    if pos == "nie":
        selected_words.append("ne")
    if verb:
        selected_words.append(verb)
        O = True
        show_frame(O_frame)

def display_result():
    result = f"{' '.join(selected_words)}"
    messagebox.showinfo("Wynik", result)
    selected_words.clear()
    global O
    O = False

root = tk.Tk()
root.title("Tworzenie zdania SVO")
root.geometry("550x610")
root.configure(bg='black')

Start_frame = tk.Frame(root, bg='black')
O_frame = tk.Frame(root, bg='black')
zaimek_frame = tk.Frame(root, bg='black')
przymiotnik_frame = tk.Frame(root, bg='black')
adjective_frame = tk.Frame(root, bg='black')
liczba_frame = tk.Frame(root, bg='black')
verb_frame = tk.Frame(root, bg='black')

label_start = tk.Label(Start_frame, text="Generowania zdań SVO w języku Ido", fg='white', bg='black', font=('Arial', 20))
label_start.pack(pady=30)
label_start1 = tk.Label(Start_frame, text="Postępuj zgodnie z poleceniami", fg='white', bg='black', font=('Arial', 12))
label_start1.pack(pady=50)

start_button = tk.Button(Start_frame, text="Start", font=('Arial', 14), command=lambda: show_frame(O_frame))
start_button.pack(pady=20)

for frame in (Start_frame, O_frame, zaimek_frame, przymiotnik_frame, adjective_frame, liczba_frame, verb_frame):
    frame.grid(row=0, column=0, sticky='nsew')

label_O = tk.Label(O_frame, text="Wybierz zaimek lub rzeczownik:", fg='white', bg='black', font=('Arial', 14))
label_O.grid(row=0, column=0, pady=10)

O_var = tk.StringVar()

O_choices = ["zaimek", "rzeczownik"]
for i, choice in enumerate(O_choices):
    O_button = tk.Radiobutton(O_frame, text=choice, variable=O_var, value=choice, command=select_O, fg='white', bg='black', font=('Arial', 12))
    O_button.grid(row=1, column=i, padx=5, pady=5)

label_zaimek = tk.Label(zaimek_frame, text="Wybierz zaimek:", fg='white', bg='black', font=('Arial', 14))
label_zaimek.grid(row=0, column=0, columnspan=5, pady=10)

zaimek_var = tk.StringVar()

for i, zaimek in enumerate(zaimki):
    col = i % 5
    row = i // 5 + 1
    zaimek_button = tk.Radiobutton(zaimek_frame, text=zaimek, variable=zaimek_var, value=zaimek, command=select_zaimek, fg='white', bg='black', font=('Arial', 12))
    zaimek_button.grid(row=row, column=col, padx=5, pady=5)

label_przymiotnik = tk.Label(przymiotnik_frame, text="Czy dodać przymiotnik do rzeczownika?", fg='white', bg='black', font=('Arial', 14))
label_przymiotnik.grid(row=0, column=0, columnspan=5, pady=10)

przymiotnik_var = tk.StringVar()
przymiotnik_choices = ["bez przymiotnika", "z przymiotnikiem"]

for i, choice in enumerate(przymiotnik_choices):
    przymiotnik_button = tk.Radiobutton(przymiotnik_frame, text=choice, variable=przymiotnik_var, value=choice, command=select_przymiotnik_option, fg='white', bg='black', font=('Arial', 12))
    przymiotnik_button.grid(row=1, column=i, padx=5, pady=5)

label_adjective = tk.Label(adjective_frame, text="Wybierz przymiotnik:", fg='white', bg='black', font=('Arial', 14))
label_adjective.grid(row=0, column=0, columnspan=5, pady=10)

adjective_var = tk.StringVar()

for i, adjective in enumerate(adjectives):
    col = i % 5
    row = i // 5 + 1
    adjective_button = tk.Radiobutton(adjective_frame, text=adjective, variable=adjective_var, value=adjective, command=select_adjective, fg='white', bg='black', font=('Arial', 12))
    adjective_button.grid(row=row, column=col, padx=5, pady=5)

label_liczba = tk.Label(liczba_frame, text="Wybierz liczbę i rzeczownik:", fg='white', bg='black', font=('Arial', 14))
label_liczba.grid(row=0, column=0, columnspan=5, pady=10)

liczba_var = tk.StringVar()
liczba_choices = ["pojedyncza", "mnoga"]

for i, choice in enumerate(liczba_choices):
    liczba_button = tk.Radiobutton(liczba_frame, text=choice, variable=liczba_var, value=choice, fg='white', bg='black', font=('Arial', 12))
    liczba_button.grid(row=1, column=i, padx=5, pady=5)

label_noun = tk.Label(liczba_frame, text="Wybierz rzeczownik:", fg='white', bg='black', font=('Arial', 14))
label_noun.grid(row=2, column=0, columnspan=5, pady=10)

noun_var = tk.StringVar()

for i, noun in enumerate(nouns):
    col = i % 5
    row = i // 5 + 3
    noun_button = tk.Radiobutton(liczba_frame, text=noun, variable=noun_var, value=noun, command=select_liczba, fg='white', bg='black', font=('Arial', 12))
    noun_button.grid(row=row, column=col, padx=5, pady=5)


label_czas = tk.Label(verb_frame, text="Wybierz czas i czasownik:", fg='white', bg='black', font=('Arial', 14))
label_czas.grid(row=0, column=0, columnspan=5, pady=10)

czas_var = tk.StringVar()
czas_choices = ["teraźniejszy", "przeszły", "przyszły"]

for i, choice in enumerate(czas_choices):
    czas_button = tk.Radiobutton(verb_frame, text=choice, variable=czas_var, value=choice, fg='white', bg='black', font=('Arial', 12))
    czas_button.grid(row=1, column=i, padx=5, pady=5)

label_verb = tk.Label(verb_frame, text="Wybierz czasownik:", fg='white', bg='black', font=('Arial', 14))
label_verb.grid(row=2, column=0, columnspan=5, pady=10)

verb_var = tk.StringVar()

for i, verb in enumerate(verbs):
    col = i % 5
    row = i // 5 + 3
    verb_button = tk.Radiobutton(verb_frame, text=verb, variable=verb_var, value=verb, fg='white', bg='black', font=('Arial', 12))
    verb_button.grid(row=row, column=col, padx=5, pady=5)

label_pos = tk.Label(verb_frame, text="Czy zdanie twierdzące?", fg='white', bg='black', font=('Arial', 14))
label_pos.grid(row=row + 1, column=0, columnspan=5, pady=10)

pos_var = tk.StringVar()
pos_choices = ["tak", "nie"]

for i, choice in enumerate(pos_choices):
    pos_button = tk.Radiobutton(verb_frame, text=choice, variable=pos_var, command=select_verb, value=choice, fg='white', bg='black', font=('Arial', 12))
    pos_button.grid(row=row + 2, column=i, padx=5, pady=5)

show_frame(Start_frame)
root.mainloop()
