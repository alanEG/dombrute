import subprocess,threading,os 

class Mitmdump:
    def __init__(self,proxyPort,wordlistUrl):
        self.proxyPort = proxyPort
        self.wordlistUrl = wordlistUrl 
        self.stop_event = threading.Event()

    def start_mitmdump(self):
        global mitmdump, stop_event
        mitmdump = subprocess.Popen(["mitmdump","-q","-p", str(self.proxyPort), "-s", os.path.dirname(os.path.abspath(__file__)) + "/proxy_replace.py", self.wordlistUrl])
        self.stop_event.clear()

    def stop_mitmdump(self):
        global mitmdump, stop_event
        if mitmdump:
            self.stop_event.set()
            mitmdump.terminate()
            mitmdump.wait()
            mitmdump = None
