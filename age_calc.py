import time

def calc(birth, life_expectancy):
    # Year Month Day, Hour Minute Second
    ts_birth = time.mktime(time.strptime("{}-{}-{} {}:{}:{}".format(*birth), "%Y-%m-%d %H:%M:%S"))
    # MilliSecond
    ts_birth += birth[-1] / 1000
    # Distance
    ts_dis = time.time() - ts_birth
    # Leap Year Cut Down
    for i in range(birth[0], int(time.strftime("%Y", time.localtime()))):
        if not i % 4:
            ts_dis -= 24 * 60 * 60
    age = ts_dis / (365 * 24 * 60 * 60)
    percentage = age / life_expectancy * 100
    # Remaining Calc
    time_remaining = (life_expectancy - age) * 60 * 60 * 24 * 365
    # Leap Year Cut Down
    for i in range(BIRTH[0] + int(age), BIRTH[0] + int(life_expectancy)):
        if not i % 4:
            time_remaining += 60 * 60 * 24
    # More Remaining Calc
    day_remaining = int(time_remaining / (24 * 60 * 60))
    week_remaining = int(time_remaining / (24 * 60 * 60 * 7))
    month_remaining = int(time_remaining / (24 * 60 * 60 * 30))

    return (age, percentage, day_remaining, week_remaining, month_remaining)

if __name__ == "__main__":
    
    BIRTH = (2005, 3, 16, 9, 0, 0, 0) # 生日，年 月 日 时 分 秒 毫秒
    LIFE_EXPECTANCY = 24 # 预期寿命，岁

    while True:
        data = calc(BIRTH, LIFE_EXPECTANCY)
        print("您已：{}岁                                    \r".format(data[0]), end="")
        time.sleep(1)
        print("生命剩下 {}月/{}周/{}日                        \r".format(data[-1], data[-2], data[-3]), end="")
        time.sleep(1)
        print("现已度过{}%                                    \r".format(data[1]), end="")
        time.sleep(1)