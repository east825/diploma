import os
import json
from PyQt4.QtCore import QSettings

if __name__ == '__main__':
    s = QSettings()
    #path = s.value('ConfigPath', '~/.settings')
    #path = s.value('ConfigPath', '~/.settings').toString()
    path = unicode(s.value('ConfigPath', '~/.settings').toString())
    path = os.path.expanduser(path)
    with open(path, 'r') as f:
        config = json.load(f)
