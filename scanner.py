from sys import argv
from getopt import getopt
from requests import get
from re import findall


def scanner(url, regex):
    return findall(regex, get(url).text) if len(findall(regex, get(url).text)) > 0 else [chr(27) + "[0;31m" + "No Comments Found", ]


def scanner_file_local(file, regex):
    with open(file, "r", errors="ignore") as code:
        return findall(regex, code.read()) if len(findall(regex, code.read())) > 0 else [chr(27) + "[0;31m" + "No Comments Found", ]


def scanner_file(url, file, regex, delimeter="\n"):
    with open(file, "r", errors="ignore") as code:
        for addon in code.read().split(delimeter):
            if len(addon) < 2: addon = "index.html"
            yield [addon, findall(regex, get(url + addon).text) if len(findall(regex, get(url + addon).text)) > 0 else [chr(27) + "[0;31m" + "No Comments Found", ]]  # YIELD EACH URL COMMENTS)


if __name__ == '__main__':
    URL = None
    REGEX = "<!---(.*?)--->"
    FILE = None
    DELIMETER = "\n"

    for option, argument in getopt(argv[1:], ":u:r:f:D:")[0]:
        if option == "-u":
            URL = argument
        elif option == "-r":
            REGEX = argument
        elif option == "-f":
            FILE = argument
        elif option == "-D":
            DELIMETER = argument

    if not FILE and URL:
        print(chr(27) + "[0;33m" + "Comments Found:" + chr(27) + "[0;36m")
        for comment in scanner(URL, REGEX):
            print(" ", scanner(URL, REGEX).index(comment), ") ", comment)

    elif FILE and not URL:
        print(chr(27) + "[0;33m" + "Comments Found:" + chr(27) + "[0;36m")
        for comment in scanner_file_local(FILE, REGEX):
            print(" ", scanner_file_local(FILE, REGEX).index(comment), ") ", comment)

    elif FILE and URL:
        print(chr(27) + "[0;33m" + "Comments Found:" + chr(27) + "[0;36m")
        for addon_, comment in scanner_file(URL, FILE, REGEX, DELIMETER):
            print(addon_, ":")
            for comment_ in comment:
                print(" ", comment.index(comment_), ") ", comment_)
            print("\n")

    else:
        print("""
Usage:
    scanner.py -u <url> [options]
    scanner.py -f <file> [options]
        
Options:
    File: -f <file>
    Regex: -r <regex>
    Delimeter: -D <delimeter>
    
""")

