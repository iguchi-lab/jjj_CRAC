# ============================================================================
# 付録 A 設置する暖房設備機器又は放熱器の種類に応じた暖房方式及び運転方法の決定方法
#        並びに評価上想定される暖房設備機器又は放熱器の種類
# ============================================================================

# ============================================================================
# A.1 設置する暖房設備機器又は放熱器の種類に応じた暖房方式及び運転方法の決定方法
# ============================================================================


def calc_heating_mode(region, H_A=None, H_MR=None, H_OR=None):
    """ 暖房方式及び運転方法の区分を取得する

    :param region: 省エネルギー地域区分
    :type region: int
    :param H_A: 暖房方式
    :type H_A: dict
    :param H_MR: 主たる居室の暖房機器の仕様
    :type H_MR: dict
    :param H_OR: その他の居室の暖房機器の仕様
    :type H_OR: dict
    :return: 暖房方式及び運転方法の区分
    :rtype: tuple(str, str)
    """
    if H_A is None:

        if H_MR is None and H_OR is None:
            return None, None

        default_spec = get_default_heating_spec(region)

        if H_MR['type'] in ['設置しない', 'その他']:
            H_MR_type = default_spec[0]['type']
        else:
            H_MR_type = H_MR['type']

        if H_OR is not None:
            if H_OR['type'] in ['設置しない', 'その他']:
                H_OR_type = default_spec[1]['type']
            else:
                H_OR_type = H_OR['type']

        y = get_index_of_table_a_1(H_MR_type)

        def to_roha(s):
            if type(s) is tuple:
                return (to_roha(s[0]), to_roha(s[1]))
            else:
                if s == '連続':
                    return 'ろ'
                elif s == '間歇':
                    return 'は'
                else:
                    raise ValueError(s)

        if H_OR is not None:
            x = get_index_of_table_a_1(H_OR_type)
            return to_roha(get_table_a_1_a()[y][x])
        else:
            tmp = get_table_a_1_b()[y]
            if type(tmp) is tuple:
                if region in [1, 2]:
                    return to_roha(tmp[0]), None
                elif region in [3, 4, 5, 6, 7]:
                    return to_roha(tmp[1]), None
                else:
                    raise ValueError(region)
            else:
                return to_roha(tmp), None

    if H_A['type'] == 'ダクト式セントラル空調機':
        # 住宅全体を連続的に暖房する方式
        return 'い'

    else:
        raise ValueError(H_A['type'])


def get_index_of_table_a_1(type):
    """ 表A.1における行番号を取得する

    :param type: 主たる居室に設置する暖冷房設備機器等
    :type type: str
    :return: 表A.1における行番号
    :rtype: int
    """
    key_table = {
        '電気蓄熱暖房器': 0,
        '温水暖房用パネルラジエーター': 1,
        '温水暖房用床暖房': 2,
        '温水暖房用ファンコンベクター': 3,
        'ルームエアコンディショナー': 4,
        'FF暖房機': 5,
        '電気ヒーター床暖房': 6,
        'ルームエアコンディショナー付温水床暖房機': 7
    }
    return key_table[type]


def get_table_a_1_a():
    """ 表 A.1(a) 主たる居室及びその他の居室の運転方法(その他の居室がある場合)

    :return: 表 A.1(a) 主たる居室及びその他の居室の運転方法(その他の居室がある場合)
    :rtype: list
    """
    table_a_1_a = [
        # 電気蓄熱暖房器
        (
            ('連続', '連続'),
            ('連続', '連続'),
            ('連続', '連続'),
            ('連続', '間歇'),
            ('連続', '間歇'),
            ('連続', '間歇'),
            ('連続', '間歇'),
            ('連続', '間歇'),
        ),
        # パネルラジエータ―
        (
            ('連続', '連続'),
            ('連続', '連続'),
            ('連続', '連続'),
            ('連続', '間歇'),
            ('連続', '間歇'),
            ('連続', '間歇'),
            ('連続', '間歇'),
            ('連続', '間歇'),
        ),
        # 温水床暖房
        (
            ('連続', '連続'),
            ('連続', '連続'),
            ('連続', '連続'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
        ),
        # ファンコンベクター
        (
            ('間歇', '連続'),
            ('間歇', '連続'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
        ),
        # ルームエアコンディショナー
        (
            ('間歇', '連続'),
            ('間歇', '連続'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
        ),
        # FF暖房機
        (
            ('間歇', '連続'),
            ('間歇', '連続'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
        ),
        # 電気ヒーター床暖房
        (
            ('間歇', '連続'),
            ('間歇', '連続'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
        ),
        # ルームエアコンディショナー付温水床暖房
        (
            ('間歇', '連続'),
            ('間歇', '連続'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
            ('間歇', '間歇'),
        )
    ]
    return table_a_1_a


def get_table_a_1_b():
    """ 表 A.1(b) 主たる居室の運転方法(その他の居室がない場合)

    :return: 表 A.1(b) 主たる居室の運転方法(その他の居室がない場合)
    :rtype: list
    """
    table_a_1_b = [
        '連続',
        '連続',
        ('連続', '間歇'),
        '間歇',
        '間歇',
        '間歇',
        '間歇',
        '間歇',
    ]
    return table_a_1_b


def get_default_heating_spec(region):
    """ 暖房設備機器等が設置されない場合の評価上想定される暖房設備機器等の種(表A.3)を取得する

    :param region: 省エネルギー地域区分
    :type region: int
    :return: 暖房設備機器等が設置されない場合の評価上想定される暖房設備機器等の種
    :rtype: tuple(dict, dict, dict)
    """
    def to_spec(type):
        if type == '温水暖房用パネルラジエーター':
            return {
                'type': type
            }
        elif type == 'FF暖房機':
            return {
                'type': type,
                'e_rtd': 0.86
            }
        elif type == 'ルームエアコンディショナー':
            return {
                'type': type,
                'e_class': 'ろ',
                'dualcompressor': False
            }
        else:
            raise ValueError(type)

    if region != 8:
        type_list = get_table_a_5()[region - 1]

        if region in [1, 2]:
            hw_spec = {
                'type': '石油従来型温水暖房機',
                'e_rtd': 0.83
            }
            return to_spec(type_list[0]), to_spec(type_list[1]), hw_spec
        else:
            return to_spec(type_list[0]), to_spec(type_list[1]), None
    else:
        return None, None, None


def get_default_heatsource(region):
    """ 温水暖房用熱源機を設置しない場合又はその他の温水暖房機を設置する場合に想定する温水暖房用熱源機の仕様を取得する

    :param region: 省エネルギー地域区分
    :type region: int
    :return: 温水暖房用熱源機を設置しない場合又はその他の温水暖房機を設置する場合に想定する温水暖房用熱源機の仕様
    :rtype: dict
    """
    if region == 8:
        return None

    hs_type = get_table_a_6()[region - 1]

    e_rtd_table = {
        '石油従来型温水暖房機': 0.830,
        'ガス従来型温水暖房機': 0.825
    }
    e_rtd = e_rtd_table[hs_type]

    return {
        'type': hs_type,
        'e_rtd_hs': e_rtd,

        # 配管を設置しない場合においては、配管の断熱措置を「断熱被覆のないもの」として評価
        'pipe_insulation': False,
        'underfloor_pipe_insulation': False
    }


def get_table_a_5():
    """ 表 A.5 主たる居室若しくはその他の居室に暖房設備機器等を設置しない場合又は表 A.1 に掲げる 暖房設備機器等以外の暖房設備機器等を設置する場合の評価において想定する暖房設備機器等

    :return: 表 A.5 主たる居室若しくはその他の居室に暖房設備機器等を設置しない場合又は表 A.1 に掲げる 暖房設備機器等以外の暖房設備機器等を設置する場合の評価において想定する暖房設備機器等
    :rtype:
    """
    table_a_5 = [
        ('温水暖房用パネルラジエーター', '温水暖房用パネルラジエーター'),
        ('温水暖房用パネルラジエーター', '温水暖房用パネルラジエーター'),
        ('FF暖房機', 'FF暖房機'),
        ('FF暖房機', 'FF暖房機'),
        ('ルームエアコンディショナー', 'ルームエアコンディショナー'),
        ('ルームエアコンディショナー', 'ルームエアコンディショナー'),
        ('ルームエアコンディショナー', 'ルームエアコンディショナー'),
    ]
    return table_a_5


def get_table_a_6():
    """ 表 A.6 温水暖房用熱源機を設置しない又はその他の温水暖房用熱源機を設置する場合の評価において想定する温水暖房用熱源機

    :return: 表 A.6 温水暖房用熱源機を設置しない又はその他の温水暖房用熱源機を設置する場合の評価において想定する温水暖房用熱源機
    :rtype: list
    """
    table_a_6 = [
        '石油従来型温水暖房機',
        '石油従来型温水暖房機',
        '石油従来型温水暖房機',
        '石油従来型温水暖房機',
        'ガス従来型温水暖房機',
        'ガス従来型温水暖房機',
        'ガス従来型温水暖房機',
    ]
    return table_a_6

if __name__ == '__main__':
    # ダクト式セントラル
    print(calc_heating_mode(region=6, H_A_type='ダクト式セントラル空調機'))
    # 個別
    print(calc_heating_mode(region=6, H_MR_type='電気蓄熱暖房器', H_OR_type='パネルラジエータ―'))
    # その他居室なし
    print(calc_heating_mode(region=6, H_MR_type='FF暖房機'))
    print(get_default_heatsource(1))
    print(get_default_heatsource(6))
    print(get_default_heating_spec(region=2))
