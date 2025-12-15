🧮 Math Adventures — Adaptive Learning Prototype
📌 Overview

This project is a minimal adaptive math learning system designed for children aged 5–10.
The system dynamically adjusts the difficulty of math puzzles based on the learner’s accuracy and response time, keeping them in an optimal challenge zone.

The focus of this prototype is on adaptive logic and reasoning, not UI or visuals.

🎯 Objective

To demonstrate how AI-inspired adaptive logic can personalize learning difficulty in real time using:

Performance tracking

Rule-based decision making

Session-level analytics

🧠 How the System Works
1️⃣ Puzzle Generation

Generates math problems based on difficulty:

Easy → Small numbers, addition/subtraction (no negative results)

Medium → Larger numbers, includes multiplication

Hard → Multiplication and division

2️⃣ Performance Tracking

For every question, the system logs:

Correct / Incorrect response

Time taken to answer

3️⃣ Adaptive Engine (Core Logic)

Uses a rolling window of the last 3 questions

Difficulty adjustment rules:

Increase difficulty if accuracy ≥ 80% and average time is fast

Decrease difficulty if accuracy ≤ 40% or response time is slow

Otherwise, maintain current difficulty

This prevents sudden jumps and handles noisy user behavior.

4️⃣ Session Summary

At the end of the session, the system displays:

Overall accuracy

Average response time

Recommended difficulty level for the next session



User
 ↓
Puzzle Generator → Performance Tracker
 ↓
Adaptive Engine (Rule-Based)
 ↓
Next Difficulty Selection
 ↓
Session Summary

