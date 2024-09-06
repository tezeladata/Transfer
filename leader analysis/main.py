import json
import math

with open("wages.json") as json_file:
    data = json.load(json_file)
start_info = [[i["Name"], {"speed count sum": i["Speed 1 Count"] + i["Speed 2 Count"] * 2 + i["Speed 3 Count"] * 3, "Wage": i["Wage"]}, [i["Speed 1 Count"], i["Speed 2 Count"], i["Speed 3 Count"]]] for i in data]

with open("wages2.json") as json_file2:
    data2 = json.load(json_file2)
second_info = [[i["Name"], {"speed count sum": i["Speed 1 count"] + i["Speed 2 count"] * 2 + i["Speed 3 count"] * 3, "Wage": i["Wage"]}, [i["Speed 1 count"], i["Speed 2 count"], i["Speed 3 count"]]] for i in data2]


'''
speed count dependant renewing of wages

<10 , wage = 6.75
10:15 , wage = 7
16:20, wage = 7.25
21:25, wage = 7.5
25:30, wage = 7.75
30:35 , wage = 8 
35:40, wage = 8.25
40:45, wage = 8.5
45:50, wage = 8.75
50 + = giga chad leader , wage = 9
'''

def generate_wages(matrix):
    fin_info = []
    total_sum = 0
    for i in matrix:
        leader, speed_count, speeds = [i[0], {"Old wage": i[1]["Wage"], "Speeds": i[2]}], i[1]["speed count sum"], i[2]

        # 7 good one
        # 6.75 best one

        if speed_count <= 10: wage_per_speed = 6.75
        elif speed_count <= 15: wage_per_speed = 7
        elif speed_count <= 20: wage_per_speed = 7.25
        elif speed_count <= 25: wage_per_speed = 7.5
        elif speed_count <= 30: wage_per_speed = 7.75
        elif speed_count <= 35: wage_per_speed = 8
        elif speed_count <= 40: wage_per_speed = 8.25
        elif speed_count <= 45: wage_per_speed = 8.5
        elif speed_count <= 50: wage_per_speed = 8.75
        else: wage_per_speed = 9

        new_wage = math.ceil(speeds[0]*wage_per_speed + speeds[1]*wage_per_speed*2 + speeds[2]*wage_per_speed*2.66)
        wage_diff = new_wage - leader[1]["Old wage"]
        total_sum += wage_diff
        leader[1]["New wage"], leader[1]["Wage increase"] = new_wage, wage_diff

        fin_info.append(leader)
    
    return fin_info

wage_before_formula = sum([i[1]["Wage"] for i in start_info])
wage_one = generate_wages(start_info)
wage_increase_after_formula = sum([i[1]["Wage increase"] for i in wage_one])
wage_two = generate_wages(second_info)
month_two_wage_increase = sum([i[1]["Wage increase"] for i in wage_two])
month_two_basic_wage = sum(i[1]["Wage"] for i in second_info)
# print(f"Wages sum before we use formula is: {wage_before_formula} \nWages sum after we use formula is {wage_before_formula + wage_increase_after_formula} percent increase is {100 - (wage_before_formula / (wage_before_formula + wage_increase_after_formula) * 100)} \nWages sum after second month is {wage_before_formula + wage_increase_after_formula + month_two_wage_increase} percent increase is {100 - ((wage_before_formula + wage_increase_after_formula) / (wage_before_formula + wage_increase_after_formula + month_two_wage_increase) * 100)} \nMonth two wages sum without our formula is {month_two_basic_wage}")
# print(f"Wages sum before we use formula is: {wage_before_formula} \nWages sum after we use formula is {wage_before_formula + wage_increase_after_formula} \nWages sum after second month is {wage_before_formula + wage_increase_after_formula + month_two_wage_increase} \nMonth two wages sum without our formula is {month_two_basic_wage}")

# renewed = []
# for member in wage_one:
#     name = member[0]
#     wage = member[1]["New wage"]
#     count = sum(member[1]["Speeds"])

#     for member_again in wage_two:
#         if member_again[0] == name:
#             if member_again[1]["New wage"] != wage:
#                 renewed.append([name, {"speeds increase": sum(member_again[1]["Speeds"]) - count, "wage increase": member_again[1]["New wage"] - wage, "old wage": wage, "new wage":  member_again[1]["New wage"]}])

# print(renewed)
# res
[['Daniel Abramiani', {'speeds increase': 7, 'wage increase': 150, 'old wage': 432, 'new wage': 582}], 
['Data Pophkadze', {'speeds increase': 7, 'wage increase': 176, 'old wage': 259, 'new wage': 435}], 
['Giorgi gvritishvili', {'speeds increase': 5, 'wage increase': 96, 'old wage': 77, 'new wage': 173}], 
['Gobron tsitlauri', {'speeds increase': 6, 'wage increase': 123, 'old wage': 68, 'new wage': 191}], 
['Guram papunashvili', {'speeds increase': 6, 'wage increase': 120, 'old wage': 501, 'new wage': 621}], 
['Luka Gurgenidze', {'speeds increase': 4, 'wage increase': 104, 'old wage': 349, 'new wage': 453}], 
['Nikoloz Tchitadze', {'speeds increase': 4, 'wage increase': 76, 'old wage': 45, 'new wage': 121}], 
['Ucha Khuberishvili', {'speeds increase': 10, 'wage increase': 172, 'old wage': 45, 'new wage': 217}], 
['Zuka Abashidze', {'speeds increase': 6, 'wage increase': 128, 'old wage': 337, 'new wage': 465}]]

# def display(matrix):
#     for i in sorted(matrix, reverse=True, key=lambda x: x[1]["New wage"]):
#         print(i)

# display(wage_one)
# print("\n\n")
# display(wage_two)


# for distribution
# def count_sums(matrix):
#     res = []
#     for i in matrix: res.append([i[0], {"speed count":  i[1]["speed count sum"]}])

#     return sorted(res, key=lambda x: x[1]["speed count"], reverse=True)

# dist = count_sums(res)
# for i in dist:
#     print(i)




# month one
['Davit Grdzelishvili', {'Old wage': 790, 'Speeds': [14, 39, 5], 'New wage': 948, 'Wage increase': 158}]
['Guram vakhtangashvili', {'Old wage': 575, 'Speeds': [6, 26, 7], 'New wage': 690, 'Wage increase': 115}]
['Guram papunashvili', {'Old wage': 417.5, 'Speeds': [9, 18, 4], 'New wage': 501, 'Wage increase': 83.5}]
['Vano Motiashvili', {'Old wage': 387.5, 'Speeds': [5, 18, 4], 'New wage': 465, 'Wage increase': 77.5}]
['Daniel Abramiani', {'Old wage': 370, 'Speeds': [6, 19, 2], 'New wage': 432, 'Wage increase': 62}]
['Giorgi Vanishvili', {'Old wage': 345, 'Speeds': [4, 17, 3], 'New wage': 403, 'Wage increase': 58}]
['Davit Narimanidze', {'Old wage': 312.5, 'Speeds': [3, 14, 4], 'New wage': 354, 'Wage increase': 41.5}]
['Luka Gurgenidze', {'Old wage': 307.5, 'Speeds': [3, 11, 6], 'New wage': 349, 'Wage increase': 41.5}]
['Levani Samsonidze', {'Old wage': 305, 'Speeds': [6, 12, 4], 'New wage': 346, 'Wage increase': 41}]
['Zuka Abashidze', {'Old wage': 297.5, 'Speeds': [11, 9, 4], 'New wage': 337, 'Wage increase': 39.5}]
['Sandro Zabakhidze', {'Old wage': 287.5, 'Speeds': [1, 12, 5], 'New wage': 316, 'Wage increase': 28.5}]
['shalva shubitidze', {'Old wage': 262.5, 'Speeds': [5, 11, 3], 'New wage': 289, 'Wage increase': 26.5}]
['Mate Giorgelashvili', {'Old wage': 255, 'Speeds': [2, 8, 6], 'New wage': 281, 'Wage increase': 26}]
['Data Pophkadze', {'Old wage': 242.5, 'Speeds': [3, 8, 5], 'New wage': 259, 'Wage increase': 16.5}]
['Giorgi Shavadze', {'Old wage': 235, 'Speeds': [8, 9, 2], 'New wage': 251, 'Wage increase': 16}]
['Mate Dolidze', {'Old wage': 225, 'Speeds': [8, 7, 3], 'New wage': 240, 'Wage increase': 15}]
['nikoloz yvavadze', {'Old wage': 212.5, 'Speeds': [3, 6, 5], 'New wage': 220, 'Wage increase': 7.5}]
['Erekle Kilasonia', {'Old wage': 195, 'Speeds': [4, 11, 0], 'New wage': 202, 'Wage increase': 7}]
['ilia dzindzibadze', {'Old wage': 175, 'Speeds': [0, 9, 2], 'New wage': 175, 'Wage increase': 0}]
['Atuka Khuskivadze', {'Old wage': 165, 'Speeds': [4, 5, 3], 'New wage': 165, 'Wage increase': 0}]
['Giorgi Motsonelidze', {'Old wage': 165, 'Speeds': [4, 5, 3], 'New wage': 165, 'Wage increase': 0}]
['Tsotne Gujabidze', {'Old wage': 162.5, 'Speeds': [5, 7, 1], 'New wage': 163, 'Wage increase': 0.5}]
['Luka Navrozashvili', {'Old wage': 155, 'Speeds': [2, 8, 1], 'New wage': 155, 'Wage increase': 0}]
['Saba isakadze', {'Old wage': 152.5, 'Speeds': [5, 5, 2], 'New wage': 153, 'Wage increase': 0.5}]
['Shotiko nukradze', {'Old wage': 140, 'Speeds': [2, 7, 1], 'New wage': 136, 'Wage increase': -4}]
['Luka Akofiani', {'Old wage': 117.5, 'Speeds': [3, 5, 1], 'New wage': 114, 'Wage increase': -3.5}]
['Nikoloz Nutsubidze', {'Old wage': 117.5, 'Speeds': [3, 5, 1], 'New wage': 114, 'Wage increase': -3.5}]
['Nikoloz Filishvili', {'Old wage': 112.5, 'Speeds': [1, 7, 0], 'New wage': 105, 'Wage increase': -7.5}]
['Aleksandre Melikjaniani', {'Old wage': 102.5, 'Speeds': [1, 5, 1], 'New wage': 96, 'Wage increase': -6.5}]
['Nika Kvaracxelia', {'Old wage': 95, 'Speeds': [4, 3, 1], 'New wage': 89, 'Wage increase': -6}]
['Giorgi Varadashvili', {'Old wage': 92.5, 'Speeds': [1, 3, 2], 'New wage': 87, 'Wage increase': -5.5}]
['Giorgi gvritishvili', {'Old wage': 82.5, 'Speeds': [5, 3, 0], 'New wage': 77, 'Wage increase': -5.5}]
['Andria Svanidze', {'Old wage': 80, 'Speeds': [0, 4, 1], 'New wage': 75, 'Wage increase': -5}]
['Giorgi Varazashvili', {'Old wage': 75, 'Speeds': [4, 3, 0], 'New wage': 68, 'Wage increase': -7}]
['Gobron tsitlauri', {'Old wage': 75, 'Speeds': [8, 1, 0], 'New wage': 68, 'Wage increase': -7}]
['Nikoloz Qimeridze', {'Old wage': 75, 'Speeds': [2, 4, 0], 'New wage': 68, 'Wage increase': -7}]
['Berdia Bekauri', {'Old wage': 72.5, 'Speeds': [5, 1, 1], 'New wage': 66, 'Wage increase': -6.5}]
['Sandro Jalagonia', {'Old wage': 65, 'Speeds': [2, 2, 1], 'New wage': 59, 'Wage increase': -6}]
['Aleko Tirkia', {'Old wage': 52.5, 'Speeds': [1, 3, 0], 'New wage': 48, 'Wage increase': -4.5}]
['Nikoloz Tchitadze', {'Old wage': 50, 'Speeds': [0, 2, 1], 'New wage': 45, 'Wage increase': -5}]
['Ucha Khuberishvili', {'Old wage': 50, 'Speeds': [0, 2, 1], 'New wage': 45, 'Wage increase': -5}]
['Giorgi Khmaladze', {'Old wage': 37.5, 'Speeds': [1, 2, 0], 'New wage': 34, 'Wage increase': -3.5}]


# month two
['Davit Grdzelishvili', {'Old wage': 790, 'Speeds': [14, 39, 5], 'New wage': 948, 'Wage increase': 158}]
['Guram vakhtangashvili', {'Old wage': 575, 'Speeds': [6, 26, 7], 'New wage': 690, 'Wage increase': 115}]
['Guram papunashvili', {'Old wage': 517.5, 'Speeds': [9, 22, 6], 'New wage': 621, 'Wage increase': 103.5}]
['Daniel Abramiani', {'Old wage': 485, 'Speeds': [6, 24, 4], 'New wage': 582, 'Wage increase': 97}]
['Vano Motiashvili', {'Old wage': 387.5, 'Speeds': [5, 18, 4], 'New wage': 465, 'Wage increase': 77.5}]
['Zuka Abashidze', {'Old wage': 387.5, 'Speeds': [11, 15, 4], 'New wage': 465, 'Wage increase': 77.5}]
['Luka Gurgenidze', {'Old wage': 377.5, 'Speeds': [3, 13, 8], 'New wage': 453, 'Wage increase': 75.5}]
['Data Pophkadze', {'Old wage': 362.5, 'Speeds': [3, 12, 8], 'New wage': 435, 'Wage increase': 72.5}]
['Giorgi Vanishvili', {'Old wage': 345, 'Speeds': [4, 17, 3], 'New wage': 403, 'Wage increase': 58}]
['Davit Narimanidze', {'Old wage': 312.5, 'Speeds': [3, 14, 4], 'New wage': 354, 'Wage increase': 41.5}]
['Levani Samsonidze', {'Old wage': 305, 'Speeds': [6, 12, 4], 'New wage': 346, 'Wage increase': 41}]
['Sandro Zabakhidze', {'Old wage': 287.5, 'Speeds': [1, 12, 5], 'New wage': 316, 'Wage increase': 28.5}]
['Shalva Shubitidze', {'Old wage': 262.5, 'Speeds': [5, 11, 3], 'New wage': 289, 'Wage increase': 26.5}]
['Mate Giorgelashvili', {'Old wage': 255, 'Speeds': [2, 8, 6], 'New wage': 281, 'Wage increase': 26}]
['giorgi shavaze', {'Old wage': 235, 'Speeds': [8, 9, 2], 'New wage': 251, 'Wage increase': 16}]
['Mate Dolidze', {'Old wage': 225, 'Speeds': [8, 7, 3], 'New wage': 240, 'Wage increase': 15}]
['nikoloz yvavadze', {'Old wage': 212.5, 'Speeds': [3, 6, 5], 'New wage': 220, 'Wage increase': 7.5}]
['Ucha Khuberishvili', {'Old wage': 210, 'Speeds': [0, 10, 3], 'New wage': 217, 'Wage increase': 7}]
['Erekle Kilasonia', {'Old wage': 195, 'Speeds': [4, 11, 0], 'New wage': 202, 'Wage increase': 7}]
['Gobron tsitlauri', {'Old wage': 185, 'Speeds': [8, 3, 4], 'New wage': 191, 'Wage increase': 6}]
['ilia dzindzibadze', {'Old wage': 175, 'Speeds': [0, 9, 2], 'New wage': 175, 'Wage increase': 0}]
['Giorgi gvritishvili', {'Old wage': 172.5, 'Speeds': [5, 5, 3], 'New wage': 173, 'Wage increase': 0.5}]
['Atuka Khuskivadze', {'Old wage': 165, 'Speeds': [4, 5, 3], 'New wage': 165, 'Wage increase': 0}]
['Giorgi Motsonelidze', {'Old wage': 165, 'Speeds': [4, 5, 3], 'New wage': 165, 'Wage increase': 0}]
['Tsotne Gujabidze', {'Old wage': 162.5, 'Speeds': [5, 7, 1], 'New wage': 163, 'Wage increase': 0.5}]
['Luka Navrozashvili', {'Old wage': 155, 'Speeds': [2, 8, 1], 'New wage': 155, 'Wage increase': 0}]
['Saba isakadze', {'Old wage': 152.5, 'Speeds': [5, 5, 2], 'New wage': 153, 'Wage increase': 0.5}]
['Shotiko nukradze', {'Old wage': 140, 'Speeds': [2, 7, 1], 'New wage': 136, 'Wage increase': -4}]
['Nikoloz Tchitadze', {'Old wage': 125, 'Speeds': [0, 3, 4], 'New wage': 121, 'Wage increase': -4}]
['Luka Akofiani', {'Old wage': 117.5, 'Speeds': [3, 5, 1], 'New wage': 114, 'Wage increase': -3.5}]
['Nikoloz Nutsubidze', {'Old wage': 117.5, 'Speeds': [3, 5, 1], 'New wage': 114, 'Wage increase': -3.5}]
['Nikoloz Filishvili', {'Old wage': 112.5, 'Speeds': [1, 7, 0], 'New wage': 105, 'Wage increase': -7.5}]
['Aleksandre Melikjaniani', {'Old wage': 102.5, 'Speeds': [1, 5, 1], 'New wage': 96, 'Wage increase': -6.5}]
['Nika Kvaratcxelia', {'Old wage': 95, 'Speeds': [4, 3, 1], 'New wage': 89, 'Wage increase': -6}]
['Giorgi Varadashvili', {'Old wage': 92.5, 'Speeds': [1, 3, 2], 'New wage': 87, 'Wage increase': -5.5}]
['Andria Svanidze', {'Old wage': 80, 'Speeds': [0, 4, 1], 'New wage': 75, 'Wage increase': -5}]
['Giorgi Varazashvili', {'Old wage': 75, 'Speeds': [4, 3, 0], 'New wage': 68, 'Wage increase': -7}]
['Nikoloz Qimeridze', {'Old wage': 75, 'Speeds': [2, 4, 0], 'New wage': 68, 'Wage increase': -7}]
['Berdia Bekauri', {'Old wage': 72.5, 'Speeds': [5, 1, 1], 'New wage': 66, 'Wage increase': -6.5}]
['Sandro Jalagonia', {'Old wage': 65, 'Speeds': [2, 2, 1], 'New wage': 59, 'Wage increase': -6}]
['Aleko Tirkia', {'Old wage': 52.5, 'Speeds': [1, 3, 0], 'New wage': 48, 'Wage increase': -4.5}]
['Giorgi Khmaladze', {'Old wage': 37.5, 'Speeds': [1, 2, 0], 'New wage': 34, 'Wage increase': -3.5}]