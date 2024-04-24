def list_sort(input_list:list):
    result_lists = []
    current_list = []

    for i in range(len(input_list) - 1):
        if abs(input_list[i + 1] - input_list[i]) > 100:
            result_lists.append(current_list)
            current_list = []
        current_list.append(input_list[i+1])

    # Add the last element and remaining sublist to the result
    current_list.append(input_list[-1])
    result_lists.append(current_list)

    return result_lists

def sort_array_by_list_sort(original_array):
    # 提取x[1]并进行排序
    sorted_x1 = sorted([item[1] for item in original_array])

    # 使用list_sort函数对sorted_x1进行排序
    sorted_x1_lists = list_sort(sorted_x1)

    # 重新构建排序后的完整二维数组
    sorted_array = []
    for sublist in sorted_x1_lists:
        sublist_array = []
        for item in original_array:
            if item[1] in sublist:
                sublist_array.append(item)
        sorted_array.append(sublist_array)

    return sorted_array

# 原始数组
original_array = [
      [801.29169, 170.43208, 841.58997, 215.03908, 0.89620, 0.00000]  ,
      [756.28979, 171.28120, 795.55811, 216.38710, 0.89018, 0.00000]  ,
      [710.68939, 171.54546, 750.74609, 216.12062, 0.90124, 0.00000]  ,
      [663.77625, 172.12682, 702.96069, 217.86403, 0.87918, 0.00000]  ,
      [620.27570, 172.72990, 658.80060, 217.41296, 0.91900, 1.00000]  ,
      [576.65924, 173.73964, 611.99060, 215.74776, 0.90768, 1.00000]  ,
      [310.43884, 176.00462, 349.29608, 221.26962, 0.87145, 0.00000]  ,
      [531.87689, 176.67242, 568.12146, 218.48024, 0.87905, 0.00000]  ,
      [488.82712, 176.78693, 522.17480, 218.88524, 0.87852, 0.00000]  ,
      [400.19843, 176.80963, 435.75522, 217.37492, 0.88058, 1.00000]  ,
      [357.51108, 176.88486, 394.38266, 220.70660, 0.89490, 0.00000]  ,
      [444.30295, 177.29688, 480.34155, 220.31790, 0.89974, 0.00000]  ,
      [358.80313, 179.13431, 390.14749, 218.88422, 0.65738, 1.00000]  ,
      [757.27698, 518.07532, 797.15729, 565.65594, 0.92173, 0.00000]  ,
      [666.70508, 518.58997, 704.43408, 562.38281, 0.90885, 1.00000]  ,
      [713.24365, 518.69421, 751.56775, 564.14087, 0.92330, 1.00000]  ,
      [623.72729, 519.73132, 659.50513, 562.56506, 0.90366, 1.00000]  ,
      [490.12036, 519.82770, 524.57910, 561.25629, 0.89738, 1.00000]  ,
      [446.10776, 519.94421, 483.08813, 563.16095, 0.90687, 0.00000]  ,
      [402.81671, 520.25348, 438.93149, 563.23462, 0.91032, 0.00000]  ,
      [535.17004, 520.55615, 570.03711, 562.71814, 0.90918, 1.00000]  ,
      [359.21768, 520.96283, 396.68268, 563.13611, 0.89142, 0.00000]  ,
      [314.38608, 521.44952, 351.73108, 563.39899, 0.90173, 0.00000]  ,
      [803.20215, 522.21350, 841.31470, 566.22577, 0.90819, 0.00000]  ,
      [579.77728, 523.68268, 612.83301, 560.53943, 0.89778, 1.00000]
]
a = sort_array_by_list_sort(original_array)
for i in a:
    print(i)