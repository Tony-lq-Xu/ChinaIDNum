#根据生日和性别生成身份证号用于测试

def genIdNum(birthday, sex):
    
    #随机生成省份城市
    import csv

    codeList = []
    with open('DivisionCode.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            codeList.append(line[0])

    import random
    pickCode = codeList[random.randrange(len(codeList))] 

    #串联生日
    idNum = pickCode + birthday 

    #串联流水号
    seq = str(random.randrange(100))
    idNum = idNum + seq.zfill(2)


    #串联性别
    if sex == 'F':
        idNum = idNum + str(random.randrange(0,10,2))
    else:
        idNum = idNum + str(random.randrange(1,10,2))        

            
    #生成校验码
    e = 17
    sumchk = 0
    for i in range(17):
        sumchk = sumchk + (int(idNum[i]) * 2 ** e) % 11
        #print(i,":",(int(idNum[i]) * 2 ** e) % 11, "e=",e)
        e -= 1

    verCode = sumchk % 11

    #print("verCode:", verCode)

    verCode = 12 - verCode

    if verCode == 10:
        verCode = 'X'
    elif verCode == 11:
        verCode = '1'
    elif verCode == 12:
        verCode = '0'
    else:
        verCode = str(verCode)
    

    #生成最终18位编号

    return idNum + verCode   

if __name__ == '__main__':
    print(genIdNum('20120430','M'))
    print(genIdNum('20170705','F'))

