# 6 大部分がガラスで構成されている窓等の開口部

# 6.1 日射熱取得率

def get_eta_H_i(f_H_i, etr_d_i):
    """ 開口部の暖房期の日射熱取得率 (-) (3)

    :param f_H_i: 開口部の暖房期の取得日射熱補正係数 (-)
    :type f_H_i: float
    :param etr_d_i: 開口部の垂直面日射熱出得率((W/m2)/(W/m2))
    :type etr_d_i: float
    :return: 開口部の暖房期の日射熱取得率((W/m2)/(W/m2))
    :rtype: float
    """
    return f_H_i * etr_d_i


def get_eta_C_i(f_C_i, etr_d_i):
    """ 開口部の冷房期の日射熱取得率 (-) (4)

    :param f_C_i: 開口部の冷房期の取得日射熱補正係数 (-)
    :type f_C_i: float
    :param etr_d_i: 開口部の垂直面日射熱出得率 ((W/m2)/(W/m2))
    :type etr_d_i: float
    :return: 開口部の冷房期の日射熱取得率((W/m2)/(W/m2))
    :rtype:
    """
    return f_C_i * etr_d_i


# 6.2 垂直面日射熱取得率

def get_eta_d_i(etr_d1_i, etr_d2_i, r_f):
    """ 二重窓等の複数の開口部が組み合わさった開口部の垂直面日射熱取得率 (-) (5)

    :param etr_d1_i: 開口部の外気側の窓の垂直面日射熱取得率 (-)
    :type etr_d1_i: float
    :param  etr_d2_i: 開口部の室内側の窓の垂直面日射熱取得率 (-)
    :type etr_d2_i: float
    :param r_f: 開口部の全体の面積に対するガラス部分の面積の比 (-)
    :type r_f: float
    :return: 二重窓等の複数の開口部が組み合わさった開口部の垂直面日射熱取得率
    :rtype: float
    """
    return etr_d1_i * etr_d2_i * 1.06 / r_f


def get_r_f(frame_type):
    """ 開口部の全体の面積に対するガラス部分の面積の比 (-)

    :param frame_type: 枠の種類
    :type frame_type: str
    :return: 開口部の全体の面積に対するガラス部分の面積の比
    :rtype: float
    """
    if frame_type == '室内側の窓及び外気側の窓の両方の枠が木製建具又は樹脂製建具':
        return 0.72
    elif frame_type == 'それ以外':
        return 0.8
    else:
        raise ValueError(frame_type)