'''
Filename filters for Nuke
FX Pipe variables apply
'''
import nuke
import pipelineSetup

def pipelineSetupFileNameFilter(fileName):
    swapped = False
    if nuke.env['LINUX']:
        fileName, swapped = pathSwap(fileName, pipelineSetup.windowsPath, pipelineSetup.linuxPath)
        if swapped == False:
            fileName = pathSwap(fileName, pipelineSetup.macPath, pipelineSetup.linuxPath)
    if nuke.env['MACOS']:
        fileName, swapped = pathSwap(fileName, pipelineSetup.linuxPath, pipelineSetup.macPath)
        if swapped == False:
            fileName, swapped = pathSwap(fileName, pipelineSetup.windowsPath, pipelineSetup.macPath)        
    if nuke.env['WIN32']:
        fileName, swapped = pathSwap(fileName, pipelineSetup.linuxPath, pipelineSetup.windowsPath)
        if swapped == False:
            fileName, swapped = pathSwap(fileName, pipelineSetup.macPath, pipelineSetup.windowsPath)
    return fileName

def pathSwap(inFile, pathA, pathB):
    swapped = False
    for pathCount in range(min(len(pathA),len(pathB))):
        if swapped == False:
            fileName = inFile.replace(pathA[pathCount],pathB[pathCount])
            if fileName != inFile:
                swapped = True
                continue
    return fileName, swapped

nuke.addFilenameFilter(pipelineSetupFileNameFilter)
