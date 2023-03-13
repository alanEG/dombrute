# dombrute

A tool designed to help identify JavaScript parameters, which can be useful in detecting DOM XSS vulnerabilities. If a parameter is being handled by JavaScript and its value is being printed in the code, this tool will be able to detect it.

## What it does

dombrute works by setting up a proxy in the Chrome browser and serving a wordlist to the tool via an HTTP server. The proxy server then receives the response from the target URL and adds some JavaScript before returning the response to the browser. The JavaScript will then send a request to the HTTP server to retrieve the wordlist, parse it, and add it to the URL. Finally, the tool checks if there is any parameter value in the content. If there is, it will save the URL and the parameter in a `found.txt` file.

## Installation
To install the requirments, run the appropriate installation file based on your platform:

For Windows, execute `install.bat`

For Linux, execute `install.sh`

You also need to install python-requirements: 
`pip install -r requirements.txt`

## How to use

- Run the tool: `python3 dombrute.py -tf urls_file`

- Alternatively, you can pipe in a list of URLs: `cat urls.txt | python3 dombrute.py -s`

[![asciicast](https://asciinema.org/a/JCAdfMyxYoOzLj5Aloi7Q1BHY.svg)](https://asciinema.org/a/JCAdfMyxYoOzLj5Aloi7Q1BHY)

<br>

## Command line arguments

```
usage: dombrute.py [-h] [-v] [-s] [-tf Target-file] [-sp Port] [-pp Port] [-w Wordlist_location] [-c Cookie]

A script discover dom parameter

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -s, --stdin           Read url from stdin
  -tf Target-file, --target-file Target-file
                        URL file
  -sp Port, --server-port Port
                        Http server port default 8911
  -pp Port, --proxy-port Port
                        Proxy server port default 8912
  -w Wordlist_location, --wordlist Wordlist_location
                        Wordlist file
  -c Cookie, --cookie Cookie
                        Cookie
```

## TODO 
- support multithreading

## Contributing

Contributions are always welcome! If you have an idea or feature request, please feel free to open an issue or submit a pull request.
