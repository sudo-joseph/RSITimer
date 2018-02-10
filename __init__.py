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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "RSI Timer" 
def description():
  return "Reminds uses to take a break at a user specified interval. "
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load RsiTimer class from file RsiTimer
  from RsiTimer import RsiTimer 
  return RsiTimer(iface)
