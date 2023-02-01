
# dombrute

A tool for discovering the JavaScript parameters

## How it works
chromium - This component sets the proxy in the Chrome browser to the proxy URL that is hosted.

http-server - This component is responsible for serving the wordlist to the tool.

proxy-server - This component receives the response from the target URL and adds some JavaScript before returning the response to 
the browser.

The JavaScript will then send a request to the http-server to retrieve the wordlist then parse it then push to url.
After the page loads, the tool checks if there is any parameter value in the content. If there is, the tool will save the URL and the parameter in a found.txt file.
# Installation

### linux
```
git clone https://github.com/alanEG/dombrute
cd dombrute 
pip install -r requirment.txt
apt install mitmproxy chromium-browser
```

### windows
```
git clone https://github.com/alanEG/dombrute
cd dombrute 
pip3 install -r requirment.txt
Download mitmproxy from https://mitmproxy.org/ and install
Download mini_installer.exe from https://www.chromium.org/getting-involved/download-chromium/ and install
```
## Using
`python3 dombrute.py -f urls_file`

Or

`cat urls.txt | python3 dombrute.py -s` 
## Documentation
Swhunt has many argument 
You can run `./swhunt.py -h` to show help 
```
usage: dombrute.py [-h] [-sp SERVERPORT] [-pp PROXYPORT] [-w WORDLIST] [-ss] [-c COOKIE] [-tf TARGETFILE] [-s]

A script discover dom parameter

optional arguments:
  -h,  --help           Show this help message and exit
  -sp, --server-port    Http server port default 8911
  -pp, --proxy-port     Proxy server port default 8912
  -w,  --wordlist       Wordlist file
  -c,  --cookie         Cookie
  -tf, --target-file    URL file
  -s,  --stdin          Read url from stdin
```

## Contributing

Contributions are always welcome!

