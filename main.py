import tkinter as tk

window = tk.Tk()
window.resizable(False, False)
window.title("TIC TAC TOE")

tk.Label(window, text="TIC TAC TOE", font=("Arial", 25)).pack()
status_label = tk.Label(window, text="X's turn ", font=("Arial", 15), bg="green", fg='snow')
status_label.pack(fill=tk.X)


def play_again():
    global current_chr
    current_chr = "X"
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text="X's turn")
    play_again_button.pack_forget()


play_again_button = tk.Button(window, text="Play Again", command=play_again)

play_area = tk.Frame(window, width=300, height=300, bg="white")
current_chr = "X"
XO_points = []
X_points = []
O_points = []


class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O"
                status_label.configure(text="O's turn")
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X"
                status_label.configure(text="X's turn")
            if check_winner():
                winner = check_winner()
                status_label.configure(text=f"{winner} wins!")
                play_again_button.pack()

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            X_points.remove(self)
        elif self.value == "O":
            O_points.remove(self)
        self.value = None


def check_winner():
    for line in [[X_points, "X"], [O_points, "O"]]:
        for i in range(3):

            if all(point in line[0] for point in filter(lambda p: p.x == i + 1, XO_points)):
                return line[1]

            if all(point in line[0] for point in filter(lambda p: p.y == i + 1, XO_points)):
                return line[1]

        if all(point in line[0] for point in filter(lambda p: p.x == p.y, XO_points)):
            return line[1]
        if all(point in line[0] for point in filter(lambda p: p.x + p.y == 4, XO_points)):
            return line[1]

    return None


for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))

play_area.pack(pady=10, padx=10)
window.mainloop()
