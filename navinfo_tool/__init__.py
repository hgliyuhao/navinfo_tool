from fairies.read import (
    read,
    read_json,
    read_txt,
    read_csv,
    read_npy
)

from fairies.write import (
    write_json,
    write_txt,
    write_npy
)

from fairies.classification_utils import (
    random_split_data,
    count_label,
    # split_data,
    # analysis_res
)

from fairies.nlp_utils import (
    label2id,
    is_chinese,
    find_lcs,
    long_substr,
    split_to_paragraph,
    split_to_sents,
    split_to_subsents,
    get_slide_window_text,
    get_cut_window_text
)

from fairies.nlp_jieba_utils import(
    jieba_init,
    jieba_add_words,
    jieba_cut,
    find_co_occurrence_word
)

from fairies.knowledge import(
    get_tongyin,
    get_tongxing,
    get_hanzi,
    get_stop_word
)

from fairies.nlp_clean_data import (
    removeLineFeed,
    cht_2_chs, # 繁体到简体
    chs_2_cht, # 简体到繁体
    strQ2B,
)


from navinfo_tool.rule_error_identification1009 import (

    error_identification
)
