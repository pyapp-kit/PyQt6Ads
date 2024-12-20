import os
from pathlib import Path
import site
import sys

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

        # Add environment variable settings for isolated build
        site_pkg = Path(site.getsitepackages()[0])
        qt_lib_dir = str(site_pkg / "PyQt6" / "Qt6" / "lib")

        if sys.platform == "darwin":
            os.environ["DYLD_LIBRARY_PATH"] = (
                qt_lib_dir + os.pathsep + os.environ.get("DYLD_LIBRARY_PATH", "")
            )
            os.environ["LDFLAGS"] = f"-L{qt_lib_dir} " + os.environ.get("LDFLAGS", "")

        elif sys.platform == "win32":
            os.environ["PATH"] = qt_lib_dir + os.pathsep + os.environ.get("PATH", "")
            os.environ["LIB"] = qt_lib_dir + os.pathsep + os.environ.get("LIB", "")

        print("Adding resource file to qmake project: ", resource_file)
        self.builder_settings.append("RESOURCES += " + resource_file)
        super().apply_user_defaults(tool)
