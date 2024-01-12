# food_tracker_gui.py

import csv
import os
import tkinter as tk
from tkinter import ttk

class FoodTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Tracker")

        self.food_db_file = "food_database.csv"
        self.log_file = "food_log.csv"

        self.initialize_files()

        # Create GUI elements
        self.food_label = ttk.Label(root, text="Food:")
        self.food_entry = ttk.Entry(root)
        self.protein_label = ttk.Label(root, text="Protein (g):")
        self.protein_entry = ttk.Entry(root)
        self.carbs_label = ttk.Label(root, text="Carbs (g):")
        self.carbs_entry = ttk.Entry(root)
        self.fat_label = ttk.Label(root, text="Fat (g):")
        self.fat_entry = ttk.Entry(root)
        self.add_food_button = ttk.Button(root, text="Add Food", command=self.add_food)

        self.date_label = ttk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_entry = ttk.Entry(root)
        self.portion_label = ttk.Label(root, text="Portion Size (g):")
        self.portion_entry = ttk.Entry(root)
        self.log_food_button = ttk.Button(root, text="Log Food Entry", command=self.log_food_entry)

        # Arrange GUI elements
        self.food_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.food_entry.grid(row=0, column=1, pady=5)
        self.protein_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.protein_entry.grid(row=1, column=1, pady=5)
        self.carbs_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.carbs_entry.grid(row=2, column=1, pady=5)
        self.fat_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.fat_entry.grid(row=3, column=1, pady=5)
        self.add_food_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.date_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.date_entry.grid(row=5, column=1, pady=5)
        self.portion_label.grid(row=6, column=0, sticky=tk.W, pady=5)
        self.portion_entry.grid(row=6, column=1, pady=5)
        self.log_food_button.grid(row=7, column=0, columnspan=2, pady=10)

    def initialize_files(self):
        if not os.path.exists(self.food_db_file):
            with open(self.food_db_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Food', 'Protein', 'Carbs', 'Fat'])

        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Food', 'Portion'])

    def add_food(self):
        food = self.food_entry.get()
        protein = float(self.protein_entry.get())
        carbs = float(self.carbs_entry.get())
        fat = float(self.fat_entry.get())

        with open(self.food_db_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([food, protein, carbs, fat])

        # Optionally, you can clear the entry fields after adding a food
        self.food_entry.delete(0, tk.END)
        self.protein_entry.delete(0, tk.END)
        self.carbs_entry.delete(0, tk.END)
        self.fat_entry.delete(0, tk.END)

    def log_food_entry(self):
        date = self.date_entry.get()
        food = self.food_entry.get()
        portion = float(self.portion_entry.get())

        with open(self.log_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, food, portion])

        # Optionally, you can clear the entry fields after logging a food entry
        self.date_entry.delete(0, tk.END)
        self.food_entry.delete(0, tk.END)
        self.portion_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = FoodTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()