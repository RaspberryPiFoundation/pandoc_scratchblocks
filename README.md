# Abandon all hope, all ye who enter here

This is a terrible, no good, awful, just plain bad pandoc filter to translate scratchblocks2 markup into images.

Using the --filter option for pandoc, it looks for blocks marked up with `blocks` as the code type, translates them into html, runs it inside phantomjs and captures it into an image.

Requires

- Phantomjs
- Python
- Pandoc
- Tears
