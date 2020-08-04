# ============================================================================
# 暖房および冷房機器にダクト式セントラル空調機を用いた際の
# 暖房および冷房設計一次エネルギー量を求めるサンプルコード
# ============================================================================

import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

import numpy as np

from pyhees.section2_1_b import get_f_prim
from pyhees.section3_1 import get_Q
from pyhees.section3_2 import calc_r_env, get_Q_dash, get_eta_H, get_eta_C
from pyhees.section4_1 import calc_heating_load, calc_cooling_load, get_virtual_heating_devices,\
    calc_E_E_H_hs_A_d_t, calc_E_UT_H_d_t__modeA, calc_E_E_C_hs_d_t, calc_E_UT_C_d_t
from pyhees.section4_1_a import calc_heating_mode


def get_basic():
    """基本情報の設定

    :return: 住宅タイプ、住宅建て方、床面積、地域区分、年間日射地域区分
    """
    # 住宅タイプ
    type = '一般住宅'

    # 住宅建て方
    tatekata = '戸建住宅'

    # 床面積
    A_A = 120.08
    A_MR = 29.81
    A_OR = 51.34

    # 地域区分
    region = 6

    # 年間日射地域区分
    sol_region = None

    return type, tatekata, A_A, A_MR, A_OR, region, sol_region


def get_env():
    """外皮の設定

    :return: 外皮条件
    """
    ENV = {
        'method': '当該住宅の外皮面積の合計を用いて評価する',
        'A_env': 307.51,
        'A_A': 120.08,
        'U_A': 0.87,
        'eta_A_H': 4.3,
        'eta_A_C': 2.8
    }

    # 自然風の利用 主たる居室
    NV_MR = 0
    # 自然風の利用 その他居室
    NV_OR = 0

    # 蓄熱
    TS = False

    # 床下空間を経由して外気を導入する換気方式の利用
    r_A_ufvnt = None

    # 床下空間の断熱
    underfloor_insulation = None

    return ENV, NV_MR, NV_OR, TS, r_A_ufvnt, underfloor_insulation


def get_heating():
    """暖房の設定

    :return: 暖房方式、住戸全体の暖房条件、主たる居室の暖房機器、その他居室の暖房機器、温水暖房の種類
    """
    # 暖房方式
    mode_H = '住戸全体を連続的に暖房する方式'

    # 住戸全体を暖房する
    H_A = {
        'type': 'ダクト式セントラル空調機',
        'duct_insulation': '全てもしくは一部が断熱区画外である',
        'VAV': False,
        'general_ventilation': True,
        'EquipmentSpec': '入力しない'
    }

    # 主たる居室暖房機器
    H_MR = None

    # その他居室暖房機器
    H_OR = None

    # 温水暖房機の種類
    H_HS = None

    return mode_H, H_A, H_MR, H_OR, H_HS


def get_cooling():
    """冷房の設定

    :return: 冷房方式、住戸全体の冷房条件、主たる居室冷房条件、その他居室冷房条件
    """
    # 冷房方式
    mode_C = '住戸全体を連続的に冷房する方式'

    # 住戸全体を冷房する
    C_A = {
        'type': 'ダクト式セントラル空調機',
        'duct_insulation': '全てもしくは一部が断熱区画外である',
        'VAV': False,
        'general_ventilation': True,
        'EquipmentSpec': '入力しない'
    }

    # 主たる居室冷房機器
    C_MR = None

    # その他居室冷房機器
    C_OR = None

    return mode_C, C_A, C_MR, C_OR


def get_heatexchangeventilation():
    """熱交換型換気の設定

    :return: 熱交換型換気
    """
    # 熱交換型換気
    HEX = None

    return HEX


def get_solarheat():
    """太陽熱利用の設定

    :return: 太陽熱利用
    """
    # 太陽熱利用
    SHC = None

    return SHC


def calc():
    """暖房設計一次エネルギー消費量

    :return: 各パラメータの計算結果
    """

    # ---------- 計算条件の取得 ----------

    # 基本情報を取得
    type, tatekata, A_A, A_MR, A_OR, region, sol_region = get_basic()

    # 外皮条件を取得
    ENV, NV_MR, NV_OR, TS, r_A_ufvnt, underfloor_insulation = get_env()

    # 暖房条件の取得
    mode_H, H_A, H_MR, H_OR, H_HS = get_heating()

    # 冷房条件の取得
    mode_C, C_A, C_MR, C_OR = get_cooling()

    # 熱交換型換気の取得
    HEX = get_heatexchangeventilation()

    # 太陽熱利用の取得
    SHC = get_solarheat()

    # ---------- その他計算条件を取得 ----------

    # 床面積の合計に対する外皮の部位の面積の合計の比
    r_env = calc_r_env(
        method='当該住戸の外皮の部位の面積等を用いて外皮性能を評価する方法',
        A_env=ENV['A_env'],
        A_A=A_A
    )

    # 熱損失係数（換気による熱損失を含まない）
    Q_dash = get_Q_dash(ENV['U_A'], r_env)
    # 熱損失係数
    Q = get_Q(Q_dash)

    # 日射取得係数の取得
    mu_H = get_eta_H(ENV['eta_A_H'], r_env)
    mu_C = get_eta_C( ENV['eta_A_C'], r_env)

    # 実質的な暖房機器の仕様を取得
    spec_MR, spec_OR = get_virtual_heating_devices(region, H_MR, H_OR)

    # 暖房方式及び運転方法の区分
    mode_MR, mode_OR = calc_heating_mode(region=region, H_MR=spec_MR, H_OR=spec_OR)

    # ---------- 暖房負荷の取得 ----------

    # 暖房負荷の取得
    L_H_d_t_i, _ = calc_heating_load(region, sol_region, A_A, A_MR, A_OR, Q, mu_H, mu_C, NV_MR, NV_OR, TS, r_A_ufvnt,
                                     HEX, underfloor_insulation, mode_H, mode_C, spec_MR, spec_OR, mode_MR, mode_OR,
                                     SHC)

    # ---------- 冷房負荷の取得 ----------

    # 冷房負荷の取得
    L_CS_d_t_i, L_CL_d_t_i = calc_cooling_load(region, A_A, A_MR, A_OR, Q, mu_H, mu_C, NV_MR, NV_OR, r_A_ufvnt,
                                               underfloor_insulation, mode_C, mode_H, mode_MR, mode_OR, TS, HEX)

    # ---------- 計算開始 ----------

    # 暖房設備機器の消費電力量（kWh/h）
    E_E_H_d_t = calc_E_E_H_hs_A_d_t(A_A, A_MR, A_OR, ENV['A_env'], mu_H, mu_C, Q, H_A, L_H_d_t_i,
                                    L_CS_d_t_i, L_CL_d_t_i, region)

    # 冷房設備機器の消費電力量（kWh/h）
    E_E_C_d_t = calc_E_E_C_hs_d_t(region, A_A, A_MR, A_OR, ENV['A_env'], mu_H, mu_C, Q, C_A, C_MR, C_OR,
                                  L_H_d_t_i, L_CS_d_t_i, L_CL_d_t_i)

    # 暖房設備の未処理暖房負荷の設計一次エネルギー消費量相当値（MJ/h）
    E_UT_H_d_t = calc_E_UT_H_d_t__modeA(H_A, A_A, A_MR, A_OR, ENV['A_env'], mu_H, mu_C, Q, region,
                                        L_H_d_t_i, L_CS_d_t_i, L_CL_d_t_i)

    # 冷房設備の未処理暖房負荷の設計一次エネルギー消費量相当値（MJ/h）
    E_UT_C_d_t = calc_E_UT_C_d_t(region, A_A, A_MR, A_OR, ENV['A_env'], mu_H, mu_C, Q, C_A, C_MR, C_OR,
                                 L_H_d_t_i, L_CS_d_t_i, L_CL_d_t_i, mode_C)

    # 電気の量 1kWh を熱量に換算する係数
    f_prim = get_f_prim()

    # 1 時間当たりの暖房設備の設計一次エネルギー消費量（MJ/h）
    E_H_d_t = E_E_H_d_t * f_prim / 1000 + E_UT_H_d_t

    # 1 時間当たりの冷房設備の設計一次エネルギー消費量（MJ/h）
    E_C_d_t = E_E_C_d_t * f_prim / 1000 + E_UT_C_d_t

    # 1 年当たりの暖房設備の設計一次エネルギー消費量（MJ/年）
    E_H = np.sum(E_H_d_t)

    # 1 年当たりの冷房設備の設計一次エネルギー消費量（MJ/年）
    E_C = np.sum(E_C_d_t)

    print({'E_H': E_H, 'E_C': E_C})


calc()