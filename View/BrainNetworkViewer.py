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
        tabs = wx.Notebook(self)
        panel = wx.Panel(tabs)
        tabs.AddPage(panel, "View")
        statusBar = self.CreateStatusBar(1, 0)
        statusBar.SetStatusWidths([-1])
        statusBar.SetStatusText('Brain Network Viewer. ')
        mainSizer = wx.GridBagSizer(6, 7)

        ### Set Status Section
        statusStaticBox = wx.StaticBox(panel, label='Status')
        mainSizer.Add(statusStaticBox, pos=(0, 4), span=(4, 3), flag=wx.TOP | wx.EXPAND | wx.RIGHT | wx.BOTTOM,
                      border=5)

        ###Set Template File Section
        templateBoxsizer = wx.StaticBoxSizer(wx.StaticBox(panel, -1, label='Template Files'), wx.VERTICAL)

        templateInternalBagSizer = wx.GridBagSizer(3, 6)
        templateBoxsizer.Add(templateInternalBagSizer, flag=wx.ALIGN_CENTER | wx.EXPAND)

        tlCheck = wx.CheckBox(panel, label="Left")
        templateInternalBagSizer.Add(tlCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                     pos=(0, 0), span=(1, 2), border=5)
        tlText = wx.TextCtrl(panel)
        templateInternalBagSizer.Add(tlText, pos=(0, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        tlButton = wx.Button(panel, label="Browse")
        templateInternalBagSizer.Add(tlButton, pos=(0, 5), flag=wx.TOP | wx.RIGHT, border=5)

        trCheck = wx.CheckBox(panel, label="Right")
        templateInternalBagSizer.Add(trCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                     pos=(1, 0), span=(1, 2), border=5)
        trText = wx.TextCtrl(panel)
        templateInternalBagSizer.Add(trText, pos=(1, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        trButton = wx.Button(panel, label="Browse")
        templateInternalBagSizer.Add(trButton, pos=(1, 5), flag=wx.TOP | wx.RIGHT, border=5)

        tfCheck = wx.CheckBox(panel, label="Full")
        templateInternalBagSizer.Add(tfCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                     pos=(2, 0), span=(1, 2), border=5)
        tfText = wx.TextCtrl(panel)
        templateInternalBagSizer.Add(tfText, pos=(2, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        tfButton = wx.Button(panel, label="Browse")
        templateInternalBagSizer.Add(tfButton, pos=(2, 5), flag=wx.TOP | wx.RIGHT, border=5)

        templateInternalBagSizer.AddGrowableCol(3)

        mainSizer.Add(templateBoxsizer, pos=(0, 0), span=(1, 4), flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        ##End Template Section

        ###Set Surface File Section
        surfaceBoxsizer = wx.StaticBoxSizer(wx.StaticBox(panel, -1, label='Surface Files'), wx.VERTICAL)

        surfaceInternalBagSizer = wx.GridBagSizer(3, 6)
        surfaceBoxsizer.Add(surfaceInternalBagSizer, flag=wx.ALIGN_CENTER | wx.EXPAND)

        slCheck = wx.CheckBox(panel, label="Left")
        surfaceInternalBagSizer.Add(slCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(0, 0), span=(1, 2), border=5)
        slText = wx.TextCtrl(panel)
        surfaceInternalBagSizer.Add(slText, pos=(0, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        slButton = wx.Button(panel, label="Browse")
        surfaceInternalBagSizer.Add(slButton, pos=(0, 5), flag=wx.TOP | wx.RIGHT, border=5)

        srCheck = wx.CheckBox(panel, label="Right")
        surfaceInternalBagSizer.Add(srCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(1, 0), span=(1, 2), border=5)
        srText = wx.TextCtrl(panel)
        surfaceInternalBagSizer.Add(srText, pos=(1, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        srButton = wx.Button(panel, label="Browse")
        surfaceInternalBagSizer.Add(srButton, pos=(1, 5), flag=wx.TOP | wx.RIGHT, border=5)

        sfCheck = wx.CheckBox(panel, label="Full")
        surfaceInternalBagSizer.Add(sfCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(2, 0), span=(1, 2), border=5)
        sfText = wx.TextCtrl(panel)
        surfaceInternalBagSizer.Add(sfText, pos=(2, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        sfButton = wx.Button(panel, label="Browse")
        surfaceInternalBagSizer.Add(sfButton, pos=(2, 5), flag=wx.TOP | wx.RIGHT, border=5)

        surfaceInternalBagSizer.AddGrowableCol(3)

        mainSizer.Add(surfaceBoxsizer, pos=(1, 0), span=(1, 4), flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        ##End Surface Section


        ###Set Network File Section
        networkBoxsizer = wx.StaticBoxSizer(wx.StaticBox(panel, -1, label='Network Files'), wx.VERTICAL)

        networkInternalBagSizer = wx.GridBagSizer(2, 6)
        networkBoxsizer.Add(networkInternalBagSizer, flag=wx.ALIGN_CENTER | wx.EXPAND)

        nodesCheck = wx.CheckBox(panel, label="Nodes")
        networkInternalBagSizer.Add(nodesCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(0, 0), span=(1, 2), border=5)
        nodesText = wx.TextCtrl(panel)
        networkInternalBagSizer.Add(nodesText, pos=(0, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        nodesButton = wx.Button(panel, label="Browse")
        networkInternalBagSizer.Add(nodesButton, pos=(0, 5), flag=wx.TOP | wx.RIGHT, border=5)

        edgesCheck = wx.CheckBox(panel, label="Edges")
        networkInternalBagSizer.Add(edgesCheck, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL,
                                    pos=(1, 0), span=(1, 2), border=5)
        edgesText = wx.TextCtrl(panel)
        networkInternalBagSizer.Add(edgesText, pos=(1, 2), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        edgesButton = wx.Button(panel, label="Browse")
        networkInternalBagSizer.Add(edgesButton, pos=(1, 5), flag=wx.TOP | wx.RIGHT, border=5)

        networkInternalBagSizer.AddGrowableCol(3)

        mainSizer.Add(networkBoxsizer, pos=(2, 0), span=(1, 4), flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        ##End Network Section

        ##Set Main Buttons
        verifyButton = wx.Button(panel, label='Verify')
        mainSizer.Add(verifyButton, pos=(4, 4), span=(1, 1), flag=wx.EXPAND, border=5)

        viewButton = wx.Button(panel, label='View')
        mainSizer.Add(viewButton, pos=(4, 5), span=(1, 1), flag=wx.EXPAND, border=5)

        quitButton = wx.Button(panel, label='Quit')
        mainSizer.Add(quitButton, pos=(4, 6), span=(1, 1), flag=wx.RIGHT | wx.EXPAND, border=5)

        ###### Initial Disabling Controls
        tlText.Enable(False)
        trText.Enable(False)
        tfText.Enable(False)
        slText.Enable(False)
        srText.Enable(False)
        sfText.Enable(False)
        nodesText.Enable(False)
        edgesText.Enable(False)

        tlButton.Enable(False)
        trButton.Enable(False)
        tfButton.Enable(False)
        slButton.Enable(False)
        srButton.Enable(False)
        sfButton.Enable(False)
        nodesButton.Enable(False)
        edgesButton.Enable(False)

        #####
        mainSizer.AddGrowableCol(1)
        mainSizer.AddGrowableCol(2)
        mainSizer.AddGrowableCol(3)
        mainSizer.AddGrowableCol(4)
        mainSizer.AddGrowableCol(5)
        mainSizer.AddGrowableCol(6)
        panel.SetSizer(mainSizer)

        ####Bindings
        self.Bind(wx.EVT_CLOSE, self.closeFrame)
        self.Bind(wx.EVT_BUTTON, self.closeButton, quitButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, tlText), tlButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, trText), trButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, tfText), tfButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, slText), slButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, srText), srButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, sfText), sfButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, nodesText), nodesButton)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onBrowse(event, edgesText), edgesButton)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, tlCheck, tlText, tlButton, disableCheckBoxList=[tfCheck],
                                                enableVerifyCheckBoxList=[trCheck]), tlCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, trCheck, trText, trButton, disableCheckBoxList=[tfCheck],
                                                enableVerifyCheckBoxList=[tlCheck]), trCheck)
        self.Bind(wx.EVT_CHECKBOX, lambda event: self.onCheckBox(event, tfCheck, tfText, tfButton,
                                                                 disableCheckBoxList=[tlCheck, trCheck],
                                                                 enableVerifyCheckBoxList=[tlCheck, trCheck]), tfCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, slCheck, slText, slButton, disableCheckBoxList=[sfCheck],
                                                enableVerifyCheckBoxList=[srCheck]), slCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, srCheck, srText, srButton, disableCheckBoxList=[sfCheck],
                                                enableVerifyCheckBoxList=[slCheck]), srCheck)
        self.Bind(wx.EVT_CHECKBOX, lambda event: self.onCheckBox(event, sfCheck, sfText, sfButton,
                                                                 disableCheckBoxList=[slCheck, srCheck],
                                                                 enableVerifyCheckBoxList=[slCheck, srCheck]), sfCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, nodesCheck, nodesText, nodesButton, disableCheckBoxList=[],
                                                enableVerifyCheckBoxList=[]), nodesCheck)
        self.Bind(wx.EVT_CHECKBOX,
                  lambda event: self.onCheckBox(event, edgesCheck, edgesText, edgesButton, disableCheckBoxList=[],
                                                enableVerifyCheckBoxList=[]), edgesCheck)

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