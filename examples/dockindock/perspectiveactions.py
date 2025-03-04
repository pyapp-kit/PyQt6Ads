from typing import TYPE_CHECKING

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu

if TYPE_CHECKING:
    from dockindock import DockInDockWidget


class LoadPerspectiveAction(QAction):
    def __init__(self, parent: QMenu, name: str, dock_manager: "DockInDockWidget"):
        super().__init__(name, parent)
        self.name = name
        self.dock_manager = dock_manager

        self.triggered.connect(self.load)

    def load(self):
        self.dock_manager.getPerspectivesManager().openPerspective(
            self.name, self.dock_manager
        )


class RemovePerspectiveAction(QAction):
    def __init__(self, parent: QMenu, name: str, dock_manager: "DockInDockWidget"):
        super().__init__(name, parent)
        self.name = name
        self.dock_manager = dock_manager

        self.triggered.connect(self.remove)

    def remove(self):
        self.dock_manager.getPerspectivesManager().removePerspective(self.name)
