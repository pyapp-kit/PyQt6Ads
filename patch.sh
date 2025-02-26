#!/bin/zsh

SO_FILE=".venv/lib/python3.12/site-packages/PyQt6Ads.abi3.so"
QT_LIB_DIR="@loader_path/PyQt6/Qt6/lib"

install_name_tool -change /opt/homebrew/opt/qt/lib/QtWidgets.framework/Versions/A/QtWidgets \
$QT_LIB_DIR/QtWidgets.framework/Versions/A/QtWidgets \
$SO_FILE

install_name_tool -change /opt/homebrew/opt/qt/lib/QtGui.framework/Versions/A/QtGui \
$QT_LIB_DIR/QtGui.framework/Versions/A/QtGui \
$SO_FILE

install_name_tool -change /opt/homebrew/opt/qt/lib/QtCore.framework/Versions/A/QtCore \
$QT_LIB_DIR/QtCore.framework/Versions/A/QtCore \
$SO_FILE
