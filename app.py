from flask import Flask, render_template, request

app = Flask(__name__)

def recommend_colors(eye_color, hair_color, skin_tone):
    # Define all possible combinations and their corresponding color recommendations
    color_recommendations = {
        # Blue Eyes
        ("blue", "blonde", "fair"): ["Pastel Pink", "Light Blue", "Soft Lavender"],
        ("blue", "blonde", "medium"): ["Soft Peach", "Sky Blue", "Lavender Gray"],
        ("blue", "blonde", "olive"): ["Mint Green", "Powder Blue", "Soft Coral"],
        ("blue", "blonde", "dark"): ["Bright White", "Royal Blue", "Soft Pink"],
        ("blue", "black", "fair"): ["Navy Blue", "Silver", "Ice Blue"],
        ("blue", "black", "medium"): ["Teal", "Charcoal Gray", "Soft White"],
        ("blue", "black", "olive"): ["Deep Blue", "Slate Gray", "Cream"],
        ("blue", "black", "dark"): ["Electric Blue", "Black", "Pure White"],
        ("blue", "brown", "fair"): ["Light Blue", "Beige", "Soft Yellow"],
        ("blue", "brown", "medium"): ["Turquoise", "Warm Gray", "Soft Orange"],
        ("blue", "brown", "olive"): ["Aqua", "Taupe", "Coral"],
        ("blue", "brown", "dark"): ["Cobalt Blue", "Dark Gray", "Gold"],
        ("blue", "red", "fair"): ["Soft Pink", "Light Blue", "Lavender"],
        ("blue", "red", "medium"): ["Coral", "Sky Blue", "Mauve"],
        ("blue", "red", "olive"): ["Salmon", "Teal", "Lilac"],
        ("blue", "red", "dark"): ["Bright Pink", "Navy Blue", "Soft Purple"],
        ("blue", "auburn", "fair"): ["Peach", "Light Blue", "Soft Lavender"],
        ("blue", "auburn", "medium"): ["Coral", "Sky Blue", "Mauve"],
        ("blue", "auburn", "olive"): ["Terracotta", "Teal", "Lilac"],
        ("blue", "auburn", "dark"): ["Rust", "Navy Blue", "Soft Purple"],
        ("blue", "gray", "fair"): ["Pastel Pink", "Light Blue", "Soft Lavender"],
        ("blue", "gray", "medium"): ["Soft Peach", "Sky Blue", "Lavender Gray"],
        ("blue", "gray", "olive"): ["Mint Green", "Powder Blue", "Soft Coral"],
        ("blue", "gray", "dark"): ["Bright White", "Royal Blue", "Soft Pink"],

        # [Keep all your other color combinations...]
        # Brown Eyes
        ("brown", "blonde", "fair"): ["Soft Pink", "Emerald Green", "Warm Coral"],
        # [Rest of your existing color recommendations...]
    }

    # Return the recommended colors for the given combination, or default if not found
    return color_recommendations.get((eye_color, hair_color, skin_tone), ["Neutral Beige", "White", "Navy Blue"])

def get_text_color(color_name):
    # Map color names to their actual hex values
    color_map = {
        "pastel pink": "#ffd1dc",
        "light blue": "#add8e6",
        "soft lavender": "#e6e6fa",
        "soft peach": "#ffd8b1",
        "sky blue": "#87ceeb",
        "lavender gray": "#c4c3d0",
        "mint green": "#98ff98",
        "powder blue": "#b0e0e6",
        "soft coral": "#f08080",
        "bright white": "#ffffff",
        "royal blue": "#4169e1",
        "soft pink": "#ffb6c1",
        "navy blue": "#000080",
        "neutral beige": "#f5f5dc",
        "white": "#ffffff",
        "emerald green": "#50c878",
        "warm coral": "#ff7f50",
        "olive green": "#808000",
        "warm beige": "#f5cba7",
        "mustard yellow": "#ffdb58",
        "terracotta": "#e2725b",
        "warm gray": "#a8a8a8",
        "gold": "#ffd700",
        "deep orange": "#ff8c00",
        "warm white": "#f5f5f5",
        "burgundy": "#800020",
        "deep purple": "#36013f",
        "forest green": "#228b22",
        "rich burgundy": "#800020",
        "dark green": "#006400",
        "deep burgundy": "#800020",
        "coral": "#ff7f50",
        "aqua": "#00ffff",
        "taupe": "#483c32",
        "cobalt blue": "#0047ab",
        "dark gray": "#a9a9a9",
        "salmon": "#fa8072",
        "lilac": "#c8a2c8",
        "bright pink": "#ff007f",
        "soft purple": "#b19cd9",
        "peach": "#ffe5b4",
        "rust": "#b7410e",
        "teal": "#008080",
        "charcoal gray": "#36454f",
        "cream": "#fffdd0",
        "black": "#000000",
        "pure white": "#ffffff",
        "turquoise": "#40e0d0",
        "soft orange": "#ffcc99",
        "mauve": "#e0b0ff",
        "electric blue": "#7df9ff",
        "slate gray": "#708090",
        "ice blue": "#99ffff",
        "silver": "#c0c0c0",
        "deep blue": "#00008b",
        "beige": "#f5f5dc",
        "yellow": "#ffff00",
        "orange": "#ffa500",
        "purple": "#800080",
        "pink": "#ffc0cb",
        "red": "#ff0000",
        "green": "#008000",
        "blue": "#0000ff",
        "gray": "#808080",
        "auburn": "#a52a2a"
    }
    # Default to black if no mapping is found
    return color_map.get(color_name.lower(), "#000000")

def is_light_color(hex_color):
    # Convert hex to RGB
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    # Calculate luminance
    luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])/255
    return luminance > 0.5

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        eye_color = request.form.get("eye_color").strip().lower()
        hair_color = request.form.get("hair_color").strip().lower()
        skin_tone = request.form.get("skin_tone").strip().lower()
        colors = recommend_colors(eye_color, hair_color, skin_tone)
        return render_template("index.html", 
                            colors=colors, 
                            eye_color=eye_color, 
                            hair_color=hair_color, 
                            skin_tone=skin_tone,
                            get_text_color=get_text_color,
                            is_light_color=is_light_color)
    return render_template("index.html", colors=None)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
