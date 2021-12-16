from requests.api import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browsermobproxy import Server
import time
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv
import os 
# DesiredCapabilities cap = DesiredCapabilities.chrome();
# LoggingPreferences logPrefs = new LoggingPreferences();
# logPrefs.enable(LogType.PERFORMANCE, Level.ALL);
# cap.setCapability(CapabilityType.LOGGING_PREFS, logPrefs);
# RemoteWebDriver driver = new RemoteWebDriver(new URL("http://127.0.0.1:9515"), cap);
  
# Main Function

load_dotenv()
DRIVER_PATH = os.environ.get("DRIVER_PATH")
PROXY_PATH =  os.environ.get("PROXY_PATH")

try:
    os.mkdir(os.path.join(os.getcwd(),"har-files"))
except:
    pass

if __name__ == "__main__":
    
    # Enter the path of bin folder by
    # extracting browsermob-proxy-2.1.4-bin
    path_to_browsermobproxy = PROXY_PATH
  
    # Start the server with the path and port 8090
    server = Server(path_to_browsermobproxy, options={'port': 9090})
    server.start()
  
    # Create the proxy with following parameter as true
    proxy = server.create_proxy()
  
    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()
  
    # Chrome will start in Headless mode
    options.add_argument("--proxy-server={0}".format(proxy.proxy))
  
    # Ignores any certificate errors if there is any
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--headless')
    options.add_argument("--disabled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-ip-pooling")
    options.add_argument("--disable-async-dns")
    options.add_argument("--disable-background-mode")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-bundled-ppapi-flash")
    options.add_argument("--disable-component-update")
    options.add_argument("--disable-crl-sets")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-dhcp-wpad")
    options.add_argument("--disable-ntp-other-sessions-menu")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--disable-restore-session-state")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-preconnect")
    options.add_argument("--disable-web-sockets")
    options.add_argument("--disable-webgl")
    options.add_argument("--disable-webaudio")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--no-sandbox")
    options.add_argument("--no-pings")
    options.add_argument("--incognito")
    options.add_argument('--start-maximized')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-sync-dictionary")
    options.add_argument("--disable-full-history-sync")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-infobars")
    options.add_argument("--host-resolver-retry-attempts=0")
    options.add_argument("--single-process")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--bwsi")
    options.add_argument("--script-badges")
    options.add_argument("--reset-variation-state")
    options.add_argument("--log-net-log=/tmp/chromium.log")

    options.add_argument("--blink-settings=imagesEnabled=false")

    # chrome_options.add_argument("--ignore-certificate-errors")
    proxy_address = "--proxy=127.0.0.1:%s" % proxy.port
    # Setting up Proxy for chrome
    
  
    # Startup the chrome webdriver with executable path and
    # the chrome options as parameters.
    driver = webdriver.Chrome(executable_path=DRIVER_PATH,service_args=[ proxy_address, '--ignore-ssl-errors=yes'],
                              options=options)
  
    # Create a new HAR file of the following domain
    # using the proxy.
    proxy.new_har("kijiji",options={'captureHeader':True,'captureContent':True})
  
    # Send a request to the website and let it load
    driver.get("https://www.kijijiautos.ca/cars/chevrolet/trax/used/#vip=20039321")

    # driver.get("https://torguard.net/whats-my-ip.php")
  
    proxy.har
    # Sleeps for 10 seconds
    time.sleep(60)

    
    name = url.split('.')[1]
    print(name)
  
    # Write it to a HAR file.
    with open(f"har-files/{name}.har", "w",encoding="utf-8") as f:
        json.dump(proxy.har, f)
  
    print("Quitting Selenium WebDriver")

    driver.quit()
    
  
    # Read HAR File and parse it using JSON
    # to find the urls containing images.
    # har_file_path = "network_log1.har"
    # with open(har_file_path, "r") as f:
    #     logs = json.loads(f.read())
  
    # # Store the network logs from 'entries' key and
    # # iterate them
    # network_logs = logs['log']['entries']
    # for log in network_logs:
  
    #     # Except block will be accessed if any of the
    #     # following keys are missing
    #     try:
    #         # URL is present inside the following keys
    #         url = log['request']['url']
  
    #         # Checks if the extension is .png or .jpg
    #         if url[len(url)-4:] == '.png' or url[len(url)-4:] == '.jpg':
    #             print(url, end="\n\n")
    #     except Exception as e:
    #         # print(e)
    #         pass