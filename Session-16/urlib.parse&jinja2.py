#urlparse, parse_qs to simplify the parsing of the URL

URL = "http://localhost:63342/operation?seq=AACC&operation=Info"
part = parse_qs(URL)[0]

print(urlparse("http://localhost:63342/operation?seq=AACC&operation=Info"))

#ver fotos del día 19 de abril de 2022 sobre las funciones urlparse, parse_qs
#ver tmb la de jinja2, es otra forma de cambiar los html files en vez de usar el .format()