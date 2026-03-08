"""
    Name: workout_tracker.py
    Author: Paul Gray
    Created: 02/08/2026
    Updated: 03/07/2026
    Purpose: Manages workout data storage, persistence (JSON file), and core operations including add, update, delete, and basic statistics.
"""

import json
import os

DATA_FILE = 'workouts.json'
workouts = []

def load_workouts():
    global workouts
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                workouts = json.load(f)
        except json.JSONDecodeError:
            workouts = []
    else:
        workouts = []

def save_workouts():
    with open(DATA_FILE, 'w') as f:
        json.dump(workouts, f, indent=4)

def add_workout(date, exercise, sets, reps, weight=None):
    workout = {
        "date": date,
        "exercise": exercise.strip().title(),
        "sets": int(sets),
        "reps": int(reps),
        "weight": float(weight) if weight else None
    }
    workouts.append(workout)
    save_workouts()

def update_workout(index, date, exercise, sets, reps, weight=None):
    if 0 <= index < len(workouts):
        workouts[index] = {
            "date": date,
            "exercise": exercise.strip().title(),
            "sets": int(sets),
            "reps": int(reps),
            "weight": float(weight) if weight else None
        }
        save_workouts()

def delete_workout(index):
    if 0 <= index < len(workouts):
        del workouts[index]
        save_workouts()

def get_all_workouts():
    return sorted(workouts, key=lambda w: w['date'])

def get_stats():
    if not workouts:
        return "No workouts logged yet."
    
    total_workouts = len(workouts)
    exercises = set(w['exercise'] for w in workouts)
    total_volume = sum(w['sets'] * w['reps'] * (w['weight'] or 0) for w in workouts)
    
    stats = f"Total Workouts: {total_workouts}\n"
    stats += f"Unique Exercises: {len(exercises)}\n"
    stats += f"Total Volume (sets × reps × weight): {total_volume:.2f} units\n"
    
    bench_press = [w for w in workouts if w['exercise'] == 'Bench Press']
    if bench_press:
        max_weight = max((w['weight'] or 0) for w in bench_press)
        stats += f"Max Bench Press Weight: {max_weight:.2f} kg/lbs\n"
    
    return stats