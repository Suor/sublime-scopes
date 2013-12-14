# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import re


#  TODO:
#  (separate for each language)
#  - detect function
#  - detect function scope (func - name - decorators)
#  - detect class
#  - detect class scope
#  - detect block
#  - detect paragraph (in text or comments)
#  - choose between paragraph, block, function or class automatically
#  (language independent)
#  - select scope
#  - delete scope
#  - Ctrl-D enchanced
#  - select all in scope


class SelectFuncCommand(sublime_plugin.TextCommand):
     def run(self, edit):
        print('select_func')
