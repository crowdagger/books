#!/usr/bin/python3

"""
Autogenerate the trpl2.book file from the contents of trpl/second-edition/src/SUMMARY.md.
"""

import os
import re

# meta information for .book file
HEADER = '''title: "The Rust Programming Language"
author: "Steve Klabnik and Carol Nichols, with Contributions from the Rust Community"
lang: en

crowbook.html_as_text: false
# tex.hyperref: false
rendering.highlight: syntect
tex.links_as_footnotes: false
rendering.num_depth: 2
rendering.inline_toc: true

resources.base_path.images: trpl/second-edition/src/img/
output.base_path: docs/

output.html: trpl2.html
output.epub: trpl2.epub
output.pdf: trpl2.pdf
'''

# find parts
PART_RE = re.compile(r'^## (.+)$')
# find chapters
CHAPTER_RE = re.compile(r'^- \[(.*?)\]\((.*)\)$')
# find sub-chapters
SUB_CHAPTER_RE = re.compile(r'^    - \[.*?\]\((.*)\)$')


def translate_summary(path, base):
    """Translate the Summary.md to .book format."""
    with open(os.path.join(path, base), 'r') as input_file_content:
        converted = HEADER
        for line in input_file_content:
            #print('checking line "{}"'.format(line))
            match = PART_RE.match(line)
            if match:
                #print("found part {}".format(match.group(1)))
                converted += '\n@ {}\n'.format(match.group(1))
            else:
                match = CHAPTER_RE.match(line)
                if match:
                    chapter_name = match.group(1)
                    chapter_path = match.group(2)
                    prefix = '+'
                    if chapter_name == 'Appendix':
                        prefix = '-'
                    converted += '{} {}/{}\n'.format(prefix, path, chapter_path)
                else:
                    match = SUB_CHAPTER_RE.match(line)
                    if match:
                        #print("found sub-chapter {}".format(match.group(1)))
                        sub_chapter = match.group(1)
                        if sub_chapter: # ignore empty sub-chapter entries in summary file
                            converted += '-- {}/{}\n'.format(path, sub_chapter)
    return converted


if __name__ == '__main__':
    INPUT_FILE_PATH = 'trpl/second-edition/src'
    INPUT_FILE_BASE = 'SUMMARY.md'
    OUTPUT_FILE = 'trpl2.book'
    with open(OUTPUT_FILE, 'w') as output:
        output.write(translate_summary(INPUT_FILE_PATH, INPUT_FILE_BASE))
