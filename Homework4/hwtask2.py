

def function_key(**kwargs):
    dct_res = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:  #проверка на хешируемость
            value = str(value)
        dct_res[value] = key

    return dct_res



if __name__ == '__main__':
    res=function_key(arg1="Hello",arg2=2,arg3="123",arg4=[1,2,3,4,5],arg5=('hi','my','friends'),arg6={1,2,3,4,5,6})
    print(res)
