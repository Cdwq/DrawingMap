import requests
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from lxml import  etree
import time

def  douban_photos_crawl_single(url, num=0):

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Host": "movie.douban.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    }
    res = requests.get(url, headers=headers, timeout=3)

    if res and res.status_code == 200 :

        img_url_list = []
        content = res.text
        #xpath取内容 将html解析成树
        # html = etree.HTML(content)
        # photos = html.xpath('/html/body/div[3]/div[1]/div/div[1]/ul/li[1]/div[1]/a')

        soup = BeautifulSoup(content, "html.parser")
        photos = soup.findAll('div', attrs={'class': 'cover'})
        for photo in photos:
            img_url = photo.find('img')['src']
            # print(img_url)
            img_url_list.append(img_url)
        return img_url_list
    else:
        print("访问网页失败")

def douban_photos_crawl():

    #max 1890
    count = 0
    for i in range(0, 30, 30):
        count += 1
        print('正在爬取第 %s 页'%count)
        url = 'https://movie.douban.com/celebrity/1319376/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(i)
        try:
            img_list = douban_photos_crawl_single(url)
            print(img_list)
            #写入耗时太多
            # douban_photos_download(count, img_list)
        except Exception as e:
            print("爬取/写入过程出错 " + e)

        print('第 %s 页爬取完成'%count)

def douban_photos_crawl_threadPool():

    #max 1890
    with ThreadPoolExecutor(max_workers=30) as pool:

        thread_events = []
        url_list = ['https://movie.douban.com/celebrity/1319376/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(i)
                    for i in range(0, 30, 30) ]
        num_list = [i for i in range(1, 11)]
        i, count = 0, 0
        for result in pool.map(douban_photos_crawl_single, url_list, num_list):

            count = num_list[i]
            print('正在爬取第 %s 页' % count)
            print(result)
            douban_photos_download(count, result)
            print('第 %s 页爬取完成' % num_list[i])
            i += 1
def douban_photos_download(pageNum, img_list):

    print("正在保存第 %s 页图片"%pageNum)
    if not os.path.exists(r'douban_pictures'):
        os.mkdir(r'douban_pictures')
    file_dir = 'douban_pictures\\%s'%pageNum
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)

    # for img in img_list:
    #     img_name = img.split('/')[-1]
    #     path = file_dir + '\\' + img_name
    #     douban_photos_download_single(img, path)
    with ThreadPoolExecutor(max_workers=30) as pool:
        for img in img_list:
            img_name = img.split('/')[-1]
            path = file_dir + '\\' + img_name
            pool.submit(lambda con : douban_photos_download_single(*con), (img, path))
    print("第 %s 页图片保存完成" % pageNum)

def douban_photos_download_single(url, path):

    pic_data = requests.get(url).content
    with open(path, 'wb') as f:
        f.write(pic_data)

if __name__ == '__main__' :

    start_time = time.time()
    # douban_photos_crawl()
    # print("串行耗时: %s 秒"%(time.time() - start_time)) #111
    douban_photos_crawl_threadPool()
    print("线程池耗时: %s 秒"%(time.time() - start_time)) #28
