# ============================================================================
# 付録B 温度差係数
# ============================================================================


def get_H(adjacent_type, region=None):
    """ 温度差係数

    :param adjacent_type: 隣接空間の種類
    :type adjacent_type: str
    :param region: 省エネルギー地域区分
    :type region: int
    :return: 温度差係数 (-)
    :rtype: float
    """


    if adjacent_type == '外気・外気に通じる空間':
        return get_table_1()[0]
    elif adjacent_type == '外気に通じていない空間・外気に通じる床裏':
        return get_table_1()[1]
    elif adjacent_type == '住戸及び住戸と同様の熱的環境の空間・外気に通じていない床裏':
        if region in [1, 2, 3]:
            return get_table_1()[2]
        elif region in [4, 5, 6, 7, 8]:
            return get_table_1()[3]
        else:
            raise ValueError(region)
    else:
        raise ValueError(adjacent_type)


def get_table_1():
    """ 表1 温度差係数

    :return: 表1 温度差係数
    :rtype: list
    """
    # 表1 温度差係数
    table_1 = (1.0, 0.7, 0.05, 0.15)

    return table_1