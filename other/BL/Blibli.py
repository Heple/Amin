import threading
from datetime import datetime

import requests
import json
import re
import time
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
def download_audio(old_video_url, audio_url):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    headers.update({"Referer": old_video_url})
    all_thread=0
    audio_content = requests.get(audio_url, headers=headers)
    print()
    audio__file_size = int(audio_content.headers['content-length']) - 1
    print('音频大小：', str(audio__file_size / 1024 / 1024) + 'MB')
    starttime = datetime.now().replace(microsecond=0)
    size = 5242880
    if audio__file_size > size:
        all_thread = int(audio__file_size / size)
        if all_thread > 10:
            all_thread = 10
    part = audio__file_size // all_thread
    print(part)
    print(audio__file_size)
    threads = []
    for i in range(all_thread):
        start = part * i
        if i == all_thread - 1:
            end = audio__file_size
        else:
            end = start + part
        if i > 0:
            start += 1
        t = threading.Thread(target=Handler, name='uth-' + str(i),
                             kwargs={'start': start, 'end': end, 'ul': video_url, 'headers': headers,'filename':'audio.mp4'})
        t.setDaemon(True)
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    endtime = datetime.now().replace(microsecond=0)
    print('用时：%s' % (endtime - starttime))

def download_video(old_video_url, video_url):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    headers.update({"Referer": old_video_url})
    all_thread=0
    video_content = requests.get(video_url, headers=headers)
    video_file_size=int(video_content.headers['content-length'])-1
    starttime = datetime.now().replace(microsecond=0)
    size = 5242880
    if video_file_size > size:
        all_thread = int(video_file_size / size)
        if all_thread > 10:
            all_thread = 10
    part = video_file_size // all_thread
    print(part)
    print(video_file_size)
    threads = []
    print('视频大小：', str(video_file_size/ 1024 / 1024)+'MB')
    for i in range(all_thread):
        start = part * i
        if i == all_thread - 1:
            end = video_file_size
        else:
            end = start + part
        if i > 0:
            start += 1
        t = threading.Thread(target=Handler, name='vth-' + str(i),
                             kwargs={'start': start, 'end': end, 'ul': video_url,'headers': headers,'filename':'void.mp4'})
        t.setDaemon(True)
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    endtime = datetime.now().replace(microsecond=0)
    print('用时：%s' % (endtime - starttime))


def Handler(start, end, headers,ul,filename):
    headers['Range'] = "bytes=%s-%s" % (start,end)
    r = requests.get(url=ul, headers=headers, stream=True)
    downsize = 0
    with open(filename, 'ab+') as fp:
        fp.seek(start)
        for chunk in r.iter_content(204800):
            if chunk:
                fp.write(chunk)
                downsize += len(chunk)

if __name__ == '__main__':
    print('视屏链接：')
    url = input().strip()
    res = requests.get(url, headers=headers)
    playinfo  = json.loads(re.search(r'__playinfo__=(.*?)</script><script>', res.text).group(1))
    #initial_state = json.loads(re.search(r'__INITIAL_STATE__=(.*?);\(function\(\)', res.text).group(1))
    video_url = playinfo['data']['dash']['video'][0]['baseUrl']
    audio_url = playinfo['data']['dash']['audio'][0]['baseUrl']
    #video_name = initial_state['videoData']['title']
    #print('视频名字为：',video_name)
    print('视频地址为：', video_url)
    print('音频地址为：', audio_url)
    download_video(url, video_url)
    download_audio(url,audio_url)
