from tkinter import *
from tkinter import ttk
import os
import pathlib

#Current path script is in
currentPath = pathlib.Path(__file__).parent.resolve()


#Window Geometry
Window = Tk()
Window.title("FMA Calculator")
Window.geometry("450x450")

#App icon
imgicon = PhotoImage(file=os.path.join(currentPath,'Physics.png'))
Window.tk.call('wm', 'iconphoto', Window._w, imgicon)  

##################

#Calculate Force
def calculateForce():
    mass = float(massEntryFT.get())
    acceleration = float(accelerationEntryFT.get())

    force = (mass * acceleration)

    forceOutput = Label(forceTab, text = (force, "N"))
    forceCanvas.create_window(250,250, window = forceOutput)

    unitLabel = Label(forceTab, text = "Force in Newtons")
    forceCanvas.create_window(250,230, window = unitLabel)

    return force

#Calculate Acceleration
def calculateMass():
    force = float(forceEntryMT.get())
    acceleration = float(accelerationEntryMT.get())

    mass = (force / acceleration)

    massOutput = Label(massTab, text = (mass, "Kg"))
    massCanvas.create_window(250,250, window = massOutput)

    unitLabel = Label(massTab, text = "Mass in Kg")
    massCanvas.create_window(250,230, window = unitLabel)

    return mass

def calculateAcceleration():
    force = float(forceEntryAT.get())
    mass = float(massEntryAT.get())

    acceleration = (force / mass)

    accelerationOutput = Label(accelerationTab, text = (acceleration, "M/s/s"))
    accelerationCanvas.create_window(250,250, window = accelerationOutput)

    unitLabel = Label(accelerationCanvas, text = "Acceleration in M/s/s")
    accelerationCanvas.create_window(250,230, window = unitLabel)

    return acceleration

##################
#Tabs
tabList = ttk.Notebook(Window)

forceTab = Frame(tabList)
massTab = Frame(tabList)
accelerationTab = Frame(tabList)

tabList.add(forceTab, text = "Force")
tabList.add(massTab, text = "Mass")
tabList.add(accelerationTab, text = "Acceleration")
tabList.pack(expand = 1, fill = "both")

##################


##-----Force Tab------##
forceCanvas = Canvas(forceTab, width = 400, height = 400)
forceCanvas.pack()

#Force Tab Labels/Entry Fields
#FT = Force Tab
massLabelFT = Label(forceTab, text="Mass in Kg")
forceCanvas.create_window(73,43, window = massLabelFT)

massVariableLabelFT = Label(forceTab, text = "m")
forceCanvas.create_window(8, 70, window = massVariableLabelFT)

massEntryFT = Entry(forceTab)
forceCanvas.create_window(83,70, window = massEntryFT)

accelerationLabelFT = Label(forceTab, text = "Acceleration in M/s/s")
forceCanvas.create_window(80, 103, window = accelerationLabelFT)

accelerationVariableLabelFT = Label(forceTab, text = "a")
forceCanvas.create_window(8, 123, window = accelerationVariableLabelFT)

accelerationEntryFT = Entry(forceTab)
forceCanvas.create_window(83, 123, window = accelerationEntryFT)

formulaLabelFT = Label(forceTab, text = "Uses F = MA, to solve for F")
forceCanvas.create_window(200,12, window = formulaLabelFT)

#Force Tab Buttons
#Force tab calculate button
forceTabCB = Button(forceTab, text = "Calculate", command = calculateForce)
forceCanvas.create_window(45, 250, window = forceTabCB)

#Force copy button
def copyTooF():
    Tk.clipboard_clear(forceTab)
    Tk.clipboard_append(forceTab, calculateForce())

forceCopyButton = Button(forceTab, text = "Copy", command = copyTooF)
forceCanvas.create_window(32, 300, window = forceCopyButton)

##################


##-----Mass Tab------##
massCanvas = Canvas(massTab, width = 400, height = 400)
massCanvas.pack()

#Mass Tab Labels/Entry Fields
#MT = Mass Tab
forceLabelMT = Label(massTab, text="Force in Newtons")
massCanvas.create_window(80,43, window = forceLabelMT)

forceVariableLabelMT = Label(massTab, text = "f")
massCanvas.create_window(8, 70, window = forceVariableLabelMT)

forceEntryMT = Entry(massTab)
massCanvas.create_window(83,70, window = forceEntryMT)

accelerationLabelMT = Label(massTab, text = "Acceleration in M/s/s")
massCanvas.create_window(80, 103, window = accelerationLabelMT)

accelerationVariableLabelMT = Label(massTab, text = "a")
massCanvas.create_window(8, 123, window = accelerationVariableLabelMT)

accelerationEntryMT = Entry(massTab)
massCanvas.create_window(83, 123, window = accelerationEntryMT)

formulaLabelMT = Label(massTab, text = "Uses M = F/A, to solve for M")
massCanvas.create_window(200,12, window = formulaLabelMT)

#Mass Tab Buttons
#Mass tab calculate button
massTabCB = Button(massTab, text = "Calculate", command = calculateMass)
massCanvas.create_window(45,250, window = massTabCB)

#Mass copy buttondef copyTooA():
def copyTooM():
    Tk.clipboard_clear(massTab)
    Tk.clipboard_append(massTab, calculateMass())

massCopyButton = Button(massTab, text = "Copy", command = copyTooM)
massCanvas.create_window(32, 300, window = massCopyButton)

##################


##-----Acceleration Tab------##
accelerationCanvas = Canvas(accelerationTab, width = 400, height = 400)
accelerationCanvas.pack()

#Acceleration Tab Labels/Entry Fields
#AT = Acceleration Tab
forceLabelAT = Label(accelerationTab, text="Force in Newtons")
accelerationCanvas.create_window(80,43, window = forceLabelAT)

forceVariableLabelAT = Label(accelerationTab, text = "f")
accelerationCanvas.create_window(8, 70, window = forceVariableLabelAT)

forceEntryAT = Entry(accelerationTab)
accelerationCanvas.create_window(83,70, window = forceEntryAT)

massLabelAT = Label(accelerationTab, text = "Mass in Kg")
accelerationCanvas.create_window(80, 103, window = massLabelAT)

massVariableLabelAT = Label(accelerationTab, text = "m")
accelerationCanvas.create_window(8, 123, window = massVariableLabelAT)

massEntryAT = Entry(accelerationTab)
accelerationCanvas.create_window(83, 123, window = massEntryAT)

formulaLabelAT = Label(accelerationTab, text = "Uses A = F/M, to solve for A")
accelerationCanvas.create_window(200,12, window = formulaLabelAT)

#Acceelration Tab Buttons
#Acceleration tab calculate button
accelerationTabCB = Button(accelerationTab, text = "Calculate", command = calculateAcceleration)
accelerationCanvas.create_window(45,250, window = accelerationTabCB)

#Acceleration Copy Button
def copyTooA():
    Tk.clipboard_clear(accelerationTab)
    Tk.clipboard_append(accelerationTab, calculateAcceleration())

accelerationCopyButton = Button(accelerationTab, text = "Copy", command = copyTooA)
accelerationCanvas.create_window(32, 300, window = accelerationCopyButton)


##################
Window.resizable(False,False)
Window.mainloop()