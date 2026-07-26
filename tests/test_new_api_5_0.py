"""Tests for APIs added in Qt-Advanced-Docking-System 5.0.0."""

from __future__ import annotations

import PyQt6Ads as ads
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication.instance() or QApplication([])


def test_color_scheme_mode() -> None:
    assert ads.CDockManager.ColorSchemeMode.Light is not None
    assert ads.CDockManager.ColorSchemeMode.Dark is not None
    assert ads.CDockManager.ColorSchemeMode.FollowPalette is not None

    window = QMainWindow()
    mgr = ads.CDockManager(window)
    mgr.setColorSchemeMode(ads.CDockManager.ColorSchemeMode.FollowPalette)
    assert isinstance(mgr.isDesiredStylesheetDark(), bool)
    assert isinstance(ads.CDockManager.isApplicationPaletteDark(), bool)


def test_new_config_flags() -> None:
    assert ads.CDockManager.eConfigFlag.UseNativeWindows.value == 0x40000000
    # 0x80000000 overflows a signed 32-bit int in the C++ enum
    assert (
        ads.CDockManager.eConfigFlag.DisableStylesheet.value & 0xFFFFFFFF == 0x80000000
    )


def test_preferred_auto_hide_side_bar_location() -> None:
    dw = ads.CDockWidget("test")
    assert dw.preferredAutoHideSideBarLocation() == ads.SideBarLocation.SideBarNone
    dw.setPreferredAutoHideSideBarLocation(ads.SideBarLocation.SideBarLeft)
    assert dw.preferredAutoHideSideBarLocation() == ads.SideBarLocation.SideBarLeft


def test_floating_dock_container_new_methods() -> None:
    window = QMainWindow()
    mgr = ads.CDockManager(window)
    dw = ads.CDockWidget("test")
    mgr.addDockWidget(ads.DockWidgetArea.TopDockWidgetArea, dw)
    floating = mgr.addDockWidgetFloating(ads.CDockWidget("floating"))
    assert floating.isDraggingActive() is False


def test_dock_overlay_global_pos_overloads() -> None:
    from PyQt6.QtCore import QPoint

    window = QMainWindow()
    overlay = ads.CDockOverlay(window)
    pos = QPoint(0, 0)
    assert isinstance(overlay.dropAreaUnderCursor(pos), ads.DockWidgetArea)
    assert isinstance(overlay.visibleDropAreaUnderCursor(pos), ads.DockWidgetArea)


def test_is_wayland() -> None:
    assert isinstance(ads.internal.isWayland(), bool)
