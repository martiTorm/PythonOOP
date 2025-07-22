# ───────────── Object Creation ─────────────
inty = 5
listy = [6, 7]
stringy = "Hi"

# ───────────── Folium Map ─────────────
import folium

azores = folium.folium.Map(
    location=(38, -27),
    zoom_start=6
)

# ───────────── Objects List ─────────────
# Objects:
# - inty: 5
# - listy: [6, 7]
# - stringy: "Hi"
# - azores: folium.folium.Map(location=(38, -27), zoom_start=6)
# - and values: 6, 7, 38, -27, 6

# ───────────── Object Types ─────────────
print(type(inty))        # <class 'int'>
print(type(listy))       # <class 'list'>
print(type(stringy))     # <class 'str'>
print(type(azores))      # <class 'folium.folium.Map'>

# Direct types
print(type(5))           # <class 'int'>
print(type([6, 7]))      # <class 'list'>
print(type("Hi"))        # <class 'str'>
print(
    type(folium.folium.Map(location=(38, -27), zoom_start=6))
)                        # <class 'folium.folium.Map'>

# ───────────── Behind-the-Scenes Object Creation ─────────────
# These are just shorthand for their constructors:
#int(x=5)          # 5
#list((6, 7))      # [6, 7]
#str(object="Hi") # "Hi"

# ───────────── Save Map to HTML inside folder 1 ─────────────
azores.save("azores_map.html")

# ───────────── Object Behavior Summary ─────────────
# - Integers can be added, subtracted, multiplied, divided
# - Lists can be indexed, sliced, iterated
# - Strings can be concatenated, split, capitalized, formatted
# - Folium maps can be displayed, saved, manipulated