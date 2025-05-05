from flask import Flask, render_template, request
import os

app = Flask(__name__)

def recommend_colors(eye_color, hair_color, skin_tone):
    # Define all possible combinations and their corresponding color recommendations
    color_recommendations = {
        # Blue Eyes Combinations (existing)
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

        # Brown Eyes (enhanced)
        ("brown", "blonde", "fair"): ["Soft Pink", "Emerald Green", "Warm Coral"],
        ("brown", "blonde", "medium"): ["Olive Green", "Warm Beige", "Mustard Yellow"],
        ("brown", "blonde", "olive"): ["Terracotta", "Warm Gray", "Gold"],
        ("brown", "blonde", "dark"): ["Deep Orange", "Warm White", "Burgundy"],
        ("brown", "black", "fair"): ["Deep Purple", "Forest Green", "Rich Burgundy"],
        ("brown", "black", "medium"): ["Dark Green", "Deep Burgundy", "Gold"],
        ("brown", "black", "olive"): ["Coral", "Aqua", "Taupe"],
        ("brown", "black", "dark"): ["Cobalt Blue", "Dark Gray", "Gold"],
        ("brown", "brown", "fair"): ["Salmon", "Lilac", "Bright Pink"],
        ("brown", "brown", "medium"): ["Soft Purple", "Peach", "Rust"],
        ("brown", "brown", "olive"): ["Teal", "Charcoal Gray", "Cream"],
        ("brown", "brown", "dark"): ["Black", "Pure White", "Turquoise"],
        ("brown", "red", "fair"): ["Soft Orange", "Mauve", "Electric Blue"],
        ("brown", "red", "medium"): ["Slate Gray", "Ice Blue", "Silver"],
        ("brown", "red", "olive"): ["Deep Blue", "Beige", "Yellow"],
        ("brown", "red", "dark"): ["Orange", "Purple", "Pink"],
        ("brown", "auburn", "fair"): ["Red", "Green", "Blue"],
        ("brown", "auburn", "medium"): ["Gray", "Auburn", "White"],
        ("brown", "auburn", "olive"): ["Pastel Pink", "Light Blue", "Soft Lavender"],
        ("brown", "auburn", "dark"): ["Soft Peach", "Sky Blue", "Lavender Gray"],

        # Green Eyes (new)
        ("green", "blonde", "fair"): ["Mauve", "Dusty Rose", "Sage Green"],
        ("green", "blonde", "medium"): ["Moss Green", "Taupe", "Peach"],
        ("green", "blonde", "olive"): ["Emerald", "Copper", "Cream"],
        ("green", "blonde", "dark"): ["Jade", "Gold", "Eggplant"],
        ("green", "black", "fair"): ["Plum", "Forest Green", "Mocha"],
        ("green", "black", "medium"): ["Hunter Green", "Burgundy", "Camel"],
        ("green", "black", "olive"): ["Olive", "Rust", "Ivory"],
        ("green", "black", "dark"): ["Dark Teal", "Chocolate", "Cream"],
        ("green", "brown", "fair"): ["Mint", "Coral", "Lavender"],
        ("green", "brown", "medium"): ["Sage", "Terracotta", "Periwinkle"],
        ("green", "brown", "olive"): ["Army Green", "Burnt Orange", "Lilac"],
        ("green", "brown", "dark"): ["Bottle Green", "Copper", "Pale Yellow"],
        ("green", "red", "fair"): ["Dusty Pink", "Seafoam", "Lavender"],
        ("green", "red", "medium"): ["Rose", "Aqua", "Mauve"],
        ("green", "red", "olive"): ["Cranberry", "Teal", "Lilac"],
        ("green", "red", "dark"): ["Ruby", "Navy", "Soft Purple"],
        ("green", "auburn", "fair"): ["Peach", "Seafoam", "Lavender"],
        ("green", "auburn", "medium"): ["Coral", "Aqua", "Mauve"],
        ("green", "auburn", "olive"): ["Terracotta", "Teal", "Lilac"],
        ("green", "auburn", "dark"): ["Rust", "Navy", "Soft Purple"],

        # Hazel Eyes (new)
        ("hazel", "blonde", "fair"): ["Soft Gold", "Lavender", "Peach"],
        ("hazel", "blonde", "medium"): ["Warm Beige", "Sage", "Dusty Pink"],
        ("hazel", "blonde", "olive"): ["Olive Green", "Terracotta", "Cream"],
        ("hazel", "blonde", "dark"): ["Gold", "Burgundy", "Eggplant"],
        ("hazel", "black", "fair"): ["Deep Purple", "Emerald", "Mocha"],
        ("hazel", "black", "medium"): ["Dark Green", "Burgundy", "Camel"],
        ("hazel", "black", "olive"): ["Army Green", "Rust", "Ivory"],
        ("hazel", "black", "dark"): ["Dark Teal", "Chocolate", "Cream"],
        ("hazel", "brown", "fair"): ["Honey", "Lavender", "Coral"],
        ("hazel", "brown", "medium"): ["Amber", "Periwinkle", "Terracotta"],
        ("hazel", "brown", "olive"): ["Olive", "Burnt Orange", "Lilac"],
        ("hazel", "brown", "dark"): ["Bronze", "Copper", "Pale Yellow"],
        ("hazel", "red", "fair"): ["Apricot", "Seafoam", "Lavender"],
        ("hazel", "red", "medium"): ["Copper", "Aqua", "Mauve"],
        ("hazel", "red", "olive"): ["Rust", "Teal", "Lilac"],
        ("hazel", "red", "dark"): ["Deep Red", "Navy", "Soft Purple"],
        ("hazel", "auburn", "fair"): ["Peach", "Seafoam", "Lavender"],
        ("hazel", "auburn", "medium"): ["Amber", "Aqua", "Mauve"],
        ("hazel", "auburn", "olive"): ["Terracotta", "Teal", "Lilac"],
        ("hazel", "auburn", "dark"): ["Rust", "Navy", "Soft Purple"],

        # Gray Eyes (new)
        ("gray", "blonde", "fair"): ["Icy Blue", "Soft Pink", "Lavender Gray"],
        ("gray", "blonde", "medium"): ["Slate Blue", "Dusty Rose", "Mauve"],
        ("gray", "blonde", "olive"): ["Steel Blue", "Taupe", "Rose Quartz"],
        ("gray", "blonde", "dark"): ["Navy", "Deep Rose", "Silver"],
        ("gray", "black", "fair"): ["Charcoal", "Ice Blue", "Pale Pink"],
        ("gray", "black", "medium"): ["Graphite", "Powder Blue", "Blush"],
        ("gray", "black", "olive"): ["Slate Gray", "Soft Teal", "Mauve"],
        ("gray", "black", "dark"): ["Black", "Silver", "Deep Purple"],
        ("gray", "brown", "fair"): ["Cool Gray", "Lavender", "Pale Yellow"],
        ("gray", "brown", "medium"): ["Stone", "Periwinkle", "Peach"],
        ("gray", "brown", "olive"): ["Pewter", "Dusty Blue", "Soft Coral"],
        ("gray", "brown", "dark"): ["Dark Gray", "Pale Blue", "Warm White"],
        ("gray", "red", "fair"): ["Cool Pink", "Seafoam", "Lavender"],
        ("gray", "red", "medium"): ["Rose Gray", "Aqua", "Mauve"],
        ("gray", "red", "olive"): ["Taupe", "Teal", "Lilac"],
        ("gray", "red", "dark"): ["Deep Rose", "Navy", "Soft Purple"],
        ("gray", "auburn", "fair"): ["Dusty Pink", "Seafoam", "Lavender"],
        ("gray", "auburn", "medium"): ["Rose", "Aqua", "Mauve"],
        ("gray", "auburn", "olive"): ["Taupe", "Teal", "Lilac"],
        ("gray", "auburn", "dark"): ["Deep Rose", "Navy", "Soft Purple"]
    }

    # Return the recommended colors for the given combination, or default if not found
    return color_recommendations.get((eye_color, hair_color, skin_tone), ["Neutral Beige", "White", "Navy Blue"])

# [Rest of your existing functions (get_text_color, is_light_color) remain unchanged]
# [Your existing route and app setup remain unchanged]
