import subprocess,threading,os 
from core.init import *

class Mitmdump:
    def __init__(self,proxyPort,wordlistUrl):
        self.proxyPort = proxyPort
        self.wordlistUrl = wordlistUrl 
        self.stop_event = threading.Event()
        self.fileSl = initFileSl()

    def start_mitmdump(self):
        global mitmdump, stop_event
        scriptLocation = os.path.dirname(os.path.abspath(__file__)) + str(self.fileSl) + "proxy_replace.py"
        mitmdump = subprocess.Popen(["mitmdump","-q","-p", str(self.proxyPort), "-s", scriptLocation, self.wordlistUrl])
        self.stop_event.clear()

    def stop_mitmdump(self):
        global mitmdump, stop_event
        if mitmdump:
            self.stop_event.set()
            mitmdump.terminate()
            mitmdump.wait()
            mitmdump = None