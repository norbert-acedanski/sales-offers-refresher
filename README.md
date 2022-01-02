# sale-offers-refresher

# About The Project
Script refreshes all espired offers from **gumtree.pl** with _pyautogui_ package in Chrome. It requires preparations listed in Working with...

# Built With
Python 3.8.0

# Getting started
### Requirements

All required packages in requirements.txt file.

To install all required packages, type _pip install -r requirements.txt_ int the terminal.

### Working with sale-offers-refresher:
1. Open gumtree tab in a new window.
2. Go to your gumtree account and choose _Expired_.
3. Use "ctrl", "shift", "j" hotkey to start DevTools.
4. Go to settings by using "F1" key.
5. Scroll down and hit "Restore defaults and reload" button.
6. Previous step will change the appearance of the DevTools. Change horizontal size of the DevTools, so that only the "Console" tab is visible:

<p align="center">
  <img src="/DevToolsLook.png" />
</p>

7. Close the DevTools with "ctrl", "shift", "j" hotkey.
8. Make sure to left-click to the right of the gumtree logo on top of the page:

<p align="center">
  <img src="/GumtreeClickPlace.png" />
</p>

9. Go to Python script.
10. Set _numberOfOffersToRefresh_ and _switchToGumTreeTab_ variables accordingly.
11. If second variable is set to True, no additional intervention is required. If to False, just after the script starts, switch to gumtree tab within 3.5 seconds.
12. Run the script.
13. During script execution **do not click any keyboard key or any mouse button**.
14. Successful execution should refresh all expired offers, close all tabs except the main gumtree page, and refresh it.

# Usage
Allows you to almost automatically refresh gumtree offers (if you have dozens of expired offers it comes in handy).

# Licence
Distributed under the MIT License. See LICENSE file for more information.
