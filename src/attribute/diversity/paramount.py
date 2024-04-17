import offer_dirs_collect
import parameters
import input_output_cont
import custom_process as custom
import batch_exec_shell as batch_e_s


def assign(media_pattern_type):
    elements_list = offer_dirs_collect.afford_element_list(media_pattern_type)
    input_output_cont.inject_to_file(elements_list, parameters.consequence_json_name)

    custom.custom_process(elements_list, media_pattern_type)
    batch_e_s.batch_execute(elements_list, media_pattern_type)
