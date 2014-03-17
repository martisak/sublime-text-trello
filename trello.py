import sublime, sublime_plugin, re

import sys, os.path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
    
from progress_notifier import ProgressNotifier

import trollop

# A base for each command
class TrelloCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.setup_data_from_settings()
        
        if not self.token:
            self.show_output_panel(self.help_text())
            return
            
        if not self.use_cache:
            self.view.run_command("trello_delete_cache")

        trello_connection = trollop.TrelloConnection(self.key, self.token)
        self.defer(lambda: self.work(trello_connection))

    def setup_data_from_settings(self):
        default_settings = sublime.load_settings("Default_app.sublime-settings")
        user_settings    = sublime.load_settings("Trello.sublime-settings")

        self.key    = default_settings.get("key")    or user_settings.get("key")
        self.secret = default_settings.get("secret") or user_settings.get("secret")
        self.token  = user_settings.get("token")
        self.use_cache = user_settings.get("use_cache", True)
        self.renavigate = user_settings.get("keep_navigate_open_after_action", True)

    def help_text(self):
        first  = "Sorry for the interruption, in order to use the package please go to:\n%s\nand paste the token in the settings (Preferences -> Package Settings -> Trello -> Settings User)." % self.token_url()
        middle = "If you don't want to use the default app, you can change the key and the secret too, just go to:\n%s\nand copy paste both to the settings :)" % self.key_secret_generator_url()
        last   = "For more info, you can go to: https://github.com/NicoSantangelo/sublime-text-trello"
        return "%s\n\n%s\n\n%s" % (first, middle, last)

    def token_url(self):
        return "https://trello.com/1/connect?key=%s&name=sublime_app&response_type=token&scope=read,write" % self.key

    def key_secret_generator_url(self):
        return "https://trello.com/1/appKey/generate"

    # Main method, override
    def work(self, connection):
        pass

    # Panels and message
    def display_message(self, text):
        sublime.active_window().active_view().set_status("trello", text)

    def show_quick_panel(self, items, on_done = None, on_highlighted = None, selected_index = -1):
        sublime.set_timeout(lambda: self.view.window().show_quick_panel(items, on_done, sublime.MONOSPACE_FONT, selected_index, on_highlighted), 0)

    def show_input_panel(self, caption, initial_text = "", on_done = None, on_change = None, on_cancel = None):
        self.view.window().show_input_panel(caption, initial_text, on_done, on_change, on_cancel)

    # Output view
    def show_output_panel(self, text):
        self.output_view = self.view.window().get_output_panel("textarea")
        self.append_to_output_view(text)
        self.view.window().run_command("show_panel", {"panel": "output.textarea"})

    def append_to_output_view(self, text):
        self.output_view.set_read_only(False)
        self.output_view.run_command("append", { "characters": text })
        self.output_view.set_read_only(True)

    # Helpers
    def defer(self, fn):
        self.async(fn, 0)
        
    def async(self, fn, delay):
        self.progress = ProgressNotifier('Trello: Working')
        sublime.set_timeout_async(lambda: self.call(fn), delay)

    def call(self, fn):
        fn()
        self.progress.stop()