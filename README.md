# pandoc_scratchblocks

Pandoc filter to translate scratchblocks2 markup into images.

Using the --filter option for pandoc, it looks for blocks marked up with `blocks` as the code type, translates them into html, runs it inside phantomjs and captures it into an image.

## Requires

- Phantomjs
- Python
- Pandoc

## Worth noting

- We have to use a custom version of rasterize.js from phantomjs to crop the image to the dimensions of the scratch block, and also use some CSS magic to ensure the containing element matches the width of the scratch block.

- We've vendored scratchblocks.js, as well as pandocfilters to avoid dependencies.

- filter takes the name of an executable, so you can't pass arguments to the process.

## TODO

- Add a setup.py script so it can be installed.
