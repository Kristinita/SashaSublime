# -*- coding: utf-8 -*-
import sublime, sublime_plugin, webbrowser

class sasha_sublime_issues(sublime_plugin.TextCommand):
    def run(self, edit):
        webbrowser.open_new_tab('https://github.com/Kristinita/SashaSublime/issues/new')
