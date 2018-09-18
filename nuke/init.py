import nuke
import pipelineSetup
import filenameFilters
import os 
'''
The template for the nuke setup
Make sure to configure this file so that you get the show specific things loaded in
'''
### CUSTOMIZE HERE
nuke.pluginAddPath(os.path.join(pipelineSetup.jobPath[0], pipelineSetup.job, pipelineSetup.jobPathNuke))
### END CUSTOMIZE

### Add general formats here
nuke.load('formats.py')