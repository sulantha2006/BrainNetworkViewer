__author__ = 'sulantha'
import wx
import os


class BrainNetworkViewer(wx.Frame):
    def __init__(self, parent, title):
        super(BrainNetworkViewer, self).__init__(parent, style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,
                                             title=title, size=(800, 500))
        self.LayoutUI()
        self.Centre()
        self.Show()


    def LayoutUI(self):
        self.tabs = wx.Notebook(self)
        self.panel = wx.Panel(self.tabs)
        self.tabs.AddPage(self.panel, "View")
        self.statusBar = self.CreateStatusBar(1, 0)
        self.statusBar.SetStatusWidths([-1])
        self.statusBar.SetStatusText('Brain Network Viewer. ')
        mainSizer = wx.GridBagSizer(6, 7)

        ### Set Status Section
        statusStaticBox = wx.StaticBox(self.panel, label='Status')
        mainSizer.Add(statusStaticBox, pos=(0, 4), span=(4, 3), flag=wx.TOP | wx.EXPAND | wx.RIGHT | wx.BOTTOM,
                      border=5)

        ###Set Template File Section
        templateBoxsizer = wx.StaticBoxSizer(wx.StaticBox(self.panel, -1, label='Template Files'), wx.VERTICAL)

        templateInternalBagSizer = wx.GridBagSizer(3, 6)
        templateBoxsizer.Add(templateInternalBagSizer, flag=wx.ALIGN_CENTER | wx.EXPAND)

        self.tlCheck = wx.CheckBox(self.panel, label="Left")
        templateInternalBagSizer.Add(self.tlCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                     pos=(0, 0), span=(1, 2), border=5)
        self.tlText = wx.TextCtrl(self.panel)
        templateInternalBagSizer.Add(self.tlText, pos=(0, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.tlButton = wx.Button(self.panel, label="Browse")
        templateInternalBagSizer.Add(self.tlButton, pos=(0, 5), flag=wx.TOP | wx.RIGHT, border=5)

        self.trCheck = wx.CheckBox(self.panel, label="Right")
        templateInternalBagSizer.Add(self.trCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                     pos=(1, 0), span=(1, 2), border=5)
        self.trText = wx.TextCtrl(self.panel)
        templateInternalBagSizer.Add(self.trText, pos=(1, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.trButton = wx.Button(self.panel, label="Browse")
        templateInternalBagSizer.Add(self.trButton, pos=(1, 5), flag=wx.TOP | wx.RIGHT, border=5)

        self.tfCheck = wx.CheckBox(self.panel, label="Full")
        templateInternalBagSizer.Add(self.tfCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                     pos=(2, 0), span=(1, 2), border=5)
        self.tfText = wx.TextCtrl(self.panel)
        templateInternalBagSizer.Add(self.tfText, pos=(2, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.tfButton = wx.Button(self.panel, label="Browse")
        templateInternalBagSizer.Add(self.tfButton, pos=(2, 5), flag=wx.TOP | wx.RIGHT, border=5)

        templateInternalBagSizer.AddGrowableCol(3)

        mainSizer.Add(templateBoxsizer, pos=(0, 0), span=(1, 4), flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        ##End Template Section

        ###Set Surface File Section
        surfaceBoxsizer = wx.StaticBoxSizer(wx.StaticBox(self.panel, -1, label='Surface Files'), wx.VERTICAL)

        surfaceInternalBagSizer = wx.GridBagSizer(3, 6)
        surfaceBoxsizer.Add(surfaceInternalBagSizer, flag=wx.ALIGN_CENTER | wx.EXPAND)

        self.slCheck = wx.CheckBox(self.panel, label="Left")
        surfaceInternalBagSizer.Add(self.slCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(0, 0), span=(1, 2), border=5)
        self.slText = wx.TextCtrl(self.panel)
        surfaceInternalBagSizer.Add(self.slText, pos=(0, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.slButton = wx.Button(self.panel, label="Browse")
        surfaceInternalBagSizer.Add(self.slButton, pos=(0, 5), flag=wx.TOP | wx.RIGHT, border=5)

        self.srCheck = wx.CheckBox(self.panel, label="Right")
        surfaceInternalBagSizer.Add(self.srCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(1, 0), span=(1, 2), border=5)
        self.srText = wx.TextCtrl(self.panel)
        surfaceInternalBagSizer.Add(self.srText, pos=(1, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.srButton = wx.Button(self.panel, label="Browse")
        surfaceInternalBagSizer.Add(self.srButton, pos=(1, 5), flag=wx.TOP | wx.RIGHT, border=5)

        self.sfCheck = wx.CheckBox(self.panel, label="Full")
        surfaceInternalBagSizer.Add(self.sfCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(2, 0), span=(1, 2), border=5)
        self.sfText = wx.TextCtrl(self.panel)
        surfaceInternalBagSizer.Add(self.sfText, pos=(2, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.sfButton = wx.Button(self.panel, label="Browse")
        surfaceInternalBagSizer.Add(self.sfButton, pos=(2, 5), flag=wx.TOP | wx.RIGHT, border=5)

        surfaceInternalBagSizer.AddGrowableCol(3)

        mainSizer.Add(surfaceBoxsizer, pos=(1, 0), span=(1, 4), flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        ##End Surface Section


        ###Set Network File Section
        networkBoxsizer = wx.StaticBoxSizer(wx.StaticBox(self.panel, -1, label='Network Files'), wx.VERTICAL)

        networkInternalBagSizer = wx.GridBagSizer(2, 6)
        networkBoxsizer.Add(networkInternalBagSizer, flag=wx.ALIGN_CENTER | wx.EXPAND)

        self.nodesCheck = wx.CheckBox(self.panel, label="Nodes")
        networkInternalBagSizer.Add(self.nodesCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(0, 0), span=(1, 2), border=5)
        self.nodesText = wx.TextCtrl(self.panel)
        networkInternalBagSizer.Add(self.nodesText, pos=(0, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.nodesButton = wx.Button(self.panel, label="Browse")
        networkInternalBagSizer.Add(self.nodesButton, pos=(0, 5), flag=wx.TOP | wx.RIGHT, border=5)

        self.edgesCheck = wx.CheckBox(self.panel, label="Edges")
        networkInternalBagSizer.Add(self.edgesCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(1, 0), span=(1, 2), border=5)
        self.edgesText = wx.TextCtrl(self.panel)
        networkInternalBagSizer.Add(self.edgesText, pos=(1, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.edgesButton = wx.Button(self.panel, label="Browse")
        networkInternalBagSizer.Add(self.edgesButton, pos=(1, 5), flag=wx.TOP | wx.RIGHT, border=5)

        networkInternalBagSizer.AddGrowableCol(3)

        mainSizer.Add(networkBoxsizer, pos=(2, 0), span=(1, 4), flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        ##End Network Section

        ##Set Main Buttons
        self.verifyButton = wx.Button(self.panel, label='Verify')
        mainSizer.Add(self.verifyButton, pos=(4, 4), span=(1, 1), flag=wx.EXPAND, border=5)

        self.viewButton = wx.Button(self.panel, label='View')
        mainSizer.Add(self.viewButton, pos=(4, 5), span=(1, 1), flag=wx.EXPAND, border=5)

        self.quitButton = wx.Button(self.panel, label='Quit')
        mainSizer.Add(self.quitButton, pos=(4, 6), span=(1, 1), flag=wx.RIGHT | wx.EXPAND, border=5)

        ###### Initial Disabling Controls
        self.tlText.Enable(False)
        self.trText.Enable(False)
        self.tfText.Enable(False)
        self.slText.Enable(False)
        self.srText.Enable(False)
        self.sfText.Enable(False)
        self.nodesText.Enable(False)
        self.edgesText.Enable(False)

        self.tlButton.Enable(False)
        self.trButton.Enable(False)
        self.tfButton.Enable(False)
        self.slButton.Enable(False)
        self.srButton.Enable(False)
        self.sfButton.Enable(False)
        self.nodesButton.Enable(False)
        self.edgesButton.Enable(False)

        #####
        mainSizer.AddGrowableCol(1)
        mainSizer.AddGrowableCol(2)
        mainSizer.AddGrowableCol(3)
        mainSizer.AddGrowableCol(4)
        mainSizer.AddGrowableCol(5)
        mainSizer.AddGrowableCol(6)
        self.panel.SetSizer(mainSizer)

        ####Bindings
        self.Bind(wx.EVT_CLOSE, self.closeFrame)
        self.Bind(wx.EVT_BUTTON, self.closeButton, self.quitButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.tlText), self.tlButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.trText), self.trButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.tfText), self.tfButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.slText), self.slButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.srText), self.srButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.sfText), self.sfButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.nodesText), self.nodesButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, self.edgesText), self.edgesButton)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, self.tlCheck, self.tlText, self.tlButton, disableCheckBoxList=[self.tfCheck],
                                                enableVerifyCheckBoxList=[self.trCheck]), self.tlCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, self.trCheck, self.trText, self.trButton, disableCheckBoxList=[self.tfCheck],
                                                enableVerifyCheckBoxList=[self.tlCheck]), self.trCheck)
        self.Bind(wx.EVT_CHECKBOX, lambda event: self.onCheckBox(event, self.tfCheck, self.tfText, self.tfButton,
                                                                 disableCheckBoxList=[self.tlCheck, self.trCheck],
                                                                 enableVerifyCheckBoxList=[self.tlCheck, self.trCheck]), self.tfCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, self.slCheck, self.slText, self.slButton, disableCheckBoxList=[self.sfCheck],
                                                enableVerifyCheckBoxList=[self.srCheck]), self.slCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, self.srCheck, self.srText, self.srButton, disableCheckBoxList=[self.sfCheck],
                                                enableVerifyCheckBoxList=[self.slCheck]), self.srCheck)
        self.Bind(wx.EVT_CHECKBOX, lambda event: self.onCheckBox(event, self.sfCheck, self.sfText, self.sfButton,
                                                                 disableCheckBoxList=[self.slCheck, self.srCheck],
                                                                 enableVerifyCheckBoxList=[self.slCheck, self.srCheck]), self.sfCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, self.nodesCheck, self.nodesText, self.nodesButton, disableCheckBoxList=[],
                                                enableVerifyCheckBoxList=[]), self.nodesCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, self.edgesCheck, self.edgesText, self.edgesButton, disableCheckBoxList=[],
                                                enableVerifyCheckBoxList=[]), self.edgesCheck)

        ####End Bindings


    def closeButton(self, event):
        self.Close(True)

    def closeFrame(self, event):
        self.Destroy()

    def onBrowse(self, event, textField):
        openFileDialog = wx.FileDialog(self, "Open", "", "", "Any (*.nv)|*.nv", wx.FD_OPEN)
        openFileDialog.ShowModal()
        filePath = openFileDialog.GetPath()
        openFileDialog.Destroy()
        textField.SetValue(filePath)

    def onCheckBox(self, event, checkBox, textField, browseButton, **kwargs):
        if checkBox.GetValue():
            textField.Enable(True)
            browseButton.Enable(True)
            for checkBox in kwargs.get('disableCheckBoxList'):
                checkBox.Enable(False)
        else:
            textField.Enable(False)
            browseButton.Enable(False)
            if not all([x.GetValue() for x in kwargs.get('enableVerifyCheckBoxList')]):
                for checkBox in kwargs.get('disableCheckBoxList'):
                    checkBox.Enable(True)


if __name__ == '__main__':
    app = wx.App()
    BrainNetworkViewer(None, title='NeuroConnector: Brain Connectome Viewer')
    app.MainLoop()