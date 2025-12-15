# 🧮 Math Adventures  
### Adaptive Learning — AI-Inspired Prototype

---

## 📌 Project Overview

**Math Adventures** is a minimal **adaptive math learning system** designed for children aged **5–10**.  
The system dynamically adjusts the difficulty of math questions based on the learner’s **accuracy** and **response time**, helping maintain an optimal learning challenge.

This prototype focuses on **adaptive logic and reasoning**, rather than UI or visual design.

---

## 🎯 Objective

To demonstrate how **AI-inspired adaptive systems** can personalize learning difficulty in real time using:

- Performance tracking  
- Rule-based decision logic  
- Session-level analytics  

---

## 🧠 System Workflow

1. User enters name and starts with an initial difficulty (Easy).
2. The system generates a math puzzle.
3. User attempts the question.
4. System records:
   - Correctness
   - Time taken
5. Adaptive engine decides the next difficulty.
6. After the session, a performance summary is displayed.

---

## ⚙️ Core Components

| Component | Description |
|--------|-------------|
| Puzzle Generator | Creates math questions based on difficulty level |
| Performance Tracker | Records correctness and response time |
| Adaptive Engine | Adjusts difficulty dynamically |
| Progress Summary | Displays session analytics |

---

## 📊 Adaptive Logic (Key Highlight)

The system uses a **rolling window of the last 3 questions**:

- ⬆️ **Increase difficulty**  
  - Accuracy ≥ 80%  
  - Average response time is fast  

- ⬇️ **Decrease difficulty**  
  - Accuracy ≤ 40%  
  - Response time is slow  

- ➖ **Maintain difficulty** otherwise  

This approach:
- Handles noisy or inconsistent answers  
- Prevents abrupt difficulty changes  
- Is suitable for young learners  

---

## 🧩 Difficulty Levels

| Level | Characteristics |
|----|----------------|
| Easy | Small numbers, addition & subtraction (no negative results) |
| Medium | Larger numbers, includes multiplication |
| Hard | Multiplication and division |

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Interface:** Command Line (Console)  
- **Libraries:** Standard Python libraries only  

---

## 📂 Repository Structure

