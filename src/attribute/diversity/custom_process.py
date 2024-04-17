import stash_material as stash
import modified_bin
import perceive_bin

def custom_process(elements_list:list,media_pattern_type):
    for item in elements_list:
        perceive_bin.get_bin_content(item['original_video'])
        if media_pattern_type == stash.silence_pattern:
            modified_bin.fix_m4s(item['original_video'],item['transition_video_path'])
        elif media_pattern_type == stash.roar_pattern:
            modified_bin.fix_m4s(item['original_video'],item['transition_video_path'])
            modified_bin.fix_m4s(item['original_audio'],item['transition_audio_path'])
        perceive_bin.get_bin_content(item['transition_video_path'])