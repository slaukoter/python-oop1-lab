#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.title = title
        self._author = None
        self._page_count = page_count
        self._genre = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
