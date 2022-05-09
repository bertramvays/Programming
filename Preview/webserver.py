"""
Реализация веб-сервера на языке Пайтонб способная запускать серверные CGI-сценарии
на языке Пайтон; обслуживает файлы и сценарии в текущем рабочем каталоге; сценари
на языке Пайтон должны находиться в каталоге webdir\cgi-bin или webdir\htbin;
"""
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler


webdir = '.'  # место, где находятся файлы html и подкаталог cgi-bin
port = 80    # по умолчанию http://localhost/, иначе используйте
             # http://localhost:xxxx/
os.chdir(webdir)  # перейти в корневой каталог HTML
srvaddr = ("", port)  # имя хоста и номер порта
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()  # запустить как бесконечный фоновый процесс
