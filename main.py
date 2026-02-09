"""
    Name: main.py
    Author: Paul Gray
    Created: 02/08/2026
    Purpose: Main program loop for Fitness Workout Tracker
"""


from datetime import datetime
import workout_tracker as tracker

def get_date():
    """Get today's date in YYYY-MM-DD format (or let user enter one)"""
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Today's date is: {today}")
    use_today = input("Use today's date? (y/n): ").strip().lower()
    if use_today == 'y' or use_today == '':
        return today
    
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if len(date) == 10 and date[4] == '-' and date[7] == '-':
            return date
        print("Please use YYYY-MM-DD format (example: 2025-02-10)")


def main():
    print("=====================================")
    print("   Fitness Workout Tracker - v0.1    ")
    print("=====================================\n")

    while True:
        print("1. Log a new workout")
        print("2. View all workouts")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == '1':
            print("\n--- Log New Workout ---")
            date = get_date()
            
            exercise = input("Exercise name: ").strip()
            if not exercise:
                print("Exercise name cannot be empty.")
                continue
                
            while True:
                try:
                    sets = int(input("Number of sets: "))
                    if sets <= 0:
                        print("Sets must be positive.")
                        continue
                    break
                except ValueError:
                    print("Please enter a number.")
                    
            while True:
                try:
                    reps = int(input("Number of reps: "))
                    if reps <= 0:
                        print("Reps must be positive.")
                        continue
                    break
                except ValueError:
                    print("Please enter a number.")
                    
            weight_input = input("Weight used (leave blank if bodyweight): ").strip()
            weight = None
            if weight_input:
                try:
                    weight = float(weight_input)
                except ValueError:
                    print("Invalid weight — saved without weight.")

            tracker.add_workout(date, exercise, sets, reps, weight)
            
        elif choice == '2':
            tracker.view_workouts()
            
        elif choice == '3':
            print("\nThanks for using Fitness Workout Tracker!")
            print("Your progress has been saved in memory for this session.\n")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()