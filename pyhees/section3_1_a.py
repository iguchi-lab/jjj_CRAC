# ============================================================================
# 付録 A 熱交換型換気設備
# ============================================================================

from math import exp, ceil, floor


# ============================================================================
# A.2 熱交換型換気設備の補正温度交換効率
# ============================================================================

def calc_etr_dash_t(etr_t_raw, e, C_bal, C_leak):
    """ 熱交換型換気設備の補正熱交換効率 (-) (1)

    :param etr_t_raw: 熱交換型換気設備の温度交換効率 (-)
    :type etr_t_raw: float
    :param e: 有効換気量率 (-)
    :type e: float
    :param C_bal: 給気と排気の比率による温度交換効率の補正係数 (-)
    :type C_bal: float
    :param C_leak: 排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数 (-)
    :type C_leak: float
    :return: 熱交換型換気設備の補正熱交換効率 (-)
    :rtype: float
    """

    # 熱交換型換気設備の温度交換効率
    etr_t = get_etr_t(etr_t_raw)

    # カタログ表記誤差による温度交換効率の補正係数 (-)
    C_tol = get_C_tol()

    # 有効換気量率による温度交換効率の補正係数 (2)
    C_eff = get_C_eff(etr_t, e)

    # 熱交換型換気設備の補正熱交換効率 (-) (1)
    etr_dash_t = get_etr_dash_t(etr_t, C_tol, C_eff, C_bal, C_leak)

    return etr_dash_t


def get_etr_dash_t(etr_t, C_tol, C_eff, C_bal, C_leak):
    """ 熱交換型換気設備の補正熱交換効率 (-) (1)

    :param etr_t: 熱交換型換気設備の温度交換効率 (-)
    :type etr_t: float
    :param C_tol: カタログ表示誤差による温度交換効率の補正係数 (-)
    :type C_tol: float
    :param C_eff: 有効換気量率による温度交換効率の補正係数 (-)
    :type C_eff: float
    :param C_bal: 給気と排気の比率による温度交換効率の補正係数 (-)
    :type C_bal: float
    :param C_leak: 排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数 (-)
    :type C_leak: float
    :return: 熱交換型換気設備の補正熱交換効率 (-)
    :rtype: float
    """

    etr_dash_t = etr_t * C_tol * C_eff * C_bal * C_leak  # (1)
    return etr_dash_t


# ============================================================================
# A.3 熱交換型換気設備の温度交換効率
# ============================================================================

def get_etr_t(etr_t_raw):
    """ 熱交換型換気設備の温度交換効率

    :param etr_t_raw: 熱交換型換気設備の温度交換効率 (-)
    :type etr_t_raw: float
    :return: 熱交換型換気設備の温度交換効率
    :rtype: float
    """

    # 温度交換効率の値は、100 分の 1 未満の端数を切り下げた小数第二位までの値
    etr_t = ceil(etr_t_raw * 100) / 100
    if etr_t > 0.95:
        return 0.95
    else:
        return etr_t


# ============================================================================
# A.4 カタログ表記誤差による温度交換効率の補正係数
# ============================================================================

def get_C_tol():
    """ カタログ表記誤差による温度交換効率の補正係数

    :return: カタログ表記誤差による温度交換効率の補正係数
    :rtype: float
    """
    return 0.95


# ============================================================================
# A.5 有効換気量率による温度交換効率の補正係数
# ============================================================================

def get_C_eff(etr_t, e):
    """ 有効換気量率による温度交換効率の補正係数 (2)

    :param etr_t: 熱交換型換気設備の温度交換効率 (-)
    :type etr_t: float
    :param e: 有効換気量率
    :type e: float
    :return: 有効換気量率による温度交換効率の補正係数
    :rtype: float
    """

    C_eff = 1 - ((1 / e - 1) * (1 - etr_t) / etr_t)  # (2)

    #100 分の 1 未満の端数を切り下げた小数第二位までの値
    C_eff = floor(C_eff * 100) / 100
    if C_eff < 0.0:
        C_eff = 0.0

    return C_eff


# ============================================================================
# A.6 給気と排気の比率による温度交換効率の補正係数
# ============================================================================

C_bal_default = 0.90


def get_C_bal():
    """

    :return:
    :rtype:
    """
    return etr_t_d / etr_t_d  # (3)


def get_etr_t_d():
    """

    :return:
    :rtype:
    """
    # (4)
    if V_d_RA > V_d_SA:
        return etr_d
    elif V_d_RA <= V_d_SA:
        return etr_d * R_dash_vnt_d


def get_etr_d_ac():
    """

    :return:
    :rtype:
    """
    # (5a)
    return 1 - exp((exp(-pow(N_d, 0.78) * R_dash_vnt_d) - 1) / (pow(N_d, -0.22) * R_dash_vnt_d))


def get_etr_d_dc():
    """

    :return:
    :rtype:
    """
    return (1 - exp(-(1 - R_dash_vnt_d) * (
            1 + ((b / l) * sin(alpha) * cos(alpha) / (0.0457143 * N_d ** 2 + 0.0691429 * N_d + 0.9954286))) * N_d)) \
           / (1 - R_dash_vnt_d * exp(-(1 - R_dash_vnt_d) * (
            ((b / l) * sin(alpha) * cos(alpha)) / (0.00457143 * N_d ** 2 + 0.0691429 ** N_d + 0.9954286)) * N_d))
