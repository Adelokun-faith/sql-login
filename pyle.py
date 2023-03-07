print()


import cgi
print("<h1>Welcome to python Python Web Mysql Application</h1>")
print("<hr/>")
print("<body bgcolor='#3e3e3e'>")

form = cgi.FieldStorage()


id = form.getvalue("id")
username = 