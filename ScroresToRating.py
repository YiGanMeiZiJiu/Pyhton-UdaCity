def cocert_to_numeric(score):
    """将输入的数据转换成浮点数
    """
    covert_score = float(score)
    return covert_score
def avg_of_middle_three(score1,score2,score3,score4,score5):
    """求出五条数据中有效的中间三条数据的平均值
    """
    covert_score1 = cocert_to_numeric(score1)
    covert_score2 = cocert_to_numeric(score2)
    covert_score3 = cocert_to_numeric(score3)
    covert_score4 = cocert_to_numeric(score4)
    covert_score5 = cocert_to_numeric(score5)
    sum_five = covert_score1+covert_score2+covert_score3+covert_score4+covert_score5
    min_five = min(covert_score4,covert_score5,covert_score3,covert_score2,covert_score1)
    max_five = max(covert_score4,covert_score5,covert_score3,covert_score2,covert_score1)
    avg_middle_three = (sum_five - min_five - max_five)/3
    return avg_middle_three
def score_to_rating(score):
    """将对应的有效分值转换成对应的评价展现给客户
    """
    evaluate = None
    if 0 <= score <1:
        evaluate = "Terrible"
    elif 1 <= score <2:
        evaluate = "Bad"
    elif 2 <= score <3:
        evaluate = "OK"
    elif 3 <= score <4:
        evaluate = "Good"
    elif 4 <= score <5:
        evaluate = "Excellent"
    if evaluate:
        return evaluate


rating_string = score_to_rating(avg_of_middle_three(1, 2, 3, 4, 5))
#print(rating_string)

def top_three(parameter_list):
    """输入一个不规则列表
    要求输出这个列表的最大三个数
    """
    if(len(parameter_list)<=3):
        return parameter_list
    
    sorted_list = sorted(parameter_list,reverse=True)
    topthree = sorted_list[-3:]
    return topthree

def top_three1(input_list):
    return sorted(input_list, reverse=True)[:3]

print(top_three(['cat', 'dog', 'python', 'cuttlefish']))

print(4//2)
print(5//2)