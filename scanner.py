from sys import argv
from getopt import getopt
from requests import get
from re import findall


def scanner(url, regex):
    """
    :param url: Target URL
    :param regex: Regex
    :return: Array with ALL Found comments
    """
    return findall(regex, get(url).text) if len(findall(regex, get(url).text)) > 0 else [chr(27) + "[0;31m" + "No Comments Found", ]


def scanner_file_local(file, regex):
    """
    :param file: Local file with .html code or kind of that
    :param regex: Regex
    :return: Array with ALL Found comments
    """

    with open(file, "r", errors="ignore") as code:
        return findall(regex, code.read()) if len(findall(regex, code.read())) > 0 else [chr(27) + "[0;31m" + "No Comments Found", ]


def scanner_file(url, file, regex, delimeter):
    """
    :param url: Target URL
    :param file: File with URL Addons
    :param regex: Regex
    :param delimeter: Delimeter to split
    :return: generator [addon, comment]
    """

    with open(file, "r", errors="ignore") as code:
        for addon in code.read().split(delimeter):
            if len(addon) < 2: addon = "index.html"
            yield [addon, findall(regex, get(url + addon).text) if len(findall(regex, get(url + addon).text)) > 0 else [chr(27) + "[0;31m" + "No Comments Found", ]]  # YIELD EACH URL COMMENTS)


if __name__ == '__main__':
    URL = None
    REGEX = "<!---(.*?)--->"
    FILE = None
    DELIMETER = "\n"
    HELP = """
Usage:
    scanner.py -u <url> [options]
    scanner.py -f <file> [options]
        
Options:
    File: -f <file>
    Regex: -r <regex>
    Delimeter: -D <delimeter>
    
For more info look at:
 https://github.com/lacashitateam/HTMLScanner
 https://lacashita.com/projects/HTMLScanner
    
"""

    try:
        for option, argument in getopt(argv[1:], ":u:r:f:D:h")[0]:
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
            print(HELP)
    except:
        print(HELP)
