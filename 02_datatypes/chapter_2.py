# EXAMPLE OF MUTABLE DATA TYPE:

spice_mix = set(); 

print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")

print(f"Initial spice mix id: {spice_mix}")
print(f"Initial spice mix id: {id(spice_mix)}")

# NOTES: Here we see spice_mix is Mutable because the changes we do after the declaration the id remain.