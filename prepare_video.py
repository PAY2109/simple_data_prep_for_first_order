
from moviepy.editor import *


class VideoProcessor():
    def process(self, video_filepath):
        video = VideoFileClip(video_filepath)

        height = video.h
        width = video.w

        if height > width:
            video = video.crop(x_center=width / 2, y_center=height / 2,
                               width=width, height=width)
        else:
            video = video.crop(x_center=width / 2, y_center=height / 2,
                               width=height, height=height)

        video = video.resize((256, 256))

        iterator = 1
        duration = video.duration
        start_time = 0
        while start_time < duration:
            if duration - start_time < 29:
                output_clip = video.subclip(t_start=start_time, t_end=duration)
                output_clip.write_videofile("output_video_" + str(iterator) + ".mp4", fps=25)
                audioclip = output_clip.audio
                audioclip.write_audiofile("output_audio_" + str(iterator) + ".mp3")
                break
            else:
                output_clip = video.subclip(t_start=start_time, t_end=start_time + 29)
                output_clip.write_videofile("output_video_" + str(iterator) + ".mp4", fps=25)
                audioclip = output_clip.audio
                audioclip.write_audiofile("output_audio_" + str(iterator) + ".mp3")
                iterator += 1
                start_time += 29

if __name__ == '__main__':
    video_filepath = 'input.mp4'
    videoProcessor = VideoProcessor()
    videoProcessor.process(video_filepath)