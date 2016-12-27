# Fontstellations

This repo contains the code and data for the Fontstellations project, available [here](https://datascopeanalytics.com/fontstellations/)
(Open with Chrome or Firefox web browsers).
To learn more about the context of this project, you can read this [blog post](https://datascopeanalytics.com/blog/fontstellations/).

## File structure

The Scripts folder contains all the Python scripts and JSON files I used to scrape and save data from fontsinuse.com. 
It also contains scripts to edit (clean, filter, format) these JSON objects and some to resize/compress the PNG labels of the fonts.

The ForceGraph folder contains the files to render de the visualization. It was built with D3.js (v4), using Mike Bostock's 
[Force-directed graph](https://bl.ocks.org/mbostock/4062045) as a basis.
