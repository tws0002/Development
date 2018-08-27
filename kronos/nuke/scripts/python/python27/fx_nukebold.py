#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import nuke
import platform

def createBold():
    bold = nuke.nodePaste('W:/user/nuke/nodes/common/group/FX/bold.nk')
    usern = os.environ['USERNAME']
    filen = os.path.basename(nuke.root().name()).split(".")[0]
    nuke.knob('%s.username' % bold.name() , usern)
    nuke.knob('%s.filename' % bold.name() , filen)
    '''
    if 'Windows' == platform.system():
        nuke.knob('%s.font' % bold.name()).setValue('C:/WINDOWS/Fonts/cour.ttf')
    elif 'Linux' == platform.system():
        nuke.knob('%s.font' % bold.name()).setValue('/usr/share/fonts/truetype/Vera.ttf')
    '''
