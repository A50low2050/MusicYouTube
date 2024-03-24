from pytube import YouTube


def download_audio_from_video(link: str):
    try:
        yt = YouTube(link, use_oauth=False)
        stream = yt.streams.get_by_itag(251)
        stream.download()
    except Exception as ex:
        raise ex


link_test = "https://www.youtube.com/watch?v=OFquPzLWJ5Q"
download_audio_from_video(link_test)
