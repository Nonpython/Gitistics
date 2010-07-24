#!/usr/bin/env python
from   dulwich.repo  import Repo
from  PyQt4.QtCore   import *
from  PyQt4.QtGui    import *
from  sys            import argv
import numpy         as     np
import                      ConfigParser

class MainWindow(QDialog):
    def __init__(self, dir):
        self.repo = Repo(str(argv[0] or QFileDialog.getExistingDirectory(caption=QString('Select Git Repository'))))
        

app = QApplication(argv)
window = MainWindow()
window.show()
app._exec()