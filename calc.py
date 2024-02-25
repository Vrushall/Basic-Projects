import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    answer.delete(1.0, "end")
    answer.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        answer.delete(1.0, "end")
        answer.insert(1.0, result)
    except:
        clear()
        answer.insert(1.0, "Error")

def clear():
    global calculation
    calculation = ""
    answer.delete(1.0, "end")

window = tk.Tk()
window.geometry("450x250")

answer = tk.Text(window, height = 5, width = 50)
answer.grid(columnspan = 5)
answer.configure(font = ("Arial", 12))

btn_1 = tk.Button(window, text = "1", command = lambda: add_to_calculation(1), width = 10)
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(window, text = "2", command = lambda: add_to_calculation(2), width = 10)
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(window, text = "3", command = lambda: add_to_calculation(3), width = 10)
btn_3.grid(row = 2, column = 3)
btn_4 = tk.Button(window, text = "4", command = lambda: add_to_calculation(4), width = 10)
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(window, text = "5", command = lambda: add_to_calculation(5), width = 10)
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(window, text = "6", command = lambda: add_to_calculation(6), width = 10)
btn_6.grid(row = 3, column = 3)
btn_7 = tk.Button(window, text = "7", command = lambda: add_to_calculation(7), width = 10)
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(window, text = "8", command = lambda: add_to_calculation(8), width = 10)
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(window, text = "9", command = lambda: add_to_calculation(9), width = 10)
btn_9.grid(row = 4, column = 3)
btn_0 = tk.Button(window, text = "0", command = lambda: add_to_calculation(0), width = 10)
btn_0.grid(row = 5, column = 2)

btn_plus = tk.Button(window, text = "+", command = lambda: add_to_calculation("+"), width = 10)
btn_plus.grid(row = 2, column = 4)
btn_minus = tk.Button(window, text = "-", command = lambda: add_to_calculation("-"), width = 10)
btn_minus.grid(row = 3, column = 4)
btn_div = tk.Button(window, text = "/", command = lambda: add_to_calculation("/"), width = 10)
btn_div.grid(row = 4, column = 4)
btn_mul = tk.Button(window, text = "*", command = lambda: add_to_calculation("*"), width = 10)
btn_mul.grid(row = 5, column = 4)

btn_open = tk.Button(window, text = "(", command = lambda: add_to_calculation("("), width = 10)
btn_open.grid(row = 5, column = 1)
btn_close = tk.Button(window, text = ")", command = lambda: add_to_calculation(")"), width = 10)
btn_close.grid(row = 5, column = 3)

btn_clr = tk.Button(window, text = "C", command = clear, width = 20)
btn_clr.grid(row = 6, column = 1, columnspan = 2)
btn_equal = tk.Button(window, text = "=", command = evaluate, width = 20)
btn_equal.grid(row = 6, column = 3, columnspan = 2)
window.mainloop()
