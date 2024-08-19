import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"], "answer": "Harper Lee"},
            {"question": "What is the smallest prime number?", "options": ["1", "2", "3", "5"], "answer": "2"},
            {"question": "What is the chemical symbol for Gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": "Au"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
            # Add more questions here
        ]
        
        self.current_question_index = 0
        self.score = 0
        
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.label_question = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.label_question.pack(pady=10)

        self.var_answer = tk.StringVar()
        
        self.options_frame = tk.Frame(self.master)
        self.options_frame.pack(pady=10)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.var_answer, value="", font=("Helvetica", 12))
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)
        
        self.button_next = tk.Button(self.master, text="Next", command=self.check_answer)
        self.button_next.pack(pady=10)

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.label_question.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.radio_buttons[i].config(text=option, value=option)
            self.var_answer.set(None)
        else:
            self.show_results()

    def check_answer(self):
        selected_answer = self.var_answer.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer.")
            return
        
        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_answer == correct_answer:
            self.score += 1
        
        self.current_question_index += 1
        self.show_question()

    def show_results(self):
        messagebox.showinfo("Quiz Completed", f"Your score is {self.score} out of {len(self.questions)}")
        self.master.quit()

def main():
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()