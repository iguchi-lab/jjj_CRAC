# ============================================================================
# 付録 A 機器の性能を表す仕様の決定方法
# ============================================================================

# ============================================================================
# A.1 敷設面積
# ============================================================================

# 敷設面積 A_f
def get_A_f(A_HCZ, r_Af):
    """敷設面積
    
    :param A_HCZ: 暖冷房区画の床面積 (m2)
    :type A_HCZ: float
    :param r_Af: 床暖房パネルの敷設率
    :type r_Af: float
    :return: 敷設面積
    :rtype: float
    """
    return A_HCZ * r_Af  # (1)


# 床暖房パネルの敷設率 r_Af
def get_r_Af(A_f, A_HCZ):
    """[summary]
    
    :param A_f: 敷設面積
    :type A_f: float
    :param A_HCZ: 暖冷房区画の床面積 (m2)
    :type A_HCZ: float
    :return: 床暖房パネルの敷設率
    :rtype: float
    """
    return A_f / A_HCZ  # (2)


# ============================================================================
# A.2 上面放熱率
# ============================================================================

# def get_r_up():
#     r_up = 1.0 - H * (R_si + R_U) * R_U     #(3)
#     return (r_up * 100) / 100

# 2) 温度差係数U

# TODO

if __name__ == '__main__':
    A_HCZ = 120.08
    A_f = 0.8

    # 床暖房パネルの敷設率
    r_Af = get_r_Af(A_f, A_HCZ)

    # 敷設面積
    A_f = get_A_f(A_HCZ, r_Af)

    print('A_HCZ = {}'.format(A_HCZ))
    print('A_f = {}'.format(A_f))
    print('r_Af = {}'.format(r_Af))
    print('A_f = {}'.format(A_f))
