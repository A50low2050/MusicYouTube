from pytube import YouTube
import io
from pydub import AudioSegment
from my_server import audio_server


def download_audio_not_file(link):
    yt = YouTube(link, use_oauth=False)
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

    buffer = io.BytesIO()
    audio_stream.stream_to_buffer(buffer)
    audio_data = AudioSegment.from_file(io.BytesIO(buffer.getvalue()), format="mp4")

    buffer.seek(0)
    buffer.write(audio_data.raw_data)
    return audio_data


links = ["https://www.youtube.com/watch?v=sWTaEc8Il6c", "https://www.youtube.com/watch?v=z7OWZar_JTU"]

d = download_audio_not_file(link=links[1])

audio_server(audio=d)

