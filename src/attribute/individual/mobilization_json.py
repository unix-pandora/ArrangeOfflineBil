import os
import stash_material as stash_m
import parameters as param

def forge_new_filepath(json_dict,identity_str)->str:
    avid = json_dict["aid"]
    title = json_dict["title"]
    page = json_dict["p"]

    print("\nforge_new_filepath:", avid, title, page)
    video_name = (
        str(avid) + "-" + str(title) + "-" + str(page) + "-" + str(identity_str) + ".mp4"
    )


    # 遍历列表进行替换
    for char in stash_m.replace_chars:
        video_name = video_name.replace(char, "")

    video_name = param.destination_directory + os.sep + video_name
    print("\nforge_new_filepath video name: ", str(video_name))

    return video_name
