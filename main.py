import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Мое GUI приложение")
        self.geometry("400x300")
        self.resizable(False, False)

        self.label = tk.Label(self, text="Привет! Введите ваше имя:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.entry.pack(pady=5)

        self.button = tk.Button(self, text="Нажми меня", font=("Arial", 12), command=self.on_click)
        self.button.pack(pady=15)

        self.result_label = tk.Label(self, text="", font=("Arial", 14, "bold"), fg="blue")
        self.result_label.pack(pady=10)

    def on_click(self):
        name = self.entry.get().strip()
        if name:
            self.result_label.config(text=f"Привет, {name}!")
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, введите имя!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
