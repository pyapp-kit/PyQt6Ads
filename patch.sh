#!/bin/zsh

SO_FILE="/Users/talley/dev/self/PyQt6Ads/.venv/lib/python3.12/site-packages/PyQt6Ads.abi3.so"
QT_LIB_DIR="@loader_path/PyQt6/Qt6/lib"

install_name_tool -change @loader_path/../PyQt6/Qt6/lib/QtWidgets.framework/Versions/A/QtWidgets \
$QT_LIB_DIR/QtWidgets.framework/Versions/A/QtWidgets \
$SO_FILE

install_name_tool -change @loader_path/../PyQt6/Qt6/lib/QtGui.framework/Versions/A/QtGui \
$QT_LIB_DIR/QtGui.framework/Versions/A/QtGui \
$SO_FILE

install_name_tool -change @loader_path/../PyQt6/Qt6/lib/QtCore.framework/Versions/A/QtCore \
$QT_LIB_DIR/QtCore.framework/Versions/A/QtCore \
$SO_FILE
