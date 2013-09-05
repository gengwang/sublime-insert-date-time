import sublime, sublime_plugin
import locale, time

class InsertDateTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit, format='s'):
		self.date_time_tring(edit, format)

	# @param format: 'f' (date and time), 's' (date only)
	def date_time_tring(self, edit, format):
		locale.setlocale(locale.LC_TIME, '')
		# date_format = locale.nl_langinfo(locale.D_FMT)

		local_time_and_date = time.strftime('%X') + ' ' + time.strftime('%x')
		local_date = time.strftime('%x')

		selection = self.view.sel()[0].begin()

		if format == 'f':
			self.view.insert(edit, selection, str(local_time_and_date))
		else:
			self.view.insert(edit, selection, str(local_date))