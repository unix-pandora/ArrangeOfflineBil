import os

def build_command_line(media_tuple: tuple, output_path:str):
    video_name = media_tuple[0]
    audio_name = media_tuple[1]
    print(
        "\nbuild_command_line-video_name: ",
        video_name,
        "\nbuild_command_line-audio_name: ",
        audio_name,
    )

    #ffmpeg -i /PATH/TO/audio.mp4 -i /PATH/TO/video.mp4 -acodec copy -vcodec copy /PATH/TO/output.mp4
    command_line = [
        "ffmpeg -i ",
        str(video_name),
        " -i ",
        str(audio_name),
        " -acodec copy -vcodec copy ",
        output_path,        
    ]

    command_line = "".join(command_line)
    print("\nbuild_commmand_line: ", command_line)

    return command_line
    