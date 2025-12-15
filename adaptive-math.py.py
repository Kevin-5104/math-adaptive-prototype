import random
import time

# Difficulty levels
DIFFICULTIES = ["Easy", "Medium", "Hard"]

current_difficulty = "Easy"
history = []

def generate_puzzle(difficulty):
    if difficulty == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        if b > a:
            a, b = b, a
        op = random.choice(["+", "-"])

    elif difficulty == "Medium":
        a, b = random.randint(10, 50), random.randint(2, 10)
        op = random.choice(["+", "-", "*"])

    else:  # Hard
        a, b = random.randint(20, 100), random.randint(2, 10)
        op = random.choice(["*", "/"])
        if op == "/":
            a = a * b

    question = f"{a} {op} {b}"
    return question, int(eval(question))

def update_difficulty():
    global current_difficulty
    if len(history) < 3:
        return

    recent = history[-3:]
    accuracy = sum(h["correct"] for h in recent) / 3
    avg_time = sum(h["time"] for h in recent) / 3

    if accuracy >= 0.8 and avg_time < 6:
        current_difficulty = DIFFICULTIES[min(DIFFICULTIES.index(current_difficulty) + 1, 2)]
    elif accuracy <= 0.4 or avg_time > 10:
        current_difficulty = DIFFICULTIES[max(DIFFICULTIES.index(current_difficulty) - 1, 0)]

# ---- MAIN FLOW ----
name = input("Enter student name: ")
print("Starting difficulty: Easy", flush=True)


for i in range(10):
    q, ans = generate_puzzle(current_difficulty)
    print(f"\nQ{i+1} ({current_difficulty}): {q}")

    start = time.time()
    user_ans = int(input("Your answer: "))
    t = time.time() - start

    correct = user_ans == ans
    history.append({"correct": correct, "time": t})

    print("Correct!" if correct else f"Wrong! Answer: {ans}")
    update_difficulty()

# ---- SUMMARY ----
accuracy = sum(h["correct"] for h in history) / len(history) * 100
avg_time = sum(h["time"] for h in history) / len(history)

print("\n--- Session Summary ---")
print("Student:", name)
print("Accuracy:", round(accuracy, 2), "%")
print("Average Time:", round(avg_time, 2), "seconds")
print("Recommended Level:", current_difficulty)
