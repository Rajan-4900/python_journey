# CRD file --> Copy File, Rename File, Delete Files

# using python module :
# think of a module as a toolBox
# each module gives you tools (function) that you don't have to write again.

# Copy file mwthod
import shutil
shutil.copy("witefile.txt", "copyfile.txt")    # it will create copy of the witefile.txt to copyfile.txt

# Rename File Method
import os
os.rename("copyfile.txt", "renamedFile.txt")    # this will rename the exisiting file to new name 

# delete File method
os.remove("renamedFile.txt")