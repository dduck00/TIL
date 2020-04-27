import codecs

if __name__ == "__main__":
    with codecs.open("book.html", "r", encoding="utf8") as file:
        bookMarkFile = file.read()
        bookMarkFile = bookMarkFile.split("<DT>")
        bookMarkFile = list(set(bookMarkFile))
        bookMarkFile.sort()
        new = codecs.open("newFile.html", "w", encoding="utf8")
        for page in bookMarkFile:
            new.write("<br>" + page)