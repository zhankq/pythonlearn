import concurrent.futures
import requests
import threading
import time

def download_one(url):
	resp = requests.get(url)
	print('Read {} from {}'.format(len(resp.content),url))

def download_all(sites):
	for site in sites:
		download_one(site)

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

# if __name__=='__main__':
main()


import concurrent.futures
import requests
import threading
import time

def download_one2(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all2(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one2, sites)

def main2():
    sites = [
	"https://www.163.com/dy/article/GLD41OTH0512D3VJ.html?clickfrom=w_yw",
	"https://www.163.com/news/article/GLD9JEBT00019K82.html?clickfrom=w_yw",
	"https://www.163.com/dy/article/GLCCKI8L0514R9OJ.html?clickfrom=w_yw",
	"https://baijiahao.baidu.com/s?id=1630405756682597112&wfr=spider&for=pc",
	"https://www.163.com/dy/article/GLCVLNID053469LG.html?clickfrom=w_lb_1_small_1"
	]
    start_time = time.perf_counter()
    download_all2(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

main2()

