import youtube_dl
from youtube_dl.utils import DownloadError


ydl = youtube_dl.YoutubeDL()


def get_info(url):
    with ydl:
        try:
            result = ydl.extract_info(
                url,
                download=False
            )
        except DownloadError:
            return None
        
    if "entries" in result:
        video = result["entries"][0]
    else:
        video = result
        
    infos = ['id', 'title', 'channel', 'view_count', 'like_count',
             'channel_id', 'duration', 'categories', 'tags']
    
    def key_name(key):
        if key == "id":
            return "video_id"
        return key
    
    return {key_name(key): video[key] for key in infos}