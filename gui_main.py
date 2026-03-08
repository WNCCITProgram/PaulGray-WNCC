"""
    Name: gui_main.py
    Author: Paul Gray
    Created: 03/07/2026
    Purpose: Provides a graphical user interface (using Tkinter) 
             for the Fitness Workout Tracker, allowing users to 
             view, add, edit, delete workouts, and view basic statistics.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import workout_tracker as tracker

tracker.load_workouts()

def refresh_treeview(tree):
    tree.delete(*tree.get_children())
    for i, w in enumerate(tracker.get_all_workouts()):
        weight_str = f"{w['weight']:.1f}" if w['weight'] else "Bodyweight"
        tree.insert('', 'end', values=(i+1, w['date'], w['exercise'], w['sets'], w['reps'], weight_str))

def add_workout_window():
    add_win = tk.Toplevel(root)
    add_win.title("Add New Workout")
    
    tk.Label(add_win, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
    date_entry = tk.Entry(add_win)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    date_entry.grid(row=0, column=1)
    
    tk.Label(add_win, text="Exercise:").grid(row=1, column=0)
    exercise_entry = tk.Entry(add_win)
    exercise_entry.grid(row=1, column=1)
    
    tk.Label(add_win, text="Sets:").grid(row=2, column=0)
    sets_entry = tk.Entry(add_win)
    sets_entry.grid(row=2, column=1)
    
    tk.Label(add_win, text="Reps:").grid(row=3, column=0)
    reps_entry = tk.Entry(add_win)
    reps_entry.grid(row=3, column=1)
    
    tk.Label(add_win, text="Weight (optional):").grid(row=4, column=0)
    weight_entry = tk.Entry(add_win)
    weight_entry.grid(row=4, column=1)
    
    def submit_add():
        date = date_entry.get().strip()
        exercise = exercise_entry.get().strip()
        sets = sets_entry.get().strip()
        reps = reps_entry.get().strip()
        weight = weight_entry.get().strip() or None
        
        if not exercise or not sets or not reps:
            messagebox.showerror("Error", "Exercise, sets, and reps are required.")
            return
        
        try:
            sets = int(sets)
            reps = int(reps)
            weight = float(weight) if weight else None
        except ValueError:
            messagebox.showerror("Error", "Sets, reps, and weight must be numbers.")
            return
        
        tracker.add_workout(date, exercise, sets, reps, weight)
        refresh_treeview(tree)
        add_win.destroy()
        messagebox.showinfo("Success", "Workout added!")
    
    tk.Button(add_win, text="Add", command=submit_add).grid(row=5, column=0, columnspan=2, pady=10)

def edit_workout():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Select a workout to edit.")
        return
    
    index = int(tree.item(selected)['values'][0]) - 1
    w = tracker.get_all_workouts()[index]
    
    edit_win = tk.Toplevel(root)
    edit_win.title("Edit Workout")
    
    tk.Label(edit_win, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
    date_entry = tk.Entry(edit_win)
    date_entry.insert(0, w['date'])
    date_entry.grid(row=0, column=1)
    
    tk.Label(edit_win, text="Exercise:").grid(row=1, column=0)
    exercise_entry = tk.Entry(edit_win)
    exercise_entry.insert(0, w['exercise'])
    exercise_entry.grid(row=1, column=1)
    
    tk.Label(edit_win, text="Sets:").grid(row=2, column=0)
    sets_entry = tk.Entry(edit_win)
    sets_entry.insert(0, str(w['sets']))
    sets_entry.grid(row=2, column=1)
    
    tk.Label(edit_win, text="Reps:").grid(row=3, column=0)
    reps_entry = tk.Entry(edit_win)
    reps_entry.insert(0, str(w['reps']))
    reps_entry.grid(row=3, column=1)
    
    tk.Label(edit_win, text="Weight (optional):").grid(row=4, column=0)
    weight_entry = tk.Entry(edit_win)
    if w['weight']:
        weight_entry.insert(0, str(w['weight']))
    weight_entry.grid(row=4, column=1)
    
    def submit_edit():
        date = date_entry.get().strip()
        exercise = exercise_entry.get().strip()
        sets = sets_entry.get().strip()
        reps = reps_entry.get().strip()
        weight = weight_entry.get().strip() or None
        
        if not exercise or not sets or not reps:
            messagebox.showerror("Error", "Exercise, sets, and reps are required.")
            return
        
        try:
            sets = int(sets)
            reps = int(reps)
            weight = float(weight) if weight else None
        except ValueError:
            messagebox.showerror("Error", "Sets, reps, and weight must be numbers.")
            return
        
        tracker.update_workout(index, date, exercise, sets, reps, weight)
        refresh_treeview(tree)
        edit_win.destroy()
        messagebox.showinfo("Success", "Workout updated!")
    
    tk.Button(edit_win, text="Update", command=submit_edit).grid(row=5, column=0, columnspan=2, pady=10)

def delete_workout_confirm():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Select a workout to delete.")
        return
    
    if messagebox.askyesno("Confirm", "Delete this workout?"):
        index = int(tree.item(selected)['values'][0]) - 1
        tracker.delete_workout(index)
        refresh_treeview(tree)
        messagebox.showinfo("Success", "Workout deleted!")

def show_stats():
    stats = tracker.get_stats()
    messagebox.showinfo("Workout Stats", stats)

root = tk.Tk()
root.title("Fitness Workout Tracker - v1.0 (GUI)")
root.geometry("800x600")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Workout", command=add_workout_window).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit Workout", command=edit_workout).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Workout", command=delete_workout_confirm).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Show Stats", command=show_stats).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Exit", command=root.quit).grid(row=0, column=4, padx=5)

tree = ttk.Treeview(root, columns=('ID', 'Date', 'Exercise', 'Sets', 'Reps', 'Weight'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Date', text='Date')
tree.heading('Exercise', text='Exercise')
tree.heading('Sets', text='Sets')
tree.heading('Reps', text='Reps')
tree.heading('Weight', text='Weight')

tree.column('ID', width=50)
tree.column('Date', width=100)
tree.column('Exercise', width=200)
tree.column('Sets', width=50)
tree.column('Reps', width=50)
tree.column('Weight', width=100)

tree.pack(expand=True, fill='both', padx=10, pady=10)

refresh_treeview(tree)

root.mainloop()