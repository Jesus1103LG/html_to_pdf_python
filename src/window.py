import wx
from html_to_pdf import generar_certificado

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw, size=(400,400))

        # create a panel in the frame
        pnl = wx.Panel(self)
        pnl.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        # Intput de texto

        # Input nombre
        st = wx.StaticText(pnl, label="Nombre:")
        font = st.GetFont()
        font.PointSize += 1
        font = font.Bold()
        st.SetFont(font)
        
        self.text_ctrl = wx.TextCtrl(pnl, style=wx.TE_PROCESS_ENTER)
        
        # Input Diplomado
        st2 = wx.StaticText(pnl, label="Diploma:")
        st2.SetFont(font)

        self.text_ctrl2 = wx.TextCtrl(pnl, style=wx.TE_PROCESS_ENTER)

        # Input Fecha
        st3 = wx.StaticText(pnl, label="Fecha:")
        st3.SetFont(font)

        self.text_ctrl3 = wx.TextCtrl(pnl, style=wx.TE_PROCESS_ENTER)

        # Input instituto
        st4 = wx.StaticText(pnl, label="Instituto:")
        st4.SetFont(font)

        self.text_ctrl4 = wx.TextCtrl(pnl, style=wx.TE_PROCESS_ENTER)

        # Boton paar mostrar el texto ingresado
        btn = wx.Button(pnl, label="Generar PDF")
        btn.Bind(wx.EVT_BUTTON, self.on_button_click)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, 0,  wx.LEFT | wx.TOP, 10)
        sizer.Add(self.text_ctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        sizer.Add(st2, 0,  wx.LEFT | wx.TOP, 10)
        sizer.Add(self.text_ctrl2, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(st3, 0,  wx.LEFT | wx.TOP, 10)
        sizer.Add(self.text_ctrl3, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(st4, 0,  wx.LEFT | wx.TOP, 10)
        sizer.Add(self.text_ctrl4, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(btn, 0, wx.ALL | wx.CENTER, 10)
        
        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def on_button_click(self, event):
        """Muestra el texto ingresado en la barra de estado"""
        nombre = self.text_ctrl.GetValue()
        diplomado = self.text_ctrl2.GetValue()
        fecha = self.text_ctrl3.GetValue()
        instituto = self.text_ctrl4.GetValue()
        data = {
            'nombre': nombre,
            'diplomado': diplomado,
            'fecha': fecha,
            'institucion': instituto
        }
        # self.SetStatusText(f"Texto ingresado: {texto_ingresado}")
        output_pdf = 'certificado.pdf'
        generar_certificado(data, output_pdf)
        self.SetStatusText(f"PDF generado correctamente: {output_pdf}")


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='HTML To PDF')
    frm.Show()
    app.MainLoop()