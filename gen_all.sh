#!/bin/sh

echo Generate EPUB, HTML and A5 version
crowbook trpl1.book
crowbook trpl2.book
crowbook trpl-2018.book
crowbook cargo.book

echo Generate A4 version
crowbook trpl1.book --to pdf --set tex.paper_size a4paper output.pdf trpl1-a4.pdf
crowbook trpl2.book --to pdf --set tex.paper_size a4paper output.pdf trpl2-a4.pdf
crowbook trpl-2018.book --to pdf --set tex.paper_size a4paper output.pdf trpl-2018-a4.pdf
crowbook cargo.book --to pdf --set tex.paper_size a4paper output.pdf cargo-a4.pdf

echo Generate letter version
crowbook trpl1.book --to pdf --set tex.paper_size letterpaper output.pdf trpl1-letter.pdf
crowbook trpl2.book --to pdf --set tex.paper_size letterpaper output.pdf trpl2-letter.pdf
crowbook trpl-2018.book --to pdf --set tex.paper_size letterpaper output.pdf trpl-2018-letter.pdf
crowbook cargo.book --to pdf --set tex.paper_size letterpaper output.pdf cargo-letter.pdf

