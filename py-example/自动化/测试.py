
from you_get import common
down_url = 'https://www.bilibili.com/video/BV184411x7F9?p=154'

downdir = r'F:\下载'
common.any_download_playlist(url=down_url, info_only=False, output_dir=downdir, merge=True)
