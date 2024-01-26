from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from core.init import *
import re, requests,os, platform, sys


PathTool = os.path.dirname(os.path.abspath(__file__))

class Chrome:
    def __init__(self,proxyPort,cookie,output_file):
        self.proxyPort = proxyPort 
        self.fileSl = initFileSl()
        self.cookie = []
        self.chromedriver_location = self.get_chromedriver_location()

        if not output_file:
            output_file = os.getcwd() + 'found.txt'

        self.output_file = output_file

        if cookie:
            self.cookie=self.parseCookie(cookie)

    def get_chromedriver_location(self):
        os_platform = platform.platform().lower()
        if "linux" in os_platform: 
            return PathTool + '/../' + 'chromedriver'
        elif "windows" in os_platform:
            return PathTool + '\\..\\' + 'chromedriver'
        else:
            print(f"Unknown platform {os_platform}")
            sys.exit(1)

    def parseCookie(self,cookie):
        cookie = cookie.split(';')
        FinalCookie = []
        for cook in cookie:
            cook = cook.split('=');
            FinalCookie.append({"name": cook[0].replace(' ',''), "value": cook[1]})

        return FinalCookie

    def save(self,url,parameter="",wher="",message="",type="found"):
        with open(self.output_file,'a+') as f:
            if (type == "found"):
                f.write(f"Found[{parameter}][{wher}]: {url}\n")
            elif (type == "skip"):
                f.write(f"Skip[{message}]: {url}")
            
    def check(self,url, content):
        search = re.findall('(1HeWkAJ3[a-zA-Z0-9_-]+)',content)
        if search:
            if len(search) > 1000:
                print(f"[Skip][all parameters are reflected]: {url}")
                self.save(url,message="All parameters are reflected",type="skp")
                return 

            for value in search:
                found = re.findall('1HeWkAJ3([a-zA-Z0-9_-]+)',value)
                for fd in found:
                    typeFd=fd[-1]
                    fd=fd[:-1]
                    if 's' in typeFd:
                        print(f"Found[{fd}][location.search]: {url}")
                        self.save(url,fd,'location.search')
                    elif 'h' in typeFd:
                        print(f"Found[{fd}][location.hash]: {url}")
                        self.save(url,fd,'location.hash')

    def lanuchChrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--proxy-server=http://localhost:" + str(self.proxyPort) + "," + "https://localhost:" + str(self.proxyPort))
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        options.headless = True
        
        # Initialize a web driver
        driver = webdriver.Chrome(self.chromedriver_location,options=options)
        driver.set_page_load_timeout(30)

        # Navigate to a URL
        return driver

    def addCookie(self,driver,cookie,url):
        for cook in cookie:
            cook.update({'domain':url.split('/')[2]})
            driver.add_cookie(cook)

    def add_log(self,res,url):
        with open('fail_proxy.txt','a+') as f:
            f.write(f"[{res}]: {url}\n")

    def run(self,urls):
        driver = self.lanuchChrome()
        for url in urls:
            print(f'[Start]: {url}')
            
            if url.startswith('https://') or url.startswith('http://'):
                response = ""
                try:
                    response = requests.get(url,timeout=5)
                    if len(response.content) > 0:
                        if not 'Content-Type' in response.headers:
                            if '<html' in str(response.content):
                                response.headers['Content-Type'] = 'text/html'
                            else:
                                response.headers['Content-Type'] = 'image/png'
                            # check if response is zero or not
                        if 'text/html' in response.headers['Content-Type']:
                            try:
                                driver.get(url)
                                if self.cookie:
                                    self.addCookie(driver,self.cookie,url);
                                    driver.get(url)

                                self.check(url,driver.page_source)
                            except Exception as e:
                                driver.quit()
                                driver=self.lanuchChrome()
                                print(e)
                        else:
                            self.add_log("Not_Html",url)
                            print(f'[Skip][Not text/html or status][{response.headers["Content-Type"]}]: {url}')
                    else:
                        self.add_log("Zero_content_length",url)
                        print(f"[Skip]: Zero content_length")
                except Exception as e:
                    self.add_log(e,url)
                    print(f":[Error_request]: {e}, {url}")
            else:
                self.add_log('Not http/https',url)
                print(f'[Skip][Not http/https]: {url}')
        driver.quit()
