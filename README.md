# HTMLScanner


HTMLScanner is a web scapping regex based tool.

  - Enter a URL and show up all text based on regex
  - Easy to use
  - Easy set-up

# New Features!

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
```

### TODO

 - Update regex support

