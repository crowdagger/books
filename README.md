# Some Rust books conversion 

The purpose of [this repository](https://github.com/lise-henry/books)
is to try to provide PDF and EPUB vesions of Rust books. Currently,
there is only an early attempt at converting the second version of [*The Rust
Programming Language*](https://github.com/rust-lang/book), which you
can look at here:

* [PDF](http://lise-henry.github.io/books/trpl2.pdf)
* [EPUB](http://lise-henry.github.io/books/trpl2.epub).

## Why?

Because this book is cool, but I personally prefer to read on a
ereader than on computer screen. Plus my
pet project is building [yet another converter from Markdown books to
PDF, EPUB and HTML](https://github.com/lise-henry/crowbook) converter from Markdown books to PDF, EPUB and HTML, so I wanted to know if it could work on this kind
of books.

## Status and what's next

The files are existing, so it somewhat works. They could be better,
though. Particularly, I didn't manage to get the syntax highlighting
on LaTeX, this is something I plan to work on. 

I'd also like to try to see how this works on other books. Later. Maybe.

## How? 

I used [Crowbook](https://github.com/lise-henry/crowbook), yet another
converter from Markdown books to PDF, EPUB and HTML. The [book
configuration file](https://github.com/lise-henry/books/blob/master/trpl2.book) is
here. 

If you want to play with that too, you'll need the Github version of
crowbook, since I had to do some tweaking to get The Rust Lang Book to
work under it. Then

```
$ git clone https://github.com/lise-henry/books/
$ cd books
$ crowbook trpl2.ebook
```

Since the source files are in a git submodule you might need to do
some git magic. Honestly, I am not sure of how that works so I won't
be able to help you on that.

Keeping these versiong up to date should not be too difficult, as long
as the structure of the 
