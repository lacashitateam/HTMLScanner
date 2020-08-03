# HTMLScanner


HTMLScanner is a web scapping regex based tool.

  - Enter a URL and show up all text based on regex
  - Easy to use
  - Easy set-up

# New Features!

  - Port Scanner *(New Logic)*
  - Search for text on local files
  - Can be implemented to your projects


You can also:
  - Search for text on URL
  - Search for text on URL with file URL Addons
  - Create custom regex to search for

### Tech

HTMLScanner uses a number of open source projects to work properly:

* [Sys] - System-specific parameters and functions.
* [Requests] - Elegant and simple HTTP library for Python, built for human beings.
* [Getopt] - C-style parser for command line options.
* [Re] - Regular expression operations.
* [Nmap] -  Nmap in any of your python pentesting projects.

And of course HTMLScanner itself is open source.

### Installation

HTMLScanner requires [Python3.x](https://www.python.org/downloads/) to run.

Install the dependencies and start scanner.py.

```sh
$ cd HTMLScanner
$ python3 -m pip install -r requirements.txt
$ python3 scanner.py
```

For Web Scrapping on URL

```sh
$ python3 scanner.py -u http://github.com/
# This wil check for all comments on URL
```

For Web Scrapping on URL + ADDONS

```sh
$ python3 scanner.py -u http://github.com/ -f addonsList.txt

# This wil check for all URL addons:
#   http://github.com/addon1.html
#   http://github.com/addon2.html
#   http://github.com/etc...
```

For Web Scrapping on FILE

```sh
$ python3 scanner.py -f file.html
# This wil check for all comments on FILE
```

For Port Scanner

```sh
$ python3 scanner.py -u 192.168.1.x -p 1 -P 255
# This wil check for all open ports of a numeric ip:
#   -u numeric ip
#   -p Initial Port
#   -P Last Port
```

### USAGE MENU
```sh
Usage:
    scanner.py -u <url> [options]
    scanner.py -f <file> [options]
    scanner.py -u <ip> -p <port> -P <port>

Options:
    File: -f <file>
    Regex: -r <regex>
    Delimeter: -D <delimeter>
    Initial Port: -p <port> | --initial-port <port>
    Final Port: -P <port> | --final-port <port>
    Show Ports: --show-ports <all/open/closed/filtered>
```


### TODO

 - Update regex support

