from tkinter import *

spaceX = 0
spaceY = 0

#Funciones
def numberButton(root, varStr, text):
    button = Button(root, text=text, font=("Hack", 15), height=3, width=6, command= lambda:varStr.set(varStr.get() + text))
    button.config(bg="#343957", fg="#ffffff", highlightthickness=0, highlightbackground="#343957", activebackground="#454A68", activeforeground="#ffffff", cursor="hand2", padx=spaceX, pady=spaceY)
    return button

def buttonClear(root, varStr, varLaststr):
    def clear():
        varStr.set("")
        varLaststr.set("")
    button = Button(root, text="AC", font=("Hack", 15), height=3, width=6, command= clear)
    button.config(bg="#FF3664", fg="#ffffff", highlightthickness=0, highlightbackground="#4F556F", activebackground="#F390A6", activeforeground="#ffffff", cursor="hand2", padx=spaceX, pady=spaceY)
    return button

def buttonMoreminor(root, varStr):
    def convert():
        re = float(varStr.get()) * (0-1)
        if re%1 == 0: return varStr.set(str(int(re)))
        else: return varStr.set(str(re)) 
    button = Button(root, text="±", font=("Hack", 22), height=2, width=4, command= convert)
    button.config(bg="#4F556F", fg="#FF3664", highlightthickness=0, highlightbackground="#4F556F", activebackground="#676D87", activeforeground="#ffffff", cursor="hand2", padx=spaceX, pady=spaceY)
    return button

def operButton(root, varStr, varLaststr, text):
    def export():
        varLaststr.set(varStr.get() + text)
        varStr.set("")
    button = Button(root, text=text, font=("Hack", 22), height=2, width=4, command= export)
    button.config(bg="#4F556F", fg="#FF3664", highlightthickness=0, highlightbackground="#4F556F", activebackground="#676D87", activeforeground="#ffffff", cursor="hand2", padx=spaceX, pady=spaceY)
    return button

def minorButton(root, varStr, varLaststr):
    def isMinor():
        try:
            if varStr.get()[-1].isdigit():
                varLaststr.set(varStr.get() + "—")
                varStr.set("")
            else: varStr.set(varStr.get() + "-")
        except: varStr.set(varStr.get() + "-")

    button = Button(root, text="-", font=("Hack", 22), height=2, width=4, command= isMinor)
    button.config(bg="#4F556F", fg="#FF3664", highlightthickness=0, highlightbackground="#4F556F", activebackground="#676D87", activeforeground="#ffffff", cursor="hand2", padx=spaceX, pady=spaceY)
    return button

def sameButton(root, varStr, varLaststr, text): 
    def operate():
        def insertResult(re):
            varLaststr.set("")
            if re%1 == 0: varStr.set(str(int(re)))
            else: varStr.set(str(round(re, 2))) 
            
        num1 = float(varLaststr.get().rstrip(varLaststr.get()[-1]))
        print(num1)
        num2 = float(varStr.get())
        print(num2)
        oper = varLaststr.get()[-1]
        print(oper)

        try:
            if oper == "+":
                re = num1 + num2
                print(re)
                insertResult(re)
            elif oper == "—":
                re = num1 - num2
                print(re)
                insertResult(re)
            elif oper == "×":
                re = num1 * num2
                print(re)
                insertResult(re)
            elif oper == "÷":
                re = num1 / num2
                print(re)
                insertResult(re)
            else: 
                varLaststr.set("")
                varStr.set("ERROR")
        except:
            varLaststr.set("")
            varStr.set("ERROR")

    button = Button(root, text=text, font=("Hack", 23), height=4, width=4, command= operate)
    button.config(bg="#FF3664", fg="#ffffff", highlightthickness=0, highlightbackground="#4F556F", activebackground="#F390A6", activeforeground="#ffffff", cursor="hand2", padx=spaceX, pady=spaceY)
    return button


root = Tk()
root.title("Calculadora")
root.resizable(False, False)
root.config(bg="#313656", highlightthickness=0, highlightbackground="#313656")


varStr = StringVar()
varLaststr = StringVar()

#Label
labelPrincipal = Label(root, anchor="e", textvariable=varStr)
labelPrincipal.config(bg="#2C3043", fg="#ffffff", font=("Hack", 42), width=9)
labelUp = Label(root, anchor="e", textvariable=varLaststr)
labelUp.config(bg="#2C3043", fg="#6A6E73", font=("Hack", 14), width=28)#28
labelDecorator = Label(root)
labelDecorator.config(bg="#2C3043", fg="#ffffff", font=("Hack", 14), pady=spaceY, width=28)

#Number Buttons
button9 = numberButton(root, varStr, "9")
button8 = numberButton(root, varStr, "8")
button7 = numberButton(root, varStr, "7")
button6 = numberButton(root, varStr, "6")
button5 = numberButton(root, varStr, "5")
button4 = numberButton(root, varStr, "4")
button3 = numberButton(root, varStr, "3")
button2 = numberButton(root, varStr, "2")
button1 = numberButton(root, varStr, "1")
button0 = numberButton(root, varStr, "0")

#Operator Buttons
buttonMore = operButton(root, varStr, varLaststr, "+")
buttonMinor = minorButton(root, varStr, varLaststr)
buttonMultiply = operButton(root, varStr, varLaststr, "×")
buttonDivide = operButton(root, varStr, varLaststr, "÷")
buttonSame = sameButton(root, varStr, varLaststr, text="=")

#Botones funcionales
buttonPoint = numberButton(root, varStr, ".")
buttonClear = buttonClear(root, varStr, varLaststr)
buttonMoreminor = buttonMoreminor(root, varStr)

#Grid
labelUp.grid(row=0, column=0, columnspan=4, sticky="e")
labelPrincipal.grid(row=1, column=0, columnspan=4, sticky="e")
labelDecorator.grid(row=2, column=0, columnspan=4, sticky="e")

button9.grid(row=4, column=2)
button8.grid(row=4, column=1)
button7.grid(row=4, column=0)
button6.grid(row=5, column=2)
button5.grid(row=5, column=1)
button4.grid(row=5, column=0)
button3.grid(row=6, column=2)
button2.grid(row=6, column=1)
button1.grid(row=6, column=0)

button0.config(width=14, font=("Hack", 14))
button0.grid(row=7, column=0, columnspan=2)

buttonSame.grid(row=6, rowspan=5, column=3)

buttonMore.grid(row=5, column=3)
buttonMinor.grid(row=4, column=3)
buttonMultiply.grid(row=3, column=3)
buttonDivide.grid(row=3, column=2)

buttonPoint.grid(row=7, column=2)
buttonClear.grid(row=3, column=0)
buttonMoreminor.grid(row=3, column=1)

root.mainloop()
