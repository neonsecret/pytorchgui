# Qt
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
import pytorchgui as rc
from nodes import export_nodes

# torch
import torch

if __name__ == "__main__":
    # first, we create the Qt application and a window
    app = QApplication()
    mw = QMainWindow()

    # now we initialize a new pytorchgui session
    session = rc.Session()
    session.design.set_flow_theme(name='Blender')  # setting the design theme

    # and register our nodes and create a script
    # device = torch.device(0) if torch.cuda.is_available() else torch.device("cpu")
    device = torch.device("cpu")
    session.register_nodes(export_nodes, device=device)

    # to get a flow where we can place nodes, we need to crate a new script
    script = session.create_script('default',
                                   flow_view_size=[1000, 1000])

    # getting the flow widget of the newly created script
    flow_view = session.flow_views[script]
    mw.setCentralWidget(flow_view)  # and show it in the main window

    # finally, show the window and run the application
    mw.show()
    # session.serialize()
    sys.exit(app.exec_())
