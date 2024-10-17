import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import random

def choose_color1():
    color_code = colorchooser.askcolor(title="Choose color 1")[0]  # Get only the RGB tuple
    if color_code:
        color1_entry.config(bg='#%02x%02x%02x' % color_code)
        return color_code

def choose_color2():
    color_code = colorchooser.askcolor(title="Choose color 2")[0]  # Get only the RGB tuple
    if color_code:
        color2_entry.config(bg='#%02x%02x%02x' % color_code)
        return color_code

def generate_logo():
    company_name = company_name_entry.get()
    tagline = tagline_entry.get()
    color1 = color1_entry.get()
    color2 = color2_entry.get()

    if not company_name:
        messagebox.showerror("Input Error", "Company name is required")
        return
    
    # Convert color strings to tuples if colors are chosen
    color1 = tuple(map(int, color1.strip('()').split(','))) if color1 else None
    color2 = tuple(map(int, color2.strip('()').split(','))) if color2 else None
    
    # Set image size
    width, height = 400, 200
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Generate random colors if not provided
    if not color1:
        color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if not color2:
        color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw background shapes (e.g., circles or rectangles)
    draw.rectangle([(0, 0), (width, height//2)], fill=color1)
    draw.rectangle([(0, height//2), (width, height)], fill=color2)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 40)
        tagline_font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
        tagline_font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(company_name, font=font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2 - 20
    
    # Add company name text
    draw.text((text_x, text_y), company_name, fill="white", font=font)

    # Add tagline if provided
    if tagline:
        tagline_width, tagline_height = draw.textsize(tagline, font=tagline_font)
        tagline_x = (width - tagline_width) / 2
        tagline_y = text_y + text_height + 10
        draw.text((tagline_x, tagline_y), tagline, fill="white", font=tagline_font)

    # Save the logo image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        image.save(file_path)
        messagebox.showinfo("Success", f"Logo saved as: {file_path}")
    else:
        messagebox.showwarning("Save Cancelled", "Logo not saved")

# Create main window
root = tk.Tk()
root.title("Logo Generator")

# Company Name
tk.Label(root, text="Company Name:").grid(row=0, column=0, padx=10, pady=10)
company_name_entry = tk.Entry(root, width=30)
company_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Tagline
tk.Label(root, text="Tagline (Optional):").grid(row=1, column=0, padx=10, pady=10)
tagline_entry = tk.Entry(root, width=30)
tagline_entry.grid(row=1, column=1, padx=10, pady=10)

# Color 1
tk.Label(root, text="Color 1 (Top):").grid(row=2, column=0, padx=10, pady=10)
color1_entry = tk.Entry(root, width=10)
color1_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
color1_button = tk.Button(root, text="Choose", command=lambda: color1_entry.delete(0, tk.END) or color1_entry.insert(0, str(choose_color1())))
color1_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Color 2
tk.Label(root, text="Color 2 (Bottom):").grid(row=3, column=0, padx=10, pady=10)
color2_entry = tk.Entry(root, width=10)
color2_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
color2_button = tk.Button(root, text="Choose", command=lambda: color2_entry.delete(0, tk.END) or color2_entry.insert(0, str(choose_color2())))
color2_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Generate Button
generate_button = tk.Button(root, text="Generate Logo", command=generate_logo)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()

