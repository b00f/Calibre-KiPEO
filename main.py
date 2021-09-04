# The base class that all tools must inherit from
from calibre.gui2.tweak_book.plugin import Tool
from calibre.gui2 import error_dialog
from qt.core import QAction, QMessageBox
from calibre_plugins.kipeo import reshaper

class KiPEOTool(Tool):
    name = 'KiPEOTool'
    allowed_in_toolbar = True
    allowed_in_menu = True

    def create_action(self, for_toolbar=True):
        ac = QAction(get_icons('images/icon.png'), 'Reshape book by KiPEO', self.gui)
        if not for_toolbar:
            self.register_shortcut(ac, 'kipeo-tool', default_keys=('Ctrl+Shift+Alt+D',))
        ac.triggered.connect(self.start_reshape)
        return ac

    def start_reshape(self):
        # Ensure any in progress editing the user is doing is present in the container
        self.boss.commit_all_editors_to_container()
        try:
            self.reshape()
        except Exception:
            # Something bad happened report the error to the user
            import traceback
            error_dialog(self.gui, _('Failed to reshape fonts'), _(
                'Failed to reshape fonts, click "Show details" for more info'),
                det_msg=traceback.format_exc(), show=True)
            # Revert to the saved restore point
            self.boss.revert_requested(self.boss.global_undo.previous_container)

    def reshape(self):
        self.boss.add_savepoint('Before: Reshape')

        container = self.current_container

        reshaper.reshape_book(container)

        self.show_success()

    def show_success(self):
        message = QMessageBox(self.gui)
        message.setIcon(QMessageBox.Information)
        message.setText("KiPEO has completely reshaped your e-book.\r\n\r\nDo you like to see the changes?")
        message.setWindowTitle("KiPEO")
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.show()

        user_choice = message.exec_()
        if user_choice == QMessageBox.Yes:
            #Show the user what changes we have made, allowing her to
            #revert them if necessary
            self.boss.show_current_diff()
        #Update the editor UI to take into account all the changes we
        #have made
        self.boss.apply_container_update_to_gui()