def population_density(population, land_area):
    return population/land_area

def printcase(excepted_result, actual_result):
    print("expected result: {}...,actual result: {}".format(excepted_result, actual_result))

BEIJING = population_density(10, 1)
EXPECTED_RESULT1 = 10
#print("expected result: {}...,actual result: {}".format(expected_result1,beijing))
#printcase(EXPECTED_RESULT1, BEIJING)

NANCHANG = population_density(86481, 120.4)
EXPECTED_RESULT2 = 7123
#print("expected result: {}...,actual result: {}".format(expected_result2,nanchang))
#printcase(EXPECTED_RESULT2, NANCHANG)

def readable_timedelta(days):
    """计算输入的天数有几个礼拜零几天
    """
    return "{} week(s) and {} day(s)".format(int(days/7), days%7)
string = readable_timedelta(10)
#print(string)
#print(int(4/2.1))

def which_price(points):
    if 0 <= points <=50:
        return "恭喜！你赢得了 [{}]!".format("wooden rabbit")
    elif 151 <= points <= 180:
        return "恭喜！你赢得了 [{}]!".format("water-thin mint")
    elif 181 <= points <= 200:
        return "恭喜！你赢得了 [{}]!".format("peguin")
    else:
        return "哦，亲爱的，这次没有奖品"
#print(which_price(201))

def which_price1(points):
    price = None
    if 0 <= points <= 50:
        price = "wooden rabbit"
    elif 151 <= points <=180:
        price = "water-thin mint"
    elif 181 <= points <= 200:
        price = "peguin"
    if price:
        return "恭喜！你赢得了 [{}]!".format(price)
    else:
        return "哦，亲爱的，这次没有奖品"
#print(which_price1(200))

def tag_list(input_list):
    """确定输入的字符串列表中
    有几个xml标签
    即判断字符串是否以<开始，>结束
    """
    temp = 0
    for string in input_list:
        if string.startswith('<',0,1):
            if string.startswith('>',len(string)-1,len(string)):
                temp += 1
    return temp

def tag_count(tokens):
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count

list1 = ['<greeting>', '<Hello World!', '</greeting>']
count = tag_list(list1)
count1 = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
print("Expected result: 2, Actual result: {}".format(count1))

capitalized_names = []
for number in range(6):
    capitalized_names.append(number)

# print(capitalized_names)
