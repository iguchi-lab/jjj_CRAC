# ============================================================================
# 第十一章 その他
# 第一節 地域の区分と外気条件
# Ver.04（エネルギー消費性能計算プログラム（住宅版）Ver.02.00～）
# ============================================================================

import numpy as np
import pandas as pd
from numpy import exp, log
from functools import lru_cache


# ============================================================================
# 付録 A 外気相対湿度の計算方法
# ============================================================================

# ============================================================================
# A.2 外気相対湿度の計算方法
# ============================================================================

@lru_cache()
def load_outdoor():
    """気温[℃],絶湿[g/kg']

    :return: 気温[℃],絶湿[g/kg']
    :rtype: DateFrame
    """
    return pd.read_csv('data/outdoor.csv', skiprows=4, nrows=24 * 365, names=(
    'day', 'hour', 'holiday', 'Theta_ex_1', 'X_ex_1', 'Theta_ex_2', 'X_ex_2', 'Theta_ex_3', 'X_ex_3', 'Theta_ex_4',
    'X_ex_4', 'Theta_ex_5', 'X_ex_5', 'Theta_ex_6', 'X_ex_6', 'Theta_ex_7', 'X_ex_7', 'Theta_ex_8', 'X_ex_8'))

@lru_cache()
def load_climate(region):
    return pd.read_csv('data/climate/climateData_{}.csv'.format(region), nrows=24 * 365, encoding="SHIFT-JIS")

# 日射量
def get_J(climate):
    return climate["水平面天空日射量 [W/m2]"].values

def get_Theta_ex(region, df):
    """気温[℃]

    :param region: 省エネルギー地域区分
    :type region: int
    :param df: 気温[℃],絶湿[g/kg']
    :type df: DateFrame
    :return: 気温[℃]
    :rtype: ndarray
    """
    return df['Theta_ex_' + str(region)].values


def get_T_ex(Theta_ex):
    """外気絶対温度[K]

    :param Theta_ex: 気温[℃]
    :type Theta_ex: ndarray
    :return: 外気絶対温度[K]
    :rtype:  ndarray
    """
    return Theta_ex + 273.16


def get_X_ex(region, df):
    """絶湿[g/kg']

    :param region: 省エネルギー地域区分
    :type region: int
    :param df: 気温[℃],絶湿[g/kg']
    :type df: DateFrame
    :return: 絶湿[g/kg']
    :rtype: ndarray
    """
    return df['X_ex_' + str(region)].values


def calc_h_ex(X_ex, Theta_ex):
    """外気相対湿度 式（１）

    :param X_ex: 絶湿[g/kg']
    :type X_ex: ndarray
    :param Theta_ex: 外気絶対温度[K]
    :type Theta_ex: ndarray
    :return: 外気相対温度
    :rtype: ndarray
    """
    P_v = get_P_v(X_ex)
    P_vs = calc_P_vs(Theta_ex)
    return P_v / P_vs * 100


def get_P_v(X_ex):
    """外気の水蒸気圧　式（２）

    :param X_ex: 絶湿[g/kg']
    :type X_ex: ndarray
    :return: 外気の水蒸気圧
    :rtype:ndarray
    """
    return 101325 * (X_ex / (622 + X_ex))


def calc_P_vs(Theta_ex):
    """外気の飽和水蒸気圧　式（3a）

    :param Theta_ex: 外気絶対温度[K]
    :type Theta_ex: ndarray
    :return: 外気の飽和水蒸気圧
    :rtype: ndarray
    """
    k = get_k(Theta_ex)
    return exp(k)


def get_k(Theta_ex):
    """指数k 式(3b)

    :param Theta_ex: 外気絶対温度[K]
    :type Theta_ex: ndarray
    :return: 指数k
    :rtype: ndarray
    """
    T_ex = get_T_ex(Theta_ex)

    a1 = -6096.9385
    a2 = 21.2409642
    a3 = -0.02711193
    a4 = 0.00001673952
    a5 = 2.433502
    b1 = -6024.5282
    b2 = 29.32707
    b3 = 0.010613863
    b4 = -0.000013198825
    b5 = -0.49382577

    # Theta_ex > 0
    k_a = a1 / T_ex + a2 + a3 * T_ex + a4 * T_ex ** 2 + a5 * log(T_ex)

    # Theta_ex <= 0
    k_b = b1 / T_ex + b2 + b3 * T_ex + b4 * T_ex ** 2 + b5 * log(T_ex)

    return k_a * (Theta_ex > 0) + k_b * (Theta_ex <= 0)


# ============================================================================
# 付録 B 平均外気温度の計算方法
# ============================================================================

# ============================================================================
# B.2 年平均外気温度
# ============================================================================


def get_Theta_ex_a_Ave(Theta_ex_d_t):
    """年平均外気温度[℃] (1)

    :param Theta_ex_d_t: 外気絶対温度[K]
    :type Theta_ex_d_t: ndarray
    :return: 年平均外気温度[℃]
    :rtype: ndarray
    """
    return np.sum(Theta_ex_d_t) / 8760

# ============================================================================
# B.3 日平均外気温度
# ============================================================================


def get_Theta_ex_d_Ave_d(Theta_ex_d_t):
    """日付dにおける日平均外気温度[℃] (2)

    :param Theta_ex_d_t: 外気絶対温度[K]
    :type Theta_ex_d_t: ndarray
    :return: 日付dにおける日平均外気温度
    :rtype: ndarray
    """

    # 1次元配列を2次元配列に形状変換する
    Theta_ex_d_t = np.reshape(Theta_ex_d_t, (365, 24))

    # 時間軸を合計し、365日分の配列を返す
    return np.sum(Theta_ex_d_t, axis=1) / 24

# ============================================================================
# B.4 暖房期における期間平均外気温度
# ============================================================================


def get_Theta_ex_H_Ave(Theta_ex_d_t, L_H_x_t_i):
    """暖房期における期間平均外気温度[℃] (3a)

    :param Theta_ex_d_t: 外気絶対温度[K]
    :type Theta_ex_d_t: ndarray
    :param L_H_x_t_i: 暖冷房区画iの1時間当たりの暖房負荷
    :type L_H_x_t_i: ndarray
    :return: 暖房期における期間平均外気温度[℃]
    :rtype: ndarray
    """

    # 暖房負荷が発生する日付の集合[-]
    D = get_D(L_H_x_t_i)

    # 1次元配列を2次元配列に形状変換する
    Theta_ex_d_t = np.reshape(Theta_ex_d_t, (365, 24))

    # 時間軸合算
    Theta_ex_d = np.sum(Theta_ex_d_t, axis=1)

    # 暖房期以外の外気温度を0とする
    Theta_ex_d[D == False] = 0

    # 暖房期における期間平均外気温度[℃]
    Theta_ex_H_Ave = np.sum(Theta_ex_d) / (24 * np.count_nonzero(D))

    return Theta_ex_H_Ave


def get_D(L_H_x_t_i):
    """ 暖房負荷が発生する日付の集合[-] (3b)

    :param L_H_x_t_i: 暖冷房区画iの1時間当たりの暖房負荷
    :type L_H_x_t_i: ndarray
    :return: 暖房負荷が発生する日付の集合
    :rtype: ndarray
    """

    # L_H_x_t_iは暖冷房区画毎に365日×24時間分の負荷を持った2次元配列
    # 暖冷房区画軸合算(暖冷房区画の次元をなくす)
    L_H_x_t = np.sum(L_H_x_t_i, axis=0)

    # 1次元配列を2次元配列に形状変換する
    L_H_x_t = np.reshape(L_H_x_t, (365, 24))

    # 時間軸合算
    L_H_x = np.sum(L_H_x_t, axis=1)

    # 暖房日の判定（暖房負荷がある日はtrue、ない日はfalse）
    D = 0 < L_H_x

    # 暖房日の判定を行った365日分の配列を返す
    return D


if __name__ == '__main__':
    import numpy as np

    df = load_outdoor()

    for region in range(1, 9):
        # 外気温
        Theta_ex = get_Theta_ex(region, df)

        # 絶対湿度
        X_ex = get_X_ex(region, df)

        # 相対湿度
        h_ex = calc_h_ex(X_ex, Theta_ex)

        print('** 地域区分{0} **'.format(region))
        print('平均気温: {0} [K]'.format(np.average(Theta_ex)))
        print('平均絶対湿度: {0} [g/kg\']'.format(np.average(X_ex)))
        print('外気相対湿度: {0} [%]'.format(np.average(h_ex)))