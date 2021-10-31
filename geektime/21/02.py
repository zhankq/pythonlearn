import concurrent.futures
import requests
import time

def download_one(url):
	resp = requests.get(url)
	print("Read {} from {}".format(len(resp.content),url))

def download_all(sites):
	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		to_do = []
		for site in sites:
			future = executor.submit(download_one,site)
			to_do.append(future)

		for future in concurrent.futures.as_completed(to_do):
			future.result()

def main():
	sites = [
	"https://www.163.com/dy/article/GLD41OTH0512D3VJ.html?clickfrom=w_yw",
	"https://www.163.com/news/article/GLD9JEBT00019K82.html?clickfrom=w_yw",
	"https://www.163.com/dy/article/GLCCKI8L0514R9OJ.html?clickfrom=w_yw",
	"https://baijiahao.baidu.com/s?id=1630405756682597112&wfr=spider&for=pc",
	"https://www.163.com/dy/article/GLCVLNID053469LG.html?clickfrom=w_lb_1_small_1"
	]
	start_time = time.perf_counter()
	download_all(sites)
	end_time = time.perf_counter()
	print("Download {} sites in {} seconds".format(len(sites),end_time-start_time))

main()