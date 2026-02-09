"""
    Name: workout_tracker.py
    Author: Paul Gray
    Created: 02/08/2026
    Purpose: Basic data storage and functions for the Fitness Workout Tracker.
"""

workouts = []  # List to hold all workout entries (in memory for now)

def add_workout(date, exercise, sets, reps, weight=None):
    """
    Add a new workout entry.
    
    Parameters:
        date (str): Date of the workout (e.g. "2025-02-10")
        exercise (str): Name of the exercise (e.g. "Bench Press")
        sets (int): Number of sets
        reps (int): Number of reps per set
        weight (float, optional): Weight used (in lbs or kg)
    """
    workout = {
        "date": date,
        "exercise": exercise.strip().title(),
        "sets": int(sets),
        "reps": int(reps),
        "weight": float(weight) if weight else None
    }
    
    workouts.append(workout)
    print(f"\nAdded: {workout['exercise']} - {workout['sets']}×{workout['reps']}"
          f" ({workout['weight']} kg/lbs)" if workout['weight'] else "")


def view_workouts():
    """Display all logged workouts in a simple readable format."""
    if not workouts:
        print("\nNo workouts logged yet.\n")
        return
    
    print("\n=== Your Workouts ===\n")
    for i, w in enumerate(workouts, 1):
        weight_str = f" @ {w['weight']} kg/lbs" if w['weight'] else ""
        print(f"{i}. {w['date']} | {w['exercise']:<20} | "
              f"{w['sets']} sets × {w['reps']} reps{weight_str}")
    print()


def get_all_workouts():
    """Return the list of workouts (useful for future features)"""
    return workouts