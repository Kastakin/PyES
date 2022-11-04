import sys

from ppg_runtime.application_context import cached_property
from ppg_runtime.application_context.PySide6 import ApplicationContext
from windows.window import MainWindow


class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec()

    @cached_property
    def app(self):
        """
        Overrides the default app function to pass in sys.argv to the
        QApplication object allowing to show the name of the app in
        titlebars such as MacOS and Linux
        """
        result = self._qt_binding.QApplication(sys.argv)
        result.setApplicationName(self.build_settings["app_name"])
        result.setOrganizationName(self.build_settings["app_name"])
        result.setApplicationVersion(self.build_settings["version"])
        return result

    @cached_property
    def main_window(self):
        return MainWindow()


if __name__ == "__main__":
    appctxt = AppContext()
    appctxt.run()
