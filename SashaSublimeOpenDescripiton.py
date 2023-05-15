# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import webbrowser


class sasha_sublime_open_description(sublime_plugin.TextCommand):

    def run(self, edit):
        webbrowser.open_new_tab(
            "https://Kristinita.netlify.app/Sublime-Text/SashaSublime")
