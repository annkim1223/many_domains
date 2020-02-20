import pandas
import os
from urllib.request import urlopen, Request
import time
from tld import get_tld, get_fld

if not os.path.exists("domain_html"):
	os.mkdir("domain_html")

df = pandas.read_csv("domains.csv")


for link in df['domain_name']:   # column named 'domain_name' in data frame matrix and call it link
	# try:
	# 	print("Downloading (1st): ", link)
	# 	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	# 	request_link = "https://www." +link
	# 	req = Request (url = request_link, headers = headers)
	# 	f = open("domain_html/" + link, "wb")   # wb: writing and binary
	# 	response = urlopen(req)
	# 	html = response.read()
	# 	#ValueError: unknown url type: '1001coques.fr' - it is hiding 'https://www.' from the real website address.  
	# 	#Downloading:  1010tires.com
	# 	# urllib.error.HTTPError: HTTP Error 403: Forbidden - the website caught that you are trying to read it by program
	# 		# python urlopen is very programming to request html from the server. Thus, being caught. 
	# 		# Then how do you make it leass programming? 
	# 		#(1) add headers (google urlopen headers) then req (request object) and then change req...
	# 	f.write(html)
	# except:
	# 	print("Downloading (2nd): ", link)
	# 	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	# 	request_link = "https://" +link
	# 	req = Request (url = request_link, headers = headers)
	# 	f = open("domain_html/" + link, "wb")   # wb: writing and binary
	# 	response = urlopen(req)
	# 	html = response.read()
	# 	f.write(html)
	# f.close()
	# # timesleep is less important here, cause it won't break the website, (??WHy?) but we will still do it.	
	# time.sleep(10) # 10 secs are more than enough.
# """
# Other problems that can be possible.

# (1) Some website has www. and some website does not have it. 
# 	: to distinguish them, we 'try' it before we open the url.
# (2) sometimes you see the website's subdomain
# 	: example) m.facebook.com - it is mobile domain for facebook.
# 	  example2) e.domain - email surver of the main domain
# 	  example3) alerts.dailymotion.com  - domain to send alearts of the main domain
# 	  Since there are multip possible subdomain formates, it is hard to get rid of them.
# 	   ( to illusttate it, add example3 link to the domains.csv, it will show error)
# 	  1) you can remove the subdomain format if there is only a few errors
# 	  2) if there are many multiple errors, you need to add a package to do that.
# 	  (tld package (below))
#     install: python -m pip install tld

# """
	print("Original: ",link)
	print(get_fld("fld version: " + 'http://' + link))
	f = open('domains_html/' + link, "wb")
	try:
		print("Downloading (1st): ", link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		fld_link = get_fld('http://' +link)
		request_link = "https://www." +link
		req = Request (url = request_link, headers = headers)
		f = open("domain_html/" + link, "wb")   # wb: writing and binary
		response = urlopen(req)
		html = response.read()
		#ValueError: unknown url type: '1001coques.fr' - it is hiding 'https://www.' from the real website address.  
		#Downloading:  1010tires.com
		# urllib.error.HTTPError: HTTP Error 403: Forbidden - the website caught that you are trying to read it by program
			# python urlopen is very programming to request html from the server. Thus, being caught. 
			# Then how do you make it leass programming? 
			#(1) add headers (google urlopen headers) then req (request object) and then change req...
		f.write(html)
	except:
		print("Downloading (2nd): ", link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		fld_link = get_fld('http://' +link)
		request_link = "https://" +link
		req = Request (url = request_link, headers = headers)
		f = open("domain_html/" + link, "wb")   # wb: writing and binary
		response = urlopen(req)
		html = response.read()
		f.write(html)
	f.close()
	# timesleep is less important here, cause it won't break the website, (??WHy?) but we will still do it.	
	time.sleep(10) # 10 secs are more than enough.


	"""
	notice that eveyrtime we start the program it starts from beginining. 
	However, we need to always check if the file exists or not in the program.
	If there exists the program already, we skip that, and it makes the program
	 much more robust and powerful. 

	 I am getting error!!!!!!!!!!!!!!!!11

	#

Original:  alerts.dailymotion.com
Traceback (most recent call last):
  File "scrape_many_domains.py", line 59, in <module>
    print(get_fld("fld version: " + 'http://' + link))
  File "C:\Users\jaeyouk\AppData\Local\Programs\Python\Python38-32\lib\site-packages\tld\utils.py", line 426, in get_fld
    domain_parts, non_zero_i, parsed_url = process_url(
  File "C:\Users\jaeyouk\AppData\Local\Programs\Python\Python38-32\lib\site-packages\tld\utils.py", line 326, in process_url
    raise TldBadUrl(url=url)
tld.exceptions.TldBadUrl: Is not a valid URL fld version: http://alerts.dailymotion.com!



	#


	"""


	