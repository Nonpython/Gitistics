#!/usr/bin/env python
from   dulwich.repo   import Repo
from   PyQt4.Qt       import *
from   sys            import argv
import numpy          as     np
import                       re

class Day(object):
    def __init__(self, date):
        "One day of commits"
        self.names = []
        self.items_by_name = {}
        self.date = date
    
    def add_name(self, name):
        self.names.append(name)
        self.items_by_name[name] = []
    
    def add_item(self, name, time):
        self.items_by_name[name].append([name, time])

class RepoStatistics(object):
      def GetCommiter(self, sha):
          "Gets the real name of the committer of the specified commit"
          return self.NameFromCommit.match(self.repo.get_object(sha).author
                                          ).group(1)
      
      def get():
class MainWindow(QMainWindow):
    def __init__(self):
        "The main window of Gitistics"
        self.repo           = Repo(str(
                                       QFileDialog.getExistingDirectory(
                                                     caption=QString(
                                                    'Select Git Repository'))))
        self.NameFromCommit = re.compile(r'(.+)\s<.+>')
        TabWidget = QTabWidget()
        byDateWidget = QWidget()
        byDateLayout = QGridLayout()

App = QApplication(argv)
Window = MainWindow()
Window.show()
App._exec()