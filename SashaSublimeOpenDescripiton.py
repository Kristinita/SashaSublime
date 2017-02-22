# -*- coding: utf-8 -*-
import sublime, sublime_plugin, webbrowser

class sasha_sublime_open_description(sublime_plugin.TextCommand):
    def run(self, edit):
        webbrowser.open_new_tab('http://Kristinita.ru/Sublime-Text/SashaSublime')
