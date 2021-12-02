Every time a file is added/deleted/modified from assets folder, it is necessary to:
1) update the assets.qrc file
2) generate the assets.py file by calling the launching command from src/gui/assets folder:
pyrcc5 assets.qrc -o assets_rc.py