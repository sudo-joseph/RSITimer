"""
/***************************************************************************
Name			 	 : RSI Timer
Description          : Reminds uses to take a break at a user specified interval. 
Date                 : 11/Nov/17 
copyright            : (C) 2017 by Joseph Reid
email                : joseph.james.reid@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_RsiTimer import Ui_RsiTimer
# create the dialog for RsiTimer
class RsiTimerDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_RsiTimer ()
    self.ui.setupUi(self)