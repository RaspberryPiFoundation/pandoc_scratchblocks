#!/bin/bash
export PYTHONPATH=`pwd`

pandoc -f markdown_github+header_attributes+yaml_metadata_block+inline_code_attributes -t html5 -s --highlight-style pygments --section-divs example.md -o example.html --filter "./filter.sh"

pandoc -f markdown_github+header_attributes+yaml_metadata_block+inline_code_attributes -t latex -s --highlight-style pygments --section-divs example.md -o example.pdf --filter "./filter.sh"

