# 付録A 一般部位及び大部分がガラスで構成されていないドア等の開口部における日除けの効果係数

def get_gamma_H_i_default():
    """ 暖房期の日除けの効果係数

    :return: 暖房期の日除けの効果係数
    :rtype: float
    """
    return 1.0


def get_gamma_C_i_default():
    """ 冷房期の日除けの効果係数

    :return: 冷房期の日除けの効果係数
    :rtype: float
    """
    return 1.0


def get_gamma(y1, y2, gamma1, gamma2):
    """ 一般部位及び大部分がガラスで構成されていないドア等の開口部における日除けの効果係数 (-)

    :param y1: 日除け下端から一般部及び大部分がガラスで構成されていないドア等の開口部の上端までの垂直方向距離 (mm)
    :type y1: float
    :param y2: 一般部及び大部分がガラスで構成されていないドア等の開口部の高さ寸法 (mm)
    :type y2: float
    :param gamma1: データ「日除けの効果係数」より算出した値
    :type gamma1: float
    :param gamma2: データ「日除けの効果係数」より算出した値
    :type gamma2: float
    :return: 一般部位及び大部分がガラスで構成されていないドア等の開口部における日除けの効果係数
    :rtype: float
    """
    gamma = (gamma2 * (y1 + y2) - gamma1 * y1) / y2
    return gamma


def get_l1(y1, z):
    """ l1 (2a)

    :param y1: 日除け下端から一般部及び大部分がガラスで構成されていないドア等の開口部の上端までの垂直方向距離 (mm)
    :type y1: float
    :param z: 壁面からの日除けの張り出し寸法（軒等の出寸法は壁表面から先端までの寸法とする）(mm)
    :type z: float
    :return: l1
    :rtype: float
    """
    l1 = y1 / z
    return l1


def get_l2(y1, y2, z):
    """ l2 (2b)

    :param y1: 日除け下端から一般部及び大部分がガラスで構成されていないドア等の開口部の上端までの垂直方向距離 (mm)
    :type y1: float
    :param y2: 一般部及び大部分がガラスで構成されていないドア等の開口部の高さ寸法 (mm)
    :type y2: float
    :param z: 壁面からの日除けの張り出し寸法（軒等の出寸法は壁表面から先端までの寸法とする）(mm)
    :type z: float
    :return: l2
    :rtype: float
    """
    return (y1 + y2) / z

