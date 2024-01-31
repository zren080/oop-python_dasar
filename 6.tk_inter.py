
import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window,text='label1')
label2 = tkinter.Label(main_window,text='label2')

tombol1 = tkinter.Button(main_window,text='tombol1')
tombol2 = tkinter.Button(main_window,text='tombol2')

# method positioning -> penentuan posisi
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method penampilan GUI
main_window.mainloop()



'''kalau huruf besar seperti -> "Tk,Label" itu adalah class
   kalau huruf kecil seperti -> "pack,mainloop" itu adalah method/fungsi'''