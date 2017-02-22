# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date:   2017-02-22 15:28:00
# @Last Modified time: 2017-02-22 18:18:27

import sublime
import sublime_plugin

class TransferSashaSublimePreferencesCommand(sublime_plugin.WindowCommand):
    def run(self):
        ans = sublime.ok_cancel_dialog(
            "Do you in truth want to transfer the settings? "
            "WARNING: you can not undo this operation. "
            "Please, to create archive copy of your "
            "User/Preferences.sublime-settings file, "
            "that you can rollback changes, if you don't like my preferences."
        )
        if not ans:
            return
        # load the settings to transfer
        res = sublime.load_resource(
            "Packages/SashaSublime/Preferences.sublime-settings")
        my_settings = sublime.decode_value(res)
        # transfer the settings to the user settings
        user_settings = sublime.load_settings("Preferences.sublime-settings")
        for k, v in my_settings.items():
            user_settings.set(k, v)
        # save the user settings
        sublime.save_settings("Preferences.sublime-settings")