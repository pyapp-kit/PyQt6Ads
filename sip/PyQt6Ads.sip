%Module(name=PyQt6Ads, call_super_init=True, keyword_arguments="Optional", use_limited_api=True)
%HideNamespace(name=ads)

%If defined(_WIN32)
%ModuleCode
    PyObject* pyqt6_module = PyImport_ImportModule("PyQt6");
    if (pyqt6_module == NULL) {
        PyErr_SetString(PyExc_ImportError, "Failed to import PyQt6");
        return;
    }
    Py_DECREF(pyqt6_module);
%End


%Import QtCore/QtCoremod.sip
%DefaultSupertype PyQt6.sip.simplewrapper

%Include ads_globals.sip
%Include AutoHideDockContainer.sip
%Include AutoHideSideBar.sip
%Include AutoHideTab.sip
%Include DockWidget.sip
%Include DockAreaTabBar.sip
%Include DockAreaTitleBar_p.sip
%Include DockAreaTitleBar.sip
%Include DockAreaWidget.sip
%Include DockComponentsFactory.sip
%Include DockContainerWidget.sip
%Include DockingStateReader.sip
%Include DockFocusController.sip
%Include DockManager.sip
%Include DockOverlay.sip
%Include DockSplitter.sip
%Include DockWidgetTab.sip
%Include ElidingLabel.sip
%Include FloatingDockContainer.sip
%Include FloatingDragPreview.sip
%Include IconProvider.sip
%Include PushButton.sip
%Include ResizeHandle.sip
%If (Linux)
    %Include linux/FloatingWidgetTitleBar.sip
%End
