# Builds index.html from template.html and the numbered source files in src/.
# Usage: python3 build.py
import glob
src = ''.join(open(f, encoding='utf-8').read() + '\n' for f in sorted(glob.glob('src/*.js')))
game = "(() => {\n'use strict';\n" + src + "\n})();"
t = open('template.html', encoding='utf-8').read()
cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
open('index.html', 'w', encoding='utf-8').write(t.replace('{{THREE}}', cdn).replace('{{GAME}}', game))
print('index.html written')
