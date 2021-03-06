# 付録C 大部分がガラスで構成される窓等の開口部の垂直面日射熱取得率
# ―ガラスの日射熱取得率等を用いる場合―


#
def get_etr_d_i(etr_g_i, frame_type):
    """ 開口部の垂直面日射熱取得率 (-) (1a, 1b, 1c)

    :param etr_g_i: 開口部のガラスの垂直面日射熱取得率 (-)
    :type etr_g_i: float
    :param frame_type: 枠の種類
    :type frame_type: str
    :return: 開口部の垂直面日射熱取得率 (-)
    :rtype: float
    """
    if frame_type == '木製建具又は樹脂製建具':
        etr_d_i = etr_g_i * 0.72
    elif frame_type == '木と金属の複合材料製建具、樹脂と金属の複合材料製建具、金属製熱遮断構造建具又は金属製建具':
        etr_d_i = etr_g_i * 0.8
    elif frame_type == '影響がない':
        etr_d_i = etr_g_i
    return etr_d_i


def get_etr_g(glass_type, attachment):
    """ ガラスの垂直面日射熱取得率 (-)

    :param glass_type: ガラスの仕様
    :type glass_type: str
    :param attachment: 付属部材
    :type attachment: str
    :return: ガラスの垂直面日射熱取得率 (-)
    :rtype: float
    """
    # 表1 ガラスの垂直面日射熱取得率
    table_1 = {
        '2枚以上のガラス表面にLow-E膜を使用したLow-E三層複層ガラス(日射取得型)': (0.54, 0.34, 0.12),
        '2枚以上のガラス表面にLow-E膜を使用したLow-E三層複層ガラス(日射遮蔽型)': (0.33, 0.22, 0.08),
        'Low-E三層複層ガラス(日射取得型)': (0.59, 0.37, 0.14),
        'Low-E三層複層ガラス(日射遮蔽型)': (0.37, 0.25, 0.10),
        '三層複層ガラス': (0.72, 0.38, 0.18),
        'Low-E二層複層ガラス(日射取得型)': (0.64, 0.38, 0.15),
        'Low-E二層複層ガラス(日射遮蔽型)': (0.40, 0.26, 0.11),
        '二層複層ガラス': (0.79, 0.38, 0.17),
        '単板ガラス2枚を組み合わせたもの': (0.79, 0.38, 0.17),
        '単板ガラス': (0.88, 0.38, 0.19)
    }
    i = {'付属部材なし': 0, '和障子': 1, '外付けブラインド': 2}[attachment]
    return table_1[glass_type][i]


def get_etr_d_win_wood_or_resin(glass_type, attachment):
    """ 大部分がガラスで構成される窓等の開口部（一重構造の建具）の垂直面日射熱取得率

    :param glass_type: ガラスの仕様
    :type glass_type: str
    :param attachment: 付属部材
    :type attachment: str
    :return: 大部分がガラスで構成される窓等の開口部（一重構造の建具）の垂直面日射熱取得率
    :rtype: float
    """
    table_2_a = {
        '2枚以上のガラス表面にLow-E膜を使用したLow-E三層複層ガラス(日射取得型)': (0.39, 0.24, 0.09),
        '2枚以上のガラス表面にLow-E膜を使用したLow-E三層複層ガラス(日射遮蔽型)': (0.24, 0.16, 0.06),
        'Low-E三層複層ガラス(日射取得型)': (0.42, 0.27, 0.10),
        'Low-E三層複層ガラス(日射遮蔽型)': (0.27, 0.18, 0.07),
        '三層複層ガラス': (0.52, 0.27, 0.13),
        'Low-E二層複層ガラス(日射取得型)': (0.46, 0.27, 0.11),
        'Low-E二層複層ガラス(日射遮蔽型)': (0.29, 0.19, 0.08),
        '二層複層ガラス': (0.57, 0.27, 0.12),
        '単板ガラス2枚を組み合わせたもの': (0.57, 0.27, 0.12),
        '単板ガラス': (0.63, 0.27, 0.14)
    }
    i = {'付属部材なし': 0, '和障子': 1, '外付けブラインド': 2}[attachment]
    return table_2_a[glass_type][i]


def get_etr_d_win_composite(glass_type, attachment):
    """ 大部分がガラスで構成される窓等の開口部（一重構造の建具）の垂直面日射熱取得率

    :param glass_type: ガラスの仕様
    :type glass_type: str
    :param attachment: 付属部材
    :type attachment: str
    :return: 大部分がガラスで構成される窓等の開口部（一重構造の建具）の垂直面日射熱取得率
    :rtype:
    """
    table_2_b = {
        '2枚以上のガラス表面にLow-E膜を使用したLow-E三層複層ガラス(日射取得型)': (0.43, 0.27, 0.10),
        '2枚以上のガラス表面にLow-E膜を使用したLow-E三層複層ガラス(日射遮蔽型)': (0.26, 0.18, 0.06),
        'Low-E三層複層ガラス(日射取得型)': (0.47, 0.30, 0.11),
        'Low-E三層複層ガラス(日射遮蔽型)': (0.30, 0.20, 0.08),
        '三層複層ガラス': (0.58, 0.30, 0.14),
        'Low-E二層複層ガラス(日射取得型)': (0.51, 0.30, 0.12),
        'Low-E二層複層ガラス(日射遮蔽型)': (0.32, 0.21, 0.09),
        '二層複層ガラス': (0.63, 0.30, 0.14),
        '単板ガラス2枚を組み合わせたもの': (0.63, 0.30, 0.14),
        '単板ガラス': (0.70, 0.30, 0.15)
    }
    i = {'付属部材なし': 0, '和障子': 1, '外付けブラインド': 2}[attachment]
    return table_2_b[glass_type][i]
