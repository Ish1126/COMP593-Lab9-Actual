"""
Description:
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""

from tkinter import *
from tkinter import Tk, ttk, messagebox
from poke_api import get_pokemon_info

# Create the main window
root = Tk()
root.title("Pokemon Information")
root.resizable(False, False)

# Create the frames
frame_input1 = ttk.Frame(root)
frame_input1.grid(row=0, column=0, columnspan=2, pady=(20, 10))

# Frame for info
frame_info1 = ttk.LabelFrame(root, text="Info")
frame_info1.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="N")

# Frame for Stats
frame_stats1 = ttk.LabelFrame(root, text="Stats")
frame_stats1.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky="N")

# Populate the user input frame with widgets
lbl_name = ttk.Label(frame_input1, text="Pokemon Name:")
lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

enter_name = ttk.Entry(frame_input1)
enter_name.insert(0, "Pikachu")
enter_name.grid(row=0, column=1)

button_get_info = ttk.Button(frame_input1, text='Get Info', command=lambda: handle_btn_get_info())
button_get_info.grid(row=0, column=2, padx=(10, 0))

# Populate the info frame with widgets
label_height = ttk.Label(frame_info1, text="Height:")
label_height.grid(row=0, column=0, sticky="W")
label_height_value = ttk.Label(frame_info1, width=20)
label_height_value.grid(row=0, column=1, sticky="W")

label_weight = ttk.Label(frame_info1, text="Weight:")
label_weight.grid(row=1, column=0, sticky="W")
label_weight_value = ttk.Label(frame_info1, width=20)
label_weight_value.grid(row=1, column=1, sticky="W")

label_type = ttk.Label(frame_info1, text="Type:")
label_type.grid(row=2, column=0, sticky="W")
label_type_value = ttk.Label(frame_info1, width=20)
label_type_value.grid(row=2, column=1, sticky="W")

# Define Progress bars for the stats frame
bar_hp = ttk.Progressbar(frame_stats1, length=200, maximum=255)
bar_hp.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="W")

bar_attack = ttk.Progressbar(frame_stats1, length=200, maximum=255)
bar_attack.grid(row=1, column=1, padx=(5, 10), pady=(5, 10), sticky="W")

bar_defense = ttk.Progressbar(frame_stats1, length=200, maximum=255)
bar_defense.grid(row=2, column=1, padx=(5, 10), pady=(5, 10), sticky="W")

bar_special_attack = ttk.Progressbar(frame_stats1, length=200, maximum=255)
bar_special_attack.grid(row=3, column=1, padx=(5, 10), pady=(5, 10), sticky="W")

bar_special_defense = ttk.Progressbar(frame_stats1, length=200, maximum=255)
bar_special_defense.grid(row=4, column=1, padx=(5, 10), pady=(5, 10), sticky="W")

bar_speed = ttk.Progressbar(frame_stats1, length=200, maximum=255)
bar_speed.grid(row=5, column=1, padx=(5, 10), pady=(5, 10), sticky="W")

def handle_btn_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '':
        return

    poke_info = get_pokemon_info(poke_name)
    print(f"Fetched data for {poke_name}: {poke_info}")  # Debugging statement
    
    if poke_info:
        label_height_value['text'] = str(poke_info["height"]) + ' dm'
        label_weight_value['text'] = str(poke_info["weight"]) + ' hg'
        types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
        
        # stats
        label_type_value['text'] = ', '.join(types_list)
        bar_hp['value'] = poke_info['stats'][0]['base_stat']
        bar_attack['value'] = poke_info['stats'][1]['base_stat']
        bar_defense['value'] = poke_info['stats'][2]['base_stat']
        bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
        bar_special_defense['value'] = poke_info['stats'][4]['base_stat']
        bar_speed['value'] = poke_info['stats'][5]['base_stat']
    else:
        error_message = f"Unable to fetch information for {poke_name.capitalize()} from the PokeAPI."
        messagebox.showinfo(title='Error', message=error_message)

# Main loop
root.mainloop()
