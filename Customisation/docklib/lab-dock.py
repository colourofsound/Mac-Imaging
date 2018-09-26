import os
from docklib import Dock
tech_dock = [
    '/Applications/Launchpad.app',
    '',
    '/Applications/Safari.app',
    '/Applications/Firefox.app',
    '/Applications/Google Chrome.app',
    '/Applications/Brave.app',
    '',
    '/Applications/Axure RP 8.app',
    '/Applications/Android Studio.app',
    '/Applications/IntelliJ IDEA.app',
    '/Applications/LEGO MINDSTORMS EV3 Home Edition.app',
    '/Applications/Sketch.app',
    '/Applications/Atom.app',
    '/Applications/Cocoapods.app',
    '/Applications/Textmate.app',
    '',
    '/Applications/Pages.app',
    '/Applications/Numbers.app',
    '/Applications/Keynote.app',
    '/Applications/Microsoft Word.app',
    '/Applications/Microsoft Excel.app',
    '/Applications/Microsoft PowerPoint.app',
    '',
    '/Applications/Adobe After Effects CC 2018/Adobe After Effects CC 2018.app',
    '/Applications/Adobe Audition CC 2018/Adobe Audition CC 2018.app',
    '/Applications/Adobe Illustrator CC 2018/Adobe Illustrator CC 2018.app',
    '/Applications/Adobe InDesign CC 2018/Adobe InDesign CC 2018.app',
    '/Applications/Adobe Photoshop CC 2018/Adobe Photoshop CC 2018.app',
    '/Applications/Adobe Premiere Pro CC 2018/Adobe Premiere Pro CC 2018.app',
    '',
    '/Applications/Audacity.app',
    '/Applications/VLC.app',
    '/Applications/VirtualBox.app',
    '/Applications/Microsoft Remote Desktop.app',
    '/Applications/Filezilla.app',
    '/Applications/Amphetamine.app',
    '/Applications/Xcode.app',
    '/Applications/Utilities/Terminal.app',
    '/Applications/System Preferences.app',
]
dock = Dock()
dock.items['persistent-apps'] = []
for item in tech_dock:
    if os.path.exists(item):
        item = dock.makeDockAppEntry(item)
        dock.items['persistent-apps'].append(item)
    elif item == '':
            item = dock.makeDockAppSpacer()
            dock.items['persistent-apps'].append(item)
    if dock.findExistingLabel('Python 3.7', section='persistent-others') == -1:
        item = dock.makeDockOtherEntry(os.path.expanduser('/Applications/Python 3.7'),
                                       arrangement=3,
                                       displayas=1,
                                       showas=1)
        dock.items['persistent-others'] = [item] + dock.items['persistent-others']
    if dock.findExistingLabel('Xcode Additional Tools', section='persistent-others') == -1:
        item = dock.makeDockOtherEntry(os.path.expanduser('/Applications/Xcode Additional Tools'),
                                       arrangement=3,
                                       displayas=1,
                                       showas=1)
        dock.items['persistent-others'] = [item] + dock.items['persistent-others']
dock.save()