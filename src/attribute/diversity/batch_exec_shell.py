import stash_material as stash
import execute_cmdline as execute_c

def batch_execute(elements_list,media_pattern_type):
    if media_pattern_type == stash.silence_pattern:
        print('not_need_for_sound')
    elif media_pattern_type == stash.roar_pattern:
        for item in elements_list:
            execute_c.execute(item['cmd_line_str'])