# PaulGray-WNCC  
**Fitness Workout Tracker with Progress Visuals**

Hey everyone! 👋  

For my semester project, I'm working on a **Fitness Workout Tracker** — something to help me (and hopefully others) actually stick with workouts by making tracking easy and motivating.  

### Why this project?  
I go to the gym pretty regularly, but I always forget what weights I used last time or whether I'm actually getting stronger. Spreadsheets get messy, phone notes are all over the place, and most apps feel either too complicated or paywalled. I wanted something simple I could use myself: log workouts quickly, see my history, and eventually get cool charts showing progress so I stay motivated.  

Right now the goal is a clean, useful app for logging strength training (exercises, sets, reps, weights) with room to grow into body stats, cardio, and visuals later.

### Current Status (March 2026 Update)  
Started with a super basic console version in Python back in February — just to figure out how the data should work and what the flow feels like. That version let me log workouts and view them in text, but everything was in memory (gone when I closed the program).

**Big step this week:** I turned it into a **GUI desktop app** using Tkinter! Now it actually feels like real software:  
- Nice window with buttons and a table showing all workouts  
- Add new workouts (date auto-fills today's, but you can change it)  
- Edit or delete entries if I mess something up  
- Basic stats popup (total workouts, unique exercises, total volume lifted, max bench press weight)  
- Saves everything automatically to a `workouts.json` file so progress doesn't disappear  

It's still Python for now, but this GUI version is way more usable than the console one. Feels like real progress! 💪  

Current files:  
- [`workout_tracker.py`](workout_tracker.py) — handles all the data stuff (add, edit, delete, save/load, stats)  
- [`gui_main.py`](gui_main.py) — launches the actual app window  

(Old console version is archived as `main.py` if I ever want to look back.)

### Final Goals (by end of semester)  
- Switch everything over to full **MERN stack** web app  
- User accounts (sign up / login)  
- Log strength workouts + maybe cardio sessions  
- Track body stats (weight, measurements, etc.)  
- Multiple progress charts (weight over time, max lifts, volume trends) using Chart.js  
- Clean, mobile-friendly design with Tailwind CSS  
- Deploy it somewhere so I can actually use it from my phone  

### Technologies (current + planned)  
**Right now (Python phase):**  
- Python 3  
- Tkinter (for the GUI)  
- JSON file for saving data  

**Next phase (web version):**  
- MERN Stack (MongoDB, Express.js, React, Node.js)  
- React + Tailwind CSS  
- Chart.js for visuals  
- JWT for authentication  
- Probably React Router, Axios, etc.  

### Resources & Tutorials I've Used  
- Tkinter basics from Python docs and a couple Real Python articles  
- JSON handling — straight from Python docs  
- Some YouTube videos on building simple GUIs in Python  
- Planning ahead: MERN full-stack tutorials (especially the exercise tracker ones on YouTube)  
- Chart.js docs for when I get to visuals  

### AI Help  
I used Grok (from xAI) a bunch to help figure out the Tkinter layout, add the edit/delete features, and get the JSON saving working smoothly. It saved me a ton of trial-and-error time. All the code decisions and structure are still mine, but credit where it's due — thanks Grok!

### Next Steps  
In the next couple weeks I want to:  
- Add better date picking/validation  
- Maybe a simple progress chart in Python (matplotlib?) as a test  
- Start the React frontend setup  
- Clean up the UI a bit more  

I'll keep updating this README with screenshots and new features as I go.  

Feel free to check it out, run it, or drop feedback!  

Happy lifting (and coding)! 💪🏋️‍♂️
