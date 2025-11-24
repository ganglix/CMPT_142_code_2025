tempts = [[1,2,3], # Jan
          [4,5,6], # Feb
          [7,8,9]  # Mar
          ]

for i in range(len(tempts)):
    tempt_month = tempts[i]
    month_avg = sum(tempt_month)/len(tempts)

month_avg_list = []
for tempt_month in tempts:
    month_avg = sum(tempt_month)/len(tempts)
    month_avg_list.append(month_avg)

month_avg_list = [sum(tempt_month)/len(tempts) for tempt_month in tempts]

