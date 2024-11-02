from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

grid = [[False for _ in range(256)] for _ in range(64)]

def set_pixel(x, y, on):
    grid[y][x] = False if on == 'FALSE' else True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/updateGrid')
def updateGrid():
    global grid
    grid = [[False for _ in range(256)] for _ in range(64)]
    code = request.args.get('code')
    exec(code)
    return json.dumps({"status": "success"})

@app.route('/fetchGrid')
def getGrid():
    return json.dumps({"grid": grid})


if __name__ == '__main__':
    app.run(debug=True)

#  /project_root
#     /static
#         /css
#             styles.cssƒ
#         /js
#             scripts.js
#         /images
#             logo.png
#     /templates
#         index.html
#     app.py