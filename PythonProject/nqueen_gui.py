import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import time

print("NEW VERSION RUNNING")


class NQueenGUI:
    def __init__(self, root, n):
        self.root = root
        self.n = n
        self.board = [-1] * n
        self.cells = []
        self.steps = 0

        self.root.geometry("520x600")

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        self.info_label = tk.Label(
            root,
            text="",
            font=("Segoe UI", 12, "bold"),
            fg="blue"
        )
        self.info_label.pack(pady=10)

        self.cell_size = 500 // n

        self.draw_board()

        start_time = time.time()

        solved = self.solve_n_queen(0)

        end_time = time.time()

        execution_time = end_time - start_time

        if solved:
            self.display_queens()

            self.info_label.config(
                text=f"Execution Time: {execution_time:.6f} seconds | Backtracking Steps: {self.steps}"
            )

        else:
            messagebox.showerror("No Solution", "No solution exists for this N")

    def draw_board(self):

        for row in range(self.n):

            row_cells = []

            for col in range(self.n):

                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"

                rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color
                )

                row_cells.append(rect)

            self.cells.append(row_cells)

    def display_queens(self):

        for row in range(self.n):

            col = self.board[row]

            x = col * self.cell_size + self.cell_size // 2
            y = row * self.cell_size + self.cell_size // 2

            self.canvas.create_text(
                x,
                y,
                text="♛",
                font=("Segoe UI Emoji", 40),
                fill="black"
            )

    def is_safe(self, row, col):

        for i in range(row):

            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row):
                return False

        return True

    def solve_n_queen(self, row):

        if row == self.n:
            return True

        for col in range(self.n):

            self.steps += 1

            if self.is_safe(row, col):

                self.board[row] = col

                if self.solve_n_queen(row + 1):
                    return True

                self.board[row] = -1

        return False


# SOLVE BUTTON
def start():

    try:
        n = int(entry.get())

        if n < 4:
            messagebox.showerror("Invalid", "Enter N ≥ 4")
            return

        window = tk.Toplevel()
        window.title("♛ N-Queen Visualization")

        NQueenGUI(window, n)

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter numbers like 4, 5, 8")


# RESET BUTTON
def reset_input():
    entry.delete(0, tk.END)


# GRAPH FEATURE
def show_graph():

    n_values = [4, 5, 6, 7, 8]
    solutions = [2, 10, 4, 40, 92]

    plt.figure()

    plt.plot(n_values, solutions, marker="o")

    for i in range(len(n_values)):
        plt.text(n_values[i], solutions[i], str(solutions[i]))

    plt.title("N-Queen Problem Analysis")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Number of Solutions")

    plt.grid(True)

    plt.show()


# ALGORITHM EXPLANATION
def explain_algorithm():

    messagebox.showinfo(
        "How Result Was Generated",

        "The N-Queen problem is solved using the Backtracking Algorithm.\n\n"

        "Steps:\n"
        "1. Place a queen in the first row.\n"
        "2. Check if the position is safe.\n"
        "3. If safe, move to the next row.\n"
        "4. If conflict occurs, backtrack.\n"
        "5. Try another column.\n\n"

        "The process continues until all queens are placed safely."
    )


# MAIN WINDOW
root = tk.Tk()

root.title("♛ N-Queen Solver ♛")
root.geometry("500x420")
root.configure(bg="#2c3e50")


title = tk.Label(
    root,
    text="♛ N-Queen Chess Solver ♛",
    font=("Segoe UI", 22, "bold"),
    bg="#2c3e50",
    fg="white"
)

title.pack(pady=20)


frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=20)


label = tk.Label(
    frame,
    text="Enter value of N:",
    font=("Segoe UI", 14),
    bg="#2c3e50",
    fg="white"
)

label.grid(row=0, column=0, padx=10)


entry = tk.Entry(
    frame,
    font=("Segoe UI", 16),
    width=10,
    justify="center",
    bd=3
)

entry.grid(row=0, column=1, padx=10)


solve_btn = tk.Button(
    root,
    text="Solve ♛",
    font=("Segoe UI", 14, "bold"),
    bg="#27ae60",
    fg="white",
    padx=20,
    pady=8,
    command=start
)

solve_btn.pack(pady=10)


reset_btn = tk.Button(
    root,
    text="Reset 🔄",
    font=("Segoe UI", 12),
    bg="#e74c3c",
    fg="white",
    command=reset_input
)

reset_btn.pack(pady=5)


graph_btn = tk.Button(
    root,
    text="Show Result Graph 📊",
    font=("Segoe UI", 12),
    command=show_graph
)

graph_btn.pack(pady=5)


explain_btn = tk.Button(
    root,
    text="How Result Was Generated ❓",
    font=("Segoe UI", 12),
    command=explain_algorithm
)

explain_btn.pack(pady=5)


root.mainloop()