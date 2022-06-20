import sublime
import sublime_plugin
import os
import ctypes

basedir = os.path.abspath(os.path.dirname(__file__))
libpath = os.path.join(basedir, 'lua-beautifier.so')
so = ctypes.CDLL(libpath)

beautify = so.beautify
beautify.argtypes = [ctypes.c_char_p]
beautify.restype = ctypes.c_void_p

class beautify_lua(sublime_plugin.TextCommand):
	def run(self, edit):
		if not self.view.settings().get("syntax").endswith("Lua.sublime-syntax"):
			return
		
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		ptr = beautify(contents.encode('utf-8'))
		if ptr is None:
			return
		out = ctypes.string_at(ptr).decode('utf-8')
		self.view.replace(edit, sublime.Region(0, self.view.size()), out)
