import argparse,sys,time,traceback
from core.chrome import *
from core.server import *
from core.mitmdump import *

def checkArgument(args):
    urls=[]
    if args.targetFile and args.targetFile != None:
        with open(args.targetFile,'r') as f:
            lines = f.read()
        urls.extend(lines.split('\n'))

    elif args.stdin:
        for line in sys.stdin:
            urls.append(line.strip("\ufeff").rstrip())
    else:
        print('You should specify one of the following arguments --target-file --stdin')
        sys.exit(1)
    return urls 

def main():
    parser = argparse.ArgumentParser(description='A script discover dom parameter')
    parser.add_argument('-v',  '--version',action='version',version='%(prog)s 1.0 beta')
    parser.add_argument('-s',  '--stdin',help='Read url from stdin',action='store_true')
    parser.add_argument('-tf', '--target-file',metavar="Target-file",dest='targetFile',help='\tURL file')
    parser.add_argument('-sp', '--server-port',metavar="Port",dest='serverPort',help='Http server port default 8911',default='8933')
    parser.add_argument('-pp', '--proxy-port',metavar="Port",dest='proxyPort',help='Proxy server port default 8912',default='8934')
    parser.add_argument('-w',  '--wordlist',metavar="Wordlist_location",help='Wordlist file',default=os.path.dirname(os.path.abspath(__file__)) + '/wordlist/parameter.txt')
    parser.add_argument('-c',  '--cookie',metavar="Cookie",help='Cookie')
    parser.add_argument('-o', '--output',metavar="Output",help="Output result")

    args = parser.parse_args()

    try:
        urls=checkArgument(args)

        chrome = Chrome(int(args.proxyPort),args.cookie,args.output)
        mitmdump = Mitmdump(int(args.proxyPort),'http://127.0.0.1:' + args.serverPort + '/words')
        server = Server(int(args.serverPort),args.wordlist)
        
        # start servers
        server.start_server()
        mitmdump.start_mitmdump()

        # Wait for all servers
        time.sleep(5)

        # Start enumeration
        chrome.run(urls)
        
        # stop servers
        server.stop_server()
        mitmdump.stop_mitmdump()
    except Exception as F:
        traceback.print_exc()
        sys.exit(1)
        
if __name__ == '__main__':
    main()