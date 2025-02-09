# Importing necessary modules/packages
import tkinter as tk 
from tkinter import messagebox
import random 

from PIL import Image, ImageTk

# Create the Main Application Window 

root = tk.Tk()
root.title('Memory Watching Game')

# Get screen height to scale images dynamically 
window_title_height = 50
os_window_height = 100
screen_height = root.winfo_screenheight() - (window_title_height + os_window_height)
screen_height = max(screen_height, 400)
print(screen_height)
# Define the Grid Dimensions
rows, cols = 4, 4
# Each image should fit in the grid=
cell_size = screen_height // rows  

# Handle resizing images 
def resize_image(image_path, size):
    img = Image.open(image_path)
    img = img.resize((size, size), Image.LANCZOS)
    return ImageTk.PhotoImage(img)




# Load and Prepare images:
image_files = [f"images/image{i}.jpg" for i in range(1, 9)]
images = [resize_image(img, cell_size) for img in image_files]

# Duplicate list to create pairs 

image_pairs = images * 2 

# Randomly shuffle the list of image pairs to ensure a unique game board each time
random.shuffle(image_pairs)

# Create a 2D list to represent the grid and assign the suffled images to each cell
grid = []
index = 0 
for row in range(rows):
    grid_row = []
    for col in range(cols):
        grid_row.append(image_pairs[index])
        index += 1
    
    grid.append(grid_row)


# Placeholder Image (Question Mark)
placeholder = resize_image("images/question_mark.png", cell_size)

# Game state variables 
first_selection = None
matched_pairs = 0
buttons = []

# Function to handle button clicks
def on_button_click(row, col):
    global first_selection, matched_pairs 

    button = buttons[row][col]

    # if already revealed, ignore click
    if button.cget('image') != str(placeholder):
        return
    
    # Reveal image 
    button.config(image=grid[row][col])
    


    if first_selection is None:
        first_selection = (row, col) 
    else:
        r1, c1 = first_selection
        # Check for a match
        if grid[r1][c1] == grid[row][col]:
            matched_pairs += 1 
            if matched_pairs == 8:
                messagebox.showinfo("Congratulations!", "You've matched all pairs!")
        else:
            # If not a match, reset images after a brief delay
            root.after(1000, lambda: hide_images(r1, c1, row, col))
        
        # Reset first selection after checking
        first_selection = None
    
def hide_images(r1, c1, r2, c2):
    buttons[r1][c1].config(image=placeholder)
    buttons[r2][c2].config(image=placeholder)

# Create the Grid of buttons
for row in range(rows):
    button_row = []
    for col in range(cols):
        button = tk.Button(
            root,
            image=placeholder,
            width=cell_size, 
            borderwidth=0, 
            highlightthickness=0,         
            command= lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)


# Game Progression:

# Turn Management: Allow players to continue selecting pairs of cells until all pairs are matched.
# Completion Check: The game concludes when all pairs have been successfully matched and revealed.

# Start the Tkinter event loop
root.mainloop()