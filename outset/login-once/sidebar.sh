#!/bin/bash
# Script uses mysides ( https://github.com/mosen/mysides ) to clear the sidebar and add our prefs.
# Our script is run by the local user in conjunction with other applescripts wrapped in an app
# before deployment to the end-user

# Get the Username of the currently logged user
loggedInUser=$(/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }')

# Removes all sides and adds /Applications, User Desktop, Documents, Downloads, Home Folder
if [ -e /usr/local/bin/mysides ]
MYSIDES="/usr/local/bin/mysides"
then
    $MYSIDES remove all
    $MYSIDES add Applications file:///Applications 
    $MYSIDES add Shares file:///home/$loggedInUser
	$MYSIDES add Desktop file:///Users/$loggedInUser/Desktop 
    $MYSIDES add Documents file:///Users/$loggedInUser/Documents
	$MYSIDES add Downloads file:///Users/$loggedInUser/Downloads 
    touch /Users/$loggedInUser/.sidebarshortcuts
fi

# Hides Tags
defaults write /Users/$loggedInUser/Library/Preferences/com.apple.finder ShowRecentTags -bool FALSE     
# Hides External Drives on Desktop      
defaults write /Users/$loggedInUser/Library/Preferences/com.apple.finder ShowExternalHardDrivesOnDesktop -bool FALSE
# Hides Server on Desktop
defaults write /Users/$loggedInUser/Library/Preferences/com.apple.finder ShowMountedServersOnDesktop -bool FALSE
# Hides Shared section on SideBar
defaults write /Users/$loggedInUser/Library/Preferences/com.apple.finder SidebarSharedSectionDisclosedState -int 0
# Sets Default Finder window to open at Computer showing root HD, connected external drives, and connected servers instead of Recents
defaults write /Users/$loggedInUser/Library/Preferences/com.apple.finder NewWindowTarget PfCm
defaults write /Users/$loggedInUser/Library/Preferences/com.apple.finder NewWindowTargetPath PfCm

killall Finder