#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import re

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        if self.path == '/api/files':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            
            # 获取当前目录下的所有md文件
            files = []
            for filename in os.listdir('.'):
                if filename.endswith('.md'):
                    # 匹配日期格式 YYYY-MM-DD.md
                    match = re.match(r'(\d{4}-\d{2}-\d{2})\.md', filename)
                    if match:
                        files.append(match.group(1))
            
            files.sort(reverse=True)  # 按日期倒序排列
            self.wfile.write(json.dumps(files, ensure_ascii=False).encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    PORT = 8000
    server = HTTPServer(('localhost', PORT), CustomHandler)
    print(f'服务器已启动，请访问 http://localhost:{PORT}')
    print('按 Ctrl+C 停止服务器')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n服务器已停止')
        server.server_close()
