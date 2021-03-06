# -*- coding: utf-8 -*-

"""
/***************************************************************************
 OPTIMAL-IPB
                                 A QGIS plugin
 This plugin adds an algorithm to calculate palm tree on high resolution imagery based on machine learning
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-09-22
        copyright            : (C) 2020 by Muhammad Nurdin
        email                : muhanur@apps.ipb.ac.id
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

__author__ = 'Muhammad Nurdin'
__date__ = '2020-09-22'
__copyright__ = '(C) 2020 by Muhammad Nurdin'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon

from qgis.core import QgsProcessingAlgorithm, QgsApplication
import processing
from .optimal_ipb_provider import OptimalIpbProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class OptimalIpbPlugin(object):

    def __init__(self, iface):
        self.provider = None
        self.iface = iface

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = OptimalIpbProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()
        
        icon = os.path.join(os.path.join(cmd_folder, 'logo.png'))
        self.action = QAction(
            QIcon(icon),
            u"OPTIMAL-IPB", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu(u"&Calculate", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
        self.iface.removePluginMenu(u"&Calculate", self.action)
        self.iface.removeToolBarIcon(self.action)
    
    def run(self):
        processing.execAlgorithmDialog("Calculate:OPTIMAL-IPB")
