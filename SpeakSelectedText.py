import subprocess
import sublime, sublime_plugin

class SpeakSelectedTextCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    begin = self.view.sel()[0].begin()
    max_length = 10000
    region = sublime.Region(begin, min(begin + max_length, self.view.size()))
    text = self.view.substr(region)

    if getattr(self, 'process', None):
      self.process.kill()
      self.process = None
    else:
      self.process = subprocess.Popen(['say', text])
