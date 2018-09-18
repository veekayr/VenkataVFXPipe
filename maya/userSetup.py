import maya.cmds as cmds
import maya.utils as utils
import maya.mel as mel
import os, sys

def setupMayaPipe():

    import pipelineSetup 
    import mayaUtils

    # let's create the menus
    if cmds.menu('pipelineSetupMenu', exists=1):
        cmds.deleteUI('pipelineSetupMenu')

    pipelineSetupMenu = cmds.menu('pipelineSetupMenu', p='MayaWindow', to=1, aob=1, l='Pipeline Tools')
    cmds.menuItem(p=pipelineSetupMenu, d=1)
    toolsMenu = cmds.menuItem(p=pipelineSetupMenu, subMenu = 1, l="Tools")
    mayaMenu = cmds.menuItem(p=toolsMenu, subMenu = 1, to = 1, l='Maya')
    
    # Tools Menu
    cmds.menuItem(p=mayaMenu, l='Create Divider', c='from createDividerGroup import createDividerGroup;createDividerGroup()')
    cmds.menuItem(p=mayaMenu, l='Create BBox from Selected', c='import mayaUtils;mayaUtils.createBoudingBox()')
        
    if pipelineSetup.job != '':
        mayaJobPath = (os.path.join(pipelineSetup.jobPath, pipelineSetup.job, pipelineSetup.jobPathMaya))
        print mayaJobPath
        sys.path.append(mayaJobPath)

utils.executeDeferred('setupMayaPipe()') # wait until maya is ready to do the real work here...
