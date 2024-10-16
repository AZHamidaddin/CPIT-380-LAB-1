import imageLogic
from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Lab 1 Assignment")


def change_color_window():

    def change_color_handler():
        rFloat = float(rValue.get())
        gFloat = float(gValue.get())
        bFloat = float(bValue.get())

        imageLogic.change_color(rFloat, gFloat, bFloat)

        t.destroy()

    t = Toplevel(root, pady=10, padx=10)
    t.title('RGB Values')

    ttk.Label(t, text="Enter RGB Values").grid(column=0, row=0)

    r = StringVar()
    rValue = ttk.Entry(t, textvariable=r)

    rValue.grid(column=0, row=1)

    g = StringVar()
    gValue = ttk.Entry(t, textvariable=g)
    gValue.grid(column=1, row=1)

    b = StringVar()
    bValue = ttk.Entry(t, textvariable=b)
    bValue.grid(column=2, row=1)

    ttk.Button(t, text="Submit", command=change_color_handler).grid(column=2, row=0)


def rotate_image_window():

    def rotate_image_handler(angle):
        imageLogic.rotate_image(angle)

        t.destroy()

    t = Toplevel(root, pady=10, padx=10)
    t.title('Rotate Options')

    ttk.Label(t, text="Choose Rotation Option").grid(column=0, row=0)

    ttk.Button(t, text="90", command=lambda: rotate_image_handler(90)).grid(column=1, row=0)

    ttk.Button(t, text="180", command=lambda: rotate_image_handler(180)).grid(column=2, row=0)

    ttk.Button(t, text="270", command=lambda: rotate_image_handler(270)).grid(column=3, row=0)


def scale_image_window():

    def scale_image_handler():
        scale_factor = float(scaleValue.get())

        imageLogic.scale(scale_factor)

        t.destroy()

    t = Toplevel(root, pady=10, padx=10)
    t.title('Scale Options')

    ttk.Label(t, text="Choose Scale Factor (Higher = Larger)").grid(column=0, row=0)

    scale = StringVar()
    scaleValue = ttk.Entry(t, textvariable=scale)
    scaleValue.grid(column=1, row=0)

    ttk.Button(t, text="Submit", command=scale_image_handler).grid(column=2, row=0)


def posterize_image_window():

    def posterizing_image_handler():
        levels_to_posterize = int(levelsValue.get())

        # if levels_to_posterize
        imageLogic.posterize(levels_to_posterize)

        t.destroy()

    t = Toplevel(root, pady=10, padx=10)
    t.title('Posterizing Options')

    ttk.Label(t, text="Choose Posterizing Levels (2 = B & W)").grid(column=0, row=0)

    levels = StringVar()
    levelsValue = ttk.Entry(t, textvariable=levels)
    levelsValue.grid(column=1, row=0)

    ttk.Button(t, text="Submit", command=posterizing_image_handler).grid(column=2, row=0)


ttk.Label(frm, text="Please select a function:").grid(column=0, row=0)

ttk.Button(frm, text="Select an Image", command=imageLogic.load_picture).grid(column=1, row=0)

ttk.Button(frm, text="Change Color", command=change_color_window).grid(column=2, row=0)

ttk.Button(frm, text="Rotation", command=rotate_image_window).grid(column=3, row=0)

ttk.Button(frm, text="Scaling", command=scale_image_window).grid(column=4, row=0)

ttk.Button(frm, text="Posterization", command=posterize_image_window).grid(column=5, row=0)

ttk.Button(frm, text="Save Image", command=imageLogic.save_picture).grid(column=6, row=0)

ttk.Button(frm, text="Reset Image", command=imageLogic.reset_image).grid(column=7, row=0)


root.mainloop()
