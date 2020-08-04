# 7 大部分がガラスで構成されていないドア等の開口部

# 開口部の暖房期の日射熱取得率  ((W/m)/(W/m2)) (6)
def get_eta_H_i(gamma_H_i, U_i):
    """ 開口部の暖房期の日射熱取得率  ((W/m)/(W/m2)) (6)

    :param gamma_H_i: 開口部の暖房期の日除けの効果係数 (-)
    :type gamma_H_i: float
    :param U_i: 開口部の熱貫流率 (W/m2K)
    :type U_i: float
    :return: 開口部の暖房期の日射熱取得率
    :rtype: float
    """
    return 0.034 * gamma_H_i * U_i


# 開口部の冷房期の日射熱取得率  ((W/m)/(W/m2)) (6)
def get_eta_C_i(gamma_C_i, U_i):
    """ 開口部の冷房期の日射熱取得率  ((W/m)/(W/m2)) (7)

    :param gamma_C_i: 一般部位iの冷房期の日除けの効果係数
    :type gamma_C_i: float
    :param U_i: ：一般部位iの熱貫流率 （W/m2K）
    :type U_i: float
    :return: 開口部の冷房期の日射熱取得率
    :rtype: float
    """
    return 0.034 * gamma_C_i * U_i