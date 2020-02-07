import math

names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']
for name in names:
    name = name.title()
    # names.append(name)
    # print(name)
# print(names)

def html_list(input_list):
    print("<ul>")
    for string in input_list:
        print(string)
    print("</ul>")

def nearest_square(num):
    """
    取最大平方数
    该函数取一个整数参数 num，并返回一个小于 num 的最大平方数。
    平方数是整数乘以自身的乘积，例如 6*6 等于 36，所以 36 是平方数。
    """
    while num>0:
        #   math.sqrt(limit)函数取一个数limit，并返回该值开方后的值(返回的值可以不为整数)
        if(math.sqrt(num-1)%1 == 0):
            return num-1
        num = num-1

def nearest__square(limit):
    """
    取最大平方数的另一种解法
    """
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2

test1 = nearest_square(2)
# print("expected result: 36, actual result: {}".format(test1))

# 大家现在使用 break 语句编写自己的循环。你们的任务是创建一个长度为 140 个字符的字符串 news_ticker。
# 可通过从 headlines 列表添加标题，在每个标题之间插入一个空格来创建新闻提醒。
# 如有必要，可以从中间截断最后一个标题，这样 news_ticker 的长度刚好就是 140 个字符。
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
lengh = 0
# for headline in headlines:
#     if (lengh + len(headline)) < 140:
#         news_ticker += headline
#         news_ticker += " "
#         lengh += len(headline)
#     else:
#         # print(140-len(news_ticker))
#         last_ticker = headline[0:(140-(len(news_ticker)))]
#         news_ticker += last_ticker
#         break
# print(news_ticker)
#另一种解法
for headline in headlines:
    news_ticker += headline+" "
    if len(news_ticker) > 140:
        news_ticker = news_ticker[:140]
        break
# print(news_ticker)

def check_answer(my_answer,answer):
    """
    Check the answer
    """
    if(my_answer == answer):
        return True
    else:
        return False
def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    count_correct = 0
    count_incorrect = 0
    for i in range(len(answers)):
        if(check_answer(my_answers[i],answers[i])):
            count_correct += 1
        else:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

# print(check_answers([1,2,3],[1,2,4]))

i = 200
my_set = set()
while i>0:
    i = nearest__square(i)
    my_set.add(i)
# print(my_set)

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(yearly_record):
    sum = 0
    for takings in monthly_takings:
        for i in monthly_takings[takings]:
            sum += i
    return sum
# print(total_takings(monthly_takings))
