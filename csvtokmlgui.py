import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename

def browse():
    global infile
    infile = askopenfilename()


def genkml(outfile="gui.kml"):
    kml = simplekml.Kml()
    df=pandas.read_csv(infile)
    for lon,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(coords=[(lon,lat)])
    kml.save(outfile)


root = tkinter.Tk()
root.title("Browse File ")
label = tkinter.Label(root, text="Browse the csv file here")
label.pack()
button = tkinter.Button(root, text="Browse", command=browse)
button.pack()
gen = tkinter.Button(root, text="Generate kml file", command=genkml)
gen.pack()
root.mainloop()
