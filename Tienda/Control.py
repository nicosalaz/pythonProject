from Tienda.Inventario import Inventario
import tkinter as tk
from tkinter import ttk
from tkinter import *
class Control:
    def __init__(self,window):
        self.win = window#declaracion de la ventana
        self.win.title('Administracion')#titulo de la ventana
        self.invent = Inventario()

        frame = LabelFrame(self.win, text='Register new Product')#es donde se colocan los widgets
        frame.grid(row=0, column=0, columnspan=4, padx=20, pady=20)#ubicacion del frame

        # Name Input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name = Entry(frame)#input del nombre
        self.name.focus()#para que el puntero empiece alli
        self.name.grid(row=1, column=1)#ubicacion en la pantalla

        # Price Input
        Label(frame, text='Price: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Amount Input
        Label(frame, text='Amount: ').grid(row=3, column=0)
        self.amount = Entry(frame)
        self.amount.grid(row=3, column=1)

        treeFrame = LabelFrame(self.win)
        treeFrame.grid(row=5, column=0)

        # ceate table
        self.tree = ttk.Treeview(treeFrame, columns=("Price", "Amount"))#creo la tabla(lugar,cantidad de columnas)
        self.tree.grid(row=5, column=0)#ubicacion
        self.tree.heading("#0", text="Name", anchor=CENTER)#encabezado(numero de column, nombre, ubicacion)
        self.tree.heading("#1", text="Price", anchor=CENTER)
        self.tree.heading("#2", text="Amount", anchor=CENTER)
        self.invent.getProducts(self.tree)

        #Buttons
        Button(frame, text="Add Product", bg='green',command= lambda:self.invent.addProduct(self.name.get()
                                                                                           ,self.price.get()
                                                                                           ,self.amount.get()
                                                                                           ,self.tree))\
                .grid(row=4, columnspan=2, sticky=W + E)
        Button(treeFrame,text='DELETE',bg='red',command=lambda:self.invent.deleteProduct(self.tree))\
            .grid(row=6,column=0,sticky=W+E)
        Button(treeFrame,text='UPDATE',bg='orange',command=lambda:self.invent.getInfo(self.tree,self.idit_interface))\
            .grid(row=7,column=0,sticky=W+E)
    def idit_interface(self,name,price,amount):
        edit_view = Toplevel()
        edit_view.title('Edit Product')
        edit_view.geometry('250x180')
        edit = LabelFrame(edit_view)
        edit.pack()
        #oldname
        Label(edit, text='old Name: ').grid(row=1, column=0)
        Entry(edit, textvariable = StringVar(edit, value = name), state = 'readonly').grid(row = 1, column = 1)
        #newName
        Label(edit, text='new Name: ').grid(row=2, column=0)
        newName = Entry(edit)
        newName.focus()
        newName.grid(row=2, column=1)
        # oldPrice
        Label(edit, text='old Price: ').grid(row=3, column=0)
        Entry(edit, textvariable=StringVar(edit, value=price), state='readonly').grid(row=3, column=1)
        # newPrice
        Label(edit, text='new Price: ').grid(row=4, column=0)
        newPrice = Entry(edit)
        newPrice.grid(row=4, column=1)
        # oldname
        Label(edit, text='old Amount: ').grid(row=5, column=0)
        Entry(edit, textvariable=StringVar(edit, value=amount), state='readonly').grid(row=5, column=1)
        # newName
        Label(edit, text='new Amount: ').grid(row=6, column=0)
        newAmount = Entry(edit)
        newAmount.grid(row=6, column=1)

        Button(edit,text='EDIT',bg='green',command=lambda:self.invent.updateProduct(self.tree,
                                                                                    newName.get(),
                                                                                    newPrice.get(),
                                                                                    newAmount.get(),
                                                                                    edit_view))\
            .grid(row=7,column=0,sticky=W+E)





if __name__  == '__main__':
    window = Tk()
    aplicacion = Control(window)
    window.mainloop()