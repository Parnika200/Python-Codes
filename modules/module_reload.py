"""
if u import a module and make changes afterwards python wont re-execute it.
to update the changes use reload()
"""

import student
import importlib
student.display("anna",1)
importlib.reload(student)