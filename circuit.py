import dot_data
import setup
import time
inin = 0
#delay = 5  # 딜레이 시간
# 임시 회로 시뮬레이터
def play():
    for i in range(2):
        for j in range(6):
            if dot_data.dot[i][j] == 1:
                #print("1")
                setup.result_list += '1'
            elif dot_data.dot[i][j] == 0:
                #print("0")
                setup.result_list += '0'

    dot_data.reset()

#    time.sleep(delay)
    #print("")



