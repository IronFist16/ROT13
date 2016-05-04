#!/usr/bin/env python
import webapp2
import cgi
import string

def escape_html(s):
	return cgi.escape(s, quote=True)

def process_text(text):
	max_len = len(string.ascii_lowercase)
	text_out = ''
	remap = {}
	for c in text:
		if c in remap:
			text_out += remap[c]
		else:
			if c.islower():
				i=(string.ascii_lowercase.index(c)+13) % max_len
				new_c = string.ascii_lowercase[i]

			elif c.isupper():
				i=(string.ascii_uppercase.index(c)+13) % max_len
				new_c = string.ascii_uppercase[i]

			else:
				new_c = c

			text_out += new_c
			remap[c] = new_c #Build a dictionary for fast caching
	return text_out

form = """
<!DOCTYPE html>
<html>
    <head>
    	<title>ROT13 Home Work</title>
    </head>

    <body>
    	<h2>Enter some text to ROT13:</h2>
    	<form method="post">
    		<textarea name="text"
    		style="height:100px; width:400px;" 
    		placeholder="Enter some text to encrypt...">{text_value}</textarea>
    		<br>
    		<input type="submit" value="Submit Query">
    	</form>
    </body>
</html>
"""
class MainPage(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(form.format(text_value=''))

	def post(self):
		text = self.request.get('text')
		self.response.out.write(form.format(text_value=process_text(text)))


app = webapp2.WSGIApplication([
	('/', MainPage)], debug=True)
