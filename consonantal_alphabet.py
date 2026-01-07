import tkinter as tk

voc = ['a', 'e', 'i', 'o', 'u',
       'A', 'E', 'I', 'O', 'U']

def remove_vowels():
    text = entry.get()
    text_as_list = list(text)
    new_text_list = []

    #testing letters
    for c in text_as_list:
        if c not in voc:
            new_text_list.append(c)

    #list to string
    new_text = ''.join(new_text_list)
    result_value.config(text=new_text)

#window
window = tk.Tk()
window.title("Consonantal Alphabet")

#text label + entry
text_label = tk.Label(window, text="Text:")
text_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = tk.Entry(window, width=40)
entry.insert(0, "Hey! This is my first public project")#preset text
entry.grid(row=0, column=1, padx=5, pady=5)

#button
button = tk.Button(window, text="Remove vowels", command=remove_vowels)
button.grid(row=1, column=0, columnspan=2, pady=10)

#result label + value
result_label = tk.Label(window, text="Result:")
result_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

result_value = tk.Label(window, text="")
result_value.grid(row=2, column=1, sticky="w", padx=5, pady=5)

window.mainloop()