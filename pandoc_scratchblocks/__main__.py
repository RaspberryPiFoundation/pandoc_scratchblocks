#!/usr/bin/env python2
from .pandocfilters import toJSONFilter, Str, Para, Image

import shutil
import sys
import os
import os.path
import subprocess
from string import Template

from tempfile import mkdtemp

base = os.path.dirname(__file__)
scratchblocks2 = os.path.join(base, "scratchblocks2")
rasterize = os.path.join(base, "rasterize.js")
jquery = os.path.join(base, "jquery.min.js")

with open(os.path.join(base, "scratch_template.html")) as fh:
    html_template = Template(fh.read())

tempdir = None

count = 0 

def block_to_image(block, output_dir):
    global count
    html_file = os.path.join(tempdir, "%d.html"%(count))
    image_file = os.path.join(output_dir, "%d.png"%(count))
    count +=1

    with open(html_file,"wb") as fh:
        raw = html_template.substitute(block=block)
        fh.write(raw)

    subprocess.check_call(['phantomjs', rasterize, html_file, image_file])
    return image_file
    
    
def render_blocks(key, value, format, meta):
    if key == "CodeBlock":
        [[ident,classes,keyvals], code] = value

        if u"blocks" in classes:
            image = block_to_image(code, os.getcwd())
            alt = Str(code)
            return Para([Image([alt], [image,""])])


def log(*a):
    for x in a:
        print >> sys.stderr, x,
    print >> sys.stderr, ""

if __name__ == '__main__':
    try:
        tempdir = mkdtemp()
        shutil.copytree(scratchblocks2, os.path.join(tempdir, "scratchblocks2"))
        shutil.copy(jquery, tempdir)

        toJSONFilter(render_blocks)

    finally:
        shutil.rmtree(tempdir)

