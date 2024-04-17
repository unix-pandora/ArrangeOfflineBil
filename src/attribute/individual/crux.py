import forge_new_obj as forge_n_o


def crux_reception(media_type_code, individual_dir_path: str):
    res_dict = forge_n_o.essential(media_type_code, individual_dir_path)

    print("crux_reception:", res_dict)
    return res_dict
