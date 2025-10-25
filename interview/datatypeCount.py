def list_data(listt):
    dic = {}
    for i in listt:
        data_type=type(i).__name__
        dic[data_type]=dic.get(data_type,0)+1
    return dic
listt=[10,20,76.9,89.5,'saagu','nandy',True]
result=list_data(listt)
print(result)