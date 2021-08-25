import tkinter

def FNC_Cacher ( ) :
    TKI_Test.withdraw ( )

def FNC_Monter ( ) :
    TKI_Test.deiconify ( )

TKI_Principal = tkinter.Tk ( )
TKI_Test = tkinter.Toplevel ( )
TKI_Test.geometry (  "240x180+300+100" )
BUT_Quitter = tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy )
BUT_Cacher = tkinter.Button ( TKI_Principal , text = "Cacher" , command = FNC_Cacher )
BUT_Monter = tkinter.Button ( TKI_Principal , text = "Monter" , command = FNC_Monter )

BUT_Cacher.pack ( )
BUT_Monter.pack ( )
BUT_Quitter.pack ( )

TKI_Principal.mainloop ( )
