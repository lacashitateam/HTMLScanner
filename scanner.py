from getopt import getopt
from re import findall
from sys import argv
from requests import get
from socket import socket, AF_INET, SOCK_STREAM


def scanner(url, regex):
    """
    :param url: Target URL
    :param regex: Regex
    :return: Array with ALL Found comments
    """

    request = get(url, headers=HEADERS)
    return findall(regex, request.text) if len(findall(regex, request.text)) > 0 else ["No Comments Found", ]


def scanner_file_local(file, regex):
    """
    :param file: Local file with .html code or kind of that
    :param regex: Regex
    :return: Array with ALL Found comments
    """

    with open(file, "r", errors="ignore") as code:
        returnArray = findall(regex, code.read())
        return returnArray if len(returnArray) > 0 else ["No Comments Found", ]


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
            request = get(url + addon, headers=HEADERS)
            if len(addon) < 2: addon = "index.html"
            yield [addon, findall(regex, request.text) if len(findall(regex, request.text)) > 0 else ["No Comments Found", ]]  # YIELD EACH URL COMMENTS)


def portScanner(url, initialPort, lastPort):
    for port in range(initialPort, lastPort + 1):
        try:
            yield port if not socket().connect_ex((url, port)) else "N/A"

        except KeyboardInterrupt:
            print(chr(27) + "\n\n[0;31mEXITING...")
            exit()

        except Exception:
            pass


URL = None
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
REGEX = "<!--(.*?)-->"
FILE = None
DELIMETER = "\n"
HELP = """
Usage:
    scanner.py -u <url> [options]
    scanner.py -f <file> [options]
    scanner.py -u <ip> -p <port> -P <port>

Options:
    File: -f <file>
    Regex: -r <regex>
    Delimeter: -D <delimeter>
    Initial Port: -p <port>
    Final Port: -P <port>

For more info look at:
 https://github.com/lacashitateam/HTMLScanner
 https://lacashita.com/projects/HTMLScanner

"""
PORT_START = None
PORT_FINISH = None

if __name__ == '__main__':
    try:
        for option, argument in getopt(argv[1:], "u:r:f:D:p:P:")[0]:
            if option == "-u":
                URL = argument
            elif option == "-r":
                REGEX = argument
            elif option == "-f":
                FILE = argument
            elif option == "-D":
                DELIMETER = argument
            elif option == "-p":
                PORT_START = int(argument)
            elif option == "-P":
                PORT_FINISH = int(argument)

        if URL and PORT_START and PORT_FINISH:
            print(chr(27) + "[0;33m" + "Open Ports:")
            for port in portScanner(URL, PORT_START, PORT_FINISH):
                if port != "N/A": print(chr(27) + "[0;36m" + " ", port, ") OPEN")

        elif URL and not FILE:
            print(chr(27) + "[0;33m" + "Comments Found:")
            commentArray = scanner(URL, REGEX)
            for comment in commentArray:
                print(chr(27) + "[0;36m" + " 0) " + chr(27) + "[0;31m", comment) if comment == "No Comments Found" else print(chr(27) + "[0;36m" + " ", commentArray.index(comment), ") ", comment)

        elif FILE and not URL:
            print(chr(27) + "[0;33m" + "Comments Found:")
            for comment in scanner_file_local(FILE, REGEX):
                print(chr(27) + "[0;36m" + " 0) " + chr(27) + "[0;31m", comment) if comment == "No Comments Found" else print(chr(27) + "[0;36m" + " ", scanner_file_local(FILE, REGEX).index(comment), ") ", comment)

        elif FILE and URL:
            print(chr(27) + "[0;33m" + "Comments Found:")
            for addon_, comment in scanner_file(URL, FILE, REGEX, DELIMETER):
                print(chr(27) + "[0;36m" + addon_, ":")
                for comment_ in comment:
                    print(chr(27) + "[0;36m" + " 0) " + chr(27) + "[0;31m", comment_) if comment_ == "No Comments Found" else print(chr(27) + "[0;36m" + " ", comment.index(comment_), ") ", comment_)
                print("\n")

        else:
            raise Exception("Invalid Arguments")

    except Exception as Error:
        print(chr(27) + "[0;31mERROR: {0}".format(Error))
        print(chr(27) + "[0;39m", HELP)
