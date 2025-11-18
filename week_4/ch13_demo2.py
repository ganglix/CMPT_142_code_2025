# nested dictionary

# green colour theme for a website
green_theme = {
    "background": {"red": 0, "green": 100, "blue": 0},
    "foreground": {"red": 0, "green": 200, "blue": 100},
    "font": {"red": 255, "green": 255, "blue": 255}
}
# halve all of the green intensities (round down to nearest int)

# reduced problem: print out all green intensities
for component in green_theme:
    # component : {r g b}
    rgb = green_theme[component]
    print(rgb['green'])    # green_theme[component]['green']

for component in green_theme:
    # component : {r g b}
    rgb = green_theme[component]
    rgb['green'] //= 2

print(green_theme)