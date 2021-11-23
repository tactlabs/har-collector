# Import the required modules
from selenium import webdriver
from browsermobproxy import Server
import time
import json

PATH="/home/aravind/Featurepreneur/chromedriver"
# Main Function
if __name__ == "__main__":

	# Enter the path of bin folder by
	# extracting browsermob-proxy-2.1.4-bin
	path_to_browsermobproxy = "/home/aravind/Featurepreneur/browsermob-proxy-2.1.4/bin/browsermob-proxy"

	# Start the server with the path and port 8090
	server = Server(path_to_browsermobproxy, options={'port': 9090})
	server.start()

	# Create the proxy with following parameter as true
	proxy = server.create_proxy(params={"trustAllServers": "true"})

	# Create the webdriver object and pass the arguments
	options = webdriver.ChromeOptions()

	# Chrome will start in Headless mode
	options.add_argument('headless')

	# Ignores any certificate errors if there is any
	options.add_argument("--ignore-certificate-errors")

	# Setting up Proxy for chrome
	options.add_argument("--proxy-server={0}".format(proxy.proxy))

	# Startup the chrome webdriver with executable path and
	# the chrome options as parameters.
	driver = webdriver.Chrome(executable_path=PATH,options=options)

	# Create a new HAR file of the following domain
	# using the proxy.
	proxy.new_har("www.spaceishare.com/",options={'captureHeader':True,'captureContent':True})

	# Send a request to the website and let it load
	driver.get("https://spaceishare.com/")

	# Sleeps for 10 seconds
	time.sleep(60)

	# Write it to a HAR file.
	with open("spaceishare.har", "w", encoding="utf-8") as f:
		f.write(json.dumps(proxy.har))

	print("Quitting Selenium WebDriver")
	driver.quit()

	# Read HAR File and parse it using JSON
	# to find the urls containing images.
	har_file_path = "spaceishare.har"
	with open(har_file_path, "r", encoding="utf-8") as f:
		logs = json.loads(f.read())

	# Store the network logs from 'entries' key and
	# iterate them
	network_logs = logs['log']['entries']
	for log in network_logs:

	# 	# Except block will be accessed if any of the
	# 	# following keys are missing
		try:
			# URL is present inside the following keys
			url = log['request']['url']

			# Checks if the extension is .png or .jpg
			if url[len(url)-4:] == '.png' or url[len(url)-4:] == '.jpg':
				print(url, end="\n\n")
		except Exception as e:
			# print(e)
			pass
