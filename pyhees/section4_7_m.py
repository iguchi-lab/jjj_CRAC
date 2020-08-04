# ============================================================================
# 付録 M 放熱器の最大能力
# ============================================================================

import numpy as np

# ============================================================================
# M.2 放熱器の最大能力
# ============================================================================

def calc_q_max_rad(region, mode, A_HCZ, R_type):
    """ 放熱器の最大能力 (1)

    :param region: 省エネルギー地域区分
    :type region: int
    :param mode: 運転モード 'い', 'ろ', 'は'
    :type mode: str
    :param A_HCZ: 暖冷房区画の床面積
    :type A_HCZ: float
    :param R_type: 居室の形式
    :type R_type: string
    :return: 熱器の最大能力
    :rtype: ndarray
    """
    # 単位面積当たりの必要暖房能力
    q_rq_H = get_q_rq_H(region, R_type)

    # 外気温度補正係数
    f_cT = get_f_cT()

    # 間歇運転能力補正係数
    f_cI = get_f_cI(mode, R_type)

    return np.ones(24*365) * q_rq_H * A_HCZ * f_cT * f_cI


def get_q_rq_H(region, R_type):
    """ 単位面積当たりの必要暖房能力

    :param region: 省エネルギー地域区分
    :type region: int
    :param R_type: 居室の形式
    :type R_type: string
    :return: 単位面積当たりの必要暖房能力
    :rtype: float
    """
    if R_type == '主たる居室':
        return get_table_m_2()[0][region - 1]
    elif R_type == 'その他の居室':
        return get_table_m_2()[1][region - 1]
    else:
        raise ValueError(R_type)


def get_f_cT():
    """ 外気温度補正係数

    :return: 外気温度補正係数
    :rtype: float
    """

    return 1.05


def get_f_cI(mode, R_type):
    """ 間歇運転能力補正係数

    :param mode: 運転モード 'い', 'ろ', 'は'
    :type mode: str
    :param R_type: 居室の形式
    :type R_type: string
    :return: 間歇運転能力補正係数
    :rtype: float
    """
    if mode in ['連続運転', '連続', 'ろ']:
        y = 0
    elif mode in ['間歇運転','間歇','は']:
        y = 1
    else:
        raise ValueError(mode)

    if R_type == '主たる居室':
        return get_table_m_3()[y][0]
    elif R_type == 'その他の居室':
        return get_table_m_3()[y][1]
    else:
        raise ValueError(R_type)


def get_table_m_2():
    """ 表M.2 単位面積当たりの必要暖房能力

    :return: 表M.2 単位面積当たりの必要暖房能力
    :rtype: list
    """
    table_m_2 = [
        (139.26, 120.65, 111.32, 118.98, 126.56, 106.48, 112.91),
        (95.97, 82.03, 84.97, 86.55, 94.44, 80.58, 84.94)
    ]
    return table_m_2

def get_table_m_3():
    """ 表M.3 間歇運転能力補正係数

    :return: 表M.3 間歇運転能力補正係数
    :rtype: list
    """
    table_m_3 = [
        (1.0, 1.0),
        (3.034, 4.804)
    ]
    return table_m_3
