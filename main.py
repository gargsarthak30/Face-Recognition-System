from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame()
bottomFrame.pack(side=BOTTOM)
heading = Label(topFrame, text="Face Recognition System using\nFACENET")
heading.pack()

powerCamera = Button(topFrame, text="Start Camera", fg="red")
powerCamera.pack()
existingFaces = Button(bottomFrame, text="Show Existing Faces", fg="blue")
existingFaces.pack(side=LEFT)
facenet = Button(bottomFrame, text="Facenet's Working", fg="blue")
facenet.pack(side=LEFT)
root.mainloop()

