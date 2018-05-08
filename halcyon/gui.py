import tkinter
import planet
import building

window = tkinter.Tk()
window.geometry('500x500')
window.title('Halcyon')

planet_name_entry = tkinter.Entry(window, width=10)
planet_name_entry.grid(column=0, row=1)
planet_x_entry = tkinter.Spinbox(window, from_=0, to=1000, width=5)
planet_x_entry.grid(column=0, row=2)
planet_y_entry = tkinter.Spinbox(window, from_=0, to=1000, width=5)
planet_y_entry.grid(column=0, row=3)

PLANET_LABELS = []

def create_planet_clicked():
    try:
        for obj in PLANET_LABELS:
            obj.destroy()
    except:
        raise
        pass
    planet_name = planet_name_entry.get()
    x_coord = planet_x_entry.get()
    y_coord = planet_y_entry.get()
    new_planet = planet.Planet(planet_name, x_coord, y_coord)
    planet_label = tkinter.Label(window, text=new_planet)
    planet_label.grid(column=1, row=1)
    planet_desc = tkinter.Label(window, text=new_planet.get_description())
    planet_desc.grid(column=1, row=2)
    PLANET_LABELS.append(planet_label)
    PLANET_LABELS.append(planet_desc)

btn = tkinter.Button(window, text='Create Planet', command=create_planet_clicked)
btn.grid(column=0, row=0)

window.mainloop()
