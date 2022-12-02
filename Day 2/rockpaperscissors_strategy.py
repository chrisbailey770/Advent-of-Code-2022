with open('Input/input.txt','r') as f:
    data = f.readlines()
    
f.close()
    
score_dic_1 = {"A X\n": 4,
               "A Y\n": 8,
               "A Z\n": 3,
               "B X\n": 1,
               "B Y\n": 5,
               "B Z\n": 9,
               "C X\n": 7,
               "C Y\n": 2,
               "C Z\n": 6}

scores_1 = [score_dic_1[x] for x in data]
  
print(sum(scores_1))

score_dic_2 = {"A X\n": 3+0,
               "A Y\n": 1+3,
               "A Z\n": 2+6,
               "B X\n": 1+0,
               "B Y\n": 2+3,
               "B Z\n": 3+6,
               "C X\n": 2+0,
               "C Y\n": 3+3,
               "C Z\n": 1+6}

scores_2 = [score_dic_2[x] for x in data]

print(sum(scores_2))