import tkinter as tk
from tkinter import messagebox

class PythonQuestionsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Question for my queen or donkey heh")

        self.questions = [
            "How are you today?",
            "Did you take a shower today?",
            "Did you eat breakfast today?",
            "What did you do today?",
            "I missed you today and I love you so much.",
            "Are you ready for school tomorrow?"
        ]
        self.current_question = 0
        self.good_count = 0  # Track how many times "good" is answered

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text=self.questions[self.current_question], font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", self.next_question)

    def next_question(self, event=None):
        answer = self.answer_entry.get().strip()

        if self.current_question == 0:
            if answer.lower() == "good":
                self.good_count += 1
                if self.good_count == 2:
                    self.current_question += 1
                    self.update_question()
                    return
                else:
                    messagebox.showinfo("Response", "You don't need to lie, habibti. Tell me the truth.")
                    self.answer_entry.delete(0, tk.END)
                    return
            elif answer.lower() == "not good":
                self.current_question += 1
                self.update_question()
                return
            else:
                messagebox.showerror("Error", "girl its either you enter 'good' or 'not good'.")
                return
        elif self.current_question == 1:
            if "yes" in answer.lower():
                messagebox.showinfo("Response", "No wonder you smell good today!")
            elif "no" in answer.lower():
                messagebox.showinfo("Response", "Ew, go take a shower, you stinky!")
            else:
                messagebox.showerror("Error", "girl type 'yes' or 'no'.")
                return
        elif self.current_question == 2:
            if "yes" in answer.lower():
                messagebox.showinfo("Response", "Yummy in your tummy!")
            elif "no" in answer.lower():
                messagebox.showinfo("Response", "Aww, are you trying to be skinny, you big fatty?")
            else:
                messagebox.showerror("Error", "are you serious right now bruh is either 'yes' or 'no'.")
                return

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            messagebox.showinfo("Response", "I'm glad you answered me with honesty. Bye, my albeh! mwahhh")
            self.master.quit()

    def update_question(self):
        self.question_label.config(text=self.questions[self.current_question])
        self.answer_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = PythonQuestionsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
