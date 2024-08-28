import tkinter as tk
from tkinter import scrolledtext

# Function to show info when a square is clicked
def open_info_screen(name, info_items):
    # Hide the main frame
    main_frame.pack_forget()

    # Create a new frame for the info screen
    info_frame = tk.Frame(root, bg="#333333")
    info_frame.pack(expand=True, fill='both')

    # Display the detailed text information with checkboxes
    row = 0
    for item, var in info_items:
        checkbutton = tk.Checkbutton(info_frame, text=item, variable=var, bg="#333333", fg="white", font=("Helvetica", 12), selectcolor="#555555", indicatoron=0, anchor="w")
        checkbutton.grid(row=row, column=0, sticky='w', padx=20, pady=5)
        row += 1

    # Create a "Back" button to return to the main screen
    back_button = tk.Button(info_frame, text="Back", command=lambda: go_back(info_frame), font=("Helvetica", 12, 'bold'), bg="#007bff", fg="white", relief="flat")
    back_button.grid(row=row, column=0, pady=20)

# Function to go back to the main screen
def go_back(info_frame):
    # Destroy the info frame
    info_frame.destroy()

    # Show the main frame again
    main_frame.pack(expand=True, fill='both')

# Create the main window
root = tk.Tk()
root.title("Workout Categories")
root.configure(bg="black")

# Set the size of the main window to mobile dimensions
root.geometry("375x667")

# Create a frame to hold the squares
main_frame = tk.Frame(root, bg="black")
main_frame.pack(expand=True, fill='both')

# Define square names and their detailed information with checkboxes
square_info = {
    "Pull 1": (
        [("Pull 1 (23 sets)", None),
         ("Back (8 sets)", None),
         ("Lat Pull Down 4x12", None),
         ("Machine Row 4x12", None),
         ("Arms (11 sets)", None),
         ("Incline Bicep Curl 4x12", None),
         ("Rope Pull Down 4x12", None),
         ("Skull Crushers 3x12", None)]
    ),
    "Push 1": (
        [("Push 1 (20 sets)", None),
         ("Chest (8 sets)", None),
         ("Incline Bench Press 4x12", None),
         ("Cable/Machine Flye 4x12", None),
         ("Arm (8 sets)", None),
         ("Dips 4x12", None),
         ("Tricep Pushdown 4x12", None)]
    ),
    "Leg 1": (
        [("Legs 1 (19 sets)", None),
         ("Legs (15 Sets)", None),
         ("Leg Extension 3x10", None),
         ("Hamstring Curl 3x10", None),
         ("Adductor Machine 3x10", None),
         ("Hip Extension 3x12", None),
         ("Calf Raises 3x12", None),
         ("Core (4 sets)", None),
         ("Hanging L-sits 4x30 sn/ failure", None)]
    ),
    "Pull 2": (
        [("Pull 2 (26 sets)", None),
         ("Back (11 sets)", None),
         ("Bent Rows 4x12", None),
         ("Pull-ups 4x12", None),
         ("Lat Prayers 3x12", None),
         ("Arm (11 sets)", None),
         ("Rope Pull Down 4x12", None),
         ("EZ Bicep Curl 4x12", None),
         ("Skull Crushers 3x12", None),
         ("Shoulder (4 sets)", None),
         ("Lat Raises 4x12", None)]
    ),
    "Push 2": (
        [("Push 2 (20 sets)", None),
         ("Chest (8 sets)", None),
         ("Bench 4x12", None),
         ("Cable Flye 4x12 (?)", None),
         ("Shoulder (4 sets)", None),
         ("Incline Shoulder Dumbbell Press 4x12", None),
         ("Arm (8 sets)", None),
         ("Tricep Pushdown 4x12", None),
         ("Dips 4x12", None)]
    ),
    "Leg 2": (
        [("Legs 2 (19 sets)", None),
         ("Legs (15 Sets)", None),
         ("Leg Press 3x10", None),
         ("Hamstring Curl 3x10", None),
         ("Adductor Machine 3x10", None),
         ("Hip Extension 3x12", None),
         ("Calf Raises 3x12", None),
         ("Core (4 sets)", None),
         ("Hanging L-sits 4x30 sn/ failure", None)]
    )
}

# Create squares with detailed information
for i, (name, info) in enumerate(square_info.items()):
    # Create an empty list for the checkbutton variables
    checkbutton_vars = [tk.BooleanVar() for _ in info]
    info_with_vars = list(zip([item for item, _ in info], checkbutton_vars))

    square = tk.Button(
        main_frame, 
        text=name, 
        bg="#808080",  # 50% gray
        fg="white", 
        font=("Helvetica", 14, 'bold'), 
        width=10,  # Fixed width for uniformity
        height=5,  # Fixed height for uniformity
        relief="flat", 
        command=lambda n=name, t=info_with_vars: open_info_screen(n, t)
    )
    
    # Center the squares in the window
    square.grid(row=i//2, column=i%2, padx=20, pady=20, sticky="nsew")

# Make sure the columns and rows expand equally
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

# Run the application
root.mainloop()
