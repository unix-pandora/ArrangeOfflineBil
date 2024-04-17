import os
import ergodic_individual as ergodic
import filter_file_type as filter_f_t
import parameters as param
import compare_sort
import perceive_json_cont as perceive_j_c
import stash_material as stash
import mobilization_json as mobilization
import forge_cmdline


def gain_cmd_by_code(media_type_code: str, filespath_tuple: tuple, new_filepath: str):
    res_cmd = ""
    if media_type_code == stash.roar_pattern:
        res_cmd = forge_cmdline.build_command_line(filespath_tuple, new_filepath)
    return res_cmd


def gain_transition_tuple(origin_foldername) -> tuple:
    transition_video_path = (
        origin_foldername
        + os.sep
        + str(param.trans_file_id)
        + "-"
        + stash.transition_video_name
    )
    transition_audio_path = (
        origin_foldername
        + os.sep
        + str(param.trans_file_id)
        + "-"
        + stash.transition_audio_name
    )
    return transition_video_path, transition_audio_path


def essential(media_type_code, individual_dir_path):
    identity_string = ""
    if media_type_code == stash.silence_pattern:
        identity_string = stash.silence_identity
    elif media_type_code == stash.roar_pattern:
        identity_string = stash.roar_identity

    ergodic_res_set = ergodic.gain_file_set(individual_dir_path)
    filter_list = filter_f_t.filter_elements(ergodic_res_set)
    sort_dict = compare_sort.compare_files(filter_list)

    json_outcome = perceive_j_c.gain_json_outcome(sort_dict[stash.minimum_video_info])
    new_filepath = mobilization.forge_new_filepath(json_outcome, identity_string)
    origin_foldername = os.path.dirname(sort_dict[stash.minimum_video_info])

    res_files_tuple = gain_transition_tuple(origin_foldername)

    sort_dict["origin_folder_name"] = origin_foldername
    sort_dict["new_file_path"] = new_filepath
    sort_dict["identity_str"] = identity_string
    sort_dict["transition_video_path"] = res_files_tuple[0]
    sort_dict["transition_audio_path"] = res_files_tuple[1]
    sort_dict["media_type_code"] = media_type_code

    cmdline_str = gain_cmd_by_code(media_type_code, res_files_tuple, new_filepath)
    sort_dict["cmd_line_str"] = cmdline_str

    return sort_dict
