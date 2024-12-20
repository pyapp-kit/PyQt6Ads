from pathlib import Path

from pyqtbuild import PyQtBindings, PyQtProject


class PyQt6Ads(PyQtProject):
    def __init__(self):
        super().__init__()
        self.bindings_factories = [ads]


class ads(PyQtBindings):
    def __init__(self, project):
        super().__init__(project, "ads")

    def apply_user_defaults(self, tool):
        """Set default values for user options that haven't been set yet."""
        root = Path(self.project.root_dir)
        resource_file = str(root / "Qt-Advanced-Docking-System" / "src" / "ads.qrc")

        print("Adding resource file to qmake project: ", resource_file)
        self.builder_settings.append("RESOURCES += " + resource_file)
        super().apply_user_defaults(tool)
