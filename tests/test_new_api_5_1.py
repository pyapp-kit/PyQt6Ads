"""Tests for APIs added in Qt-Advanced-Docking-System 5.1."""

from __future__ import annotations

import PyQt6Ads as ads
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication.instance() or QApplication([])


def test_auto_hide_side_bar_wheel_event() -> None:
    flag = ads.CDockManager.eAutoHideFlag.AutoHideFeatureEnabled
    ads.CDockManager.setAutoHideConfigFlag(flag, True)
    try:
        window = QMainWindow()
        mgr = ads.CDockManager(window)
        dock = ads.CDockWidget(mgr, "dock")
        loc = ads.SideBarLocation.SideBarLeft
        container = mgr.addAutoHideDockWidget(loc, dock)
        side_bar = container.autoHideSideBar()
        assert "wheelEvent" in type(side_bar).__dict__
    finally:
        ads.CDockManager.setAutoHideConfigFlag(flag, False)
