# dombrute

A tool for discovering the JavaScript parameters on a website 

## What it does

dombrute works by setting up a proxy in the Chrome browser and serving a wordlist to the tool via an HTTP server. The proxy server then receives the response from the target URL and adds some JavaScript before returning the response to the browser. The JavaScript will then send a request to the HTTP server to retrieve the wordlist, parse it, and add it to the URL. Finally, the tool checks if there is any parameter value in the content. If there is, it will save the URL and the parameter in a `found.txt` file.

## How to install

### On Linux

1.  Clone the repository: `git clone https://github.com/alanEG/dombrute`
2.  Change into the directory: `cd dombrute`
3.  Install the requirements: `pip install -r requirment.txt`
4.  Install `mitmproxy` and `chromium-browser`: `apt install mitmproxy chromium-browser`

### On Windows

1.  Clone the repository: `git clone https://github.com/alanEG/dombrute`
2.  Change into the directory: `cd dombrute`
3.  Install the requirements: `pip3 install -r requirment.txt`
4.  Download and install `mitmproxy` from [https://mitmproxy.org/](https://mitmproxy.org/)
5.  Download and install the Chrome browser from [https://www.chromium.org/getting-involved/download-chromium/](https://www.chromium.org/getting-involved/download-chromium/)

## How to use

1.  Run the tool: `python3 dombrute.py -f urls_file`
2.  Alternatively, you can pipe in a list of URLs: `cat urls.txt | python3 dombrute.py -s`

## Command line arguments

dombrute has several command line arguments that you can use to customize your run. You can view the list of arguments by running `./dombrute.py -h` in your terminal.

## Contributing

Contributions are always welcome! If you have an idea or feature request, please feel free to open an issue or submit a pull request.
