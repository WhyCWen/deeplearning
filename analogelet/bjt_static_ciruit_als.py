"""
 三级管电路静态电路分析与计算
 假设三极管处于放大状态来计算 Uceq 的静态电压是否大于
 Uces  ce 端的饱和电压,Uces 默认等于 0.3V
 Ubeq = 0.7V

"""
# Ec = 15
# beta = 100  # 三级管的静态默认放大倍数的系数  # 基电极电阻
# Re = 1.8 * 10 ** 3  # 发射极电阻
# Ibq = 1
Ubeq = 0.7  # 静态硅材料管的导通电压
Uces = 0.3  # 饱和状态 CE 端的电压


## Eb = Ibq * Rb + Ubeq + (1 + beta) * Re*Ibq  # Eb 于Ibq的通用计算公式
# Eb = Ec-(1+beta)*Rc          # 根据不同电路情况计算确定的 Eb值

def get_Eb(eba=None):
    if eba is None:
        return Ec - (1 + beta) * Rc
    else:
        return eba


def get_Rb(rba=None,d_p=None,data=None):
    """
    添加一些常用的 Rb 的电路组成
    :param data:
    :param d_p: 默认戴维林等效电路 标记符,
    :param rba:
    :return:
    """
    rba_temp=0
    if rba is None and d_p is None:
        return 100 * 1e3
    else:
        if d_p is not None and data is not None:
            # 戴维林等效电路求解 Rb
            if d_p == "d_p":
                rba_temp = (data[0]*data[1])/(data[1]*data[0])
            else:
                rba_temp = sum(data)
            if rba is None:
                rba_temp += rba
        else:
            if rba is not None:
                rba_temp = rba
    return rba_temp


def get_Rc(rca=None):
    if rca is None:
        return 0
    else:
        return rca


def get_Re(rea=None):
    if rea is None:
        return 0
    else:
        return rea


def get_beta(b=None):
    if b is None:
        return 100
    else:
        return b


Ec = 12
# Rb = get_Rb(rba=101 * 1e3)
Rc = get_Rc(rca=500)
Re = get_Re(rea=200)
beta = get_beta(b=567)
# Rb = get_Rb(200*1e3)
Rb = get_Rb((100 * 200 / (100 + 200)) * 1e3)
Eb = get_Eb(eba=8)

def analysis_Uceq(ee=0):
    """
    :param ee: 发射极的电位位
    :return:
    """
    ### 三端电流 Ibq, Ieq,Icq 计算
    # 当 Ec 位负电压的时候
    Ibq = (abs(abs(ee) - abs(Eb)) - Ubeq) / (Rb + (1 + beta) * Re)
    Ieq = (1 + beta) * Ibq
    Icq = beta * Ibq

    ### 三端对地 电位计算 Ueq, Ucq,Ubq

    Ueq = Re * Ieq
    Ucq = abs(Ec) - Rc * Icq
    Uceq = Ucq - Ueq

    print("基极 b 静态电流   Ibq =", Ibq * 1e6, "uA")
    print("发射极 e 静态电流 Ieq =", Ieq * 1e3, "mA")
    print("集电极 c 静态电流 Icq =", Icq * 1e3, "mA")
    print("基极与发射极之间的电压 Uceq =", Uceq, "V")
    if Uceq > Uces:
        print("假设成功该电路处于放大状态,Uceq > Uces = 0.3")
    else:
        print("假设失败该电路处于饱和状态,Uceq < Uces <0.3")


analysis_Uceq(ee=12)
