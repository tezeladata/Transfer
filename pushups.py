# მონაცემების შეტანა
starting_list = []

def sort_users(name, weight, push_up_count):
    starting_list.append([name, weight, push_up_count])

sort_users("ლაშა ფილიშვილი", 24, 0)
sort_users("გიორგი კრავჩენკო", 26, 0)
sort_users("გიორგი უგრეხელიძე", 28, 0)
sort_users("ბარბარე წივილაშვილი", 29, 0)
sort_users("ლუკ ვეკუა", 30, 0)
sort_users("ლევან ჯაჯანიძე", 34, 0)
sort_users("მახმუდი მახმუდოღლი", 35, 0)
sort_users("თორნიკე ალუღიშვილი", 35, 0)
sort_users("გიორგი წურწუმია", 35, 0)
sort_users("ვაკო პაქსაძე", 38, 0)
sort_users("ზაზა კუჭავა", 40, 0)
sort_users("გაბრიელ ხელაია", 40, 0)
sort_users("გიორგი გერლიანი", 40, 0)
sort_users("დემეტრე გორგიაშვილი", 40, 0)
sort_users("ანდრია ჩიხლაძე", 44, 0)
sort_users("ალექსანდრე ნარიმანიშვილი", 46, 0)
sort_users("ვაჟა საბაური", 48, 0)
sort_users("დავით თედორაძე", 48, 0)
sort_users("ლუკა ციცვიძე", 48, 0)
sort_users("ანდრია გიკაშვილი", 48, 0)
sort_users("დემეტრე ელიაშვილი", 55, 0)
sort_users("ბექა აბულაძე", 57, 0)
sort_users("საბა მუმლაძე", 57, 0)
sort_users("გურამ თოფჩიშვილი", 57, 0)
sort_users("გიორგი ღვინაძე", 59, 0)
sort_users("ლუკა ლეკიშვილი", 59, 0)
sort_users("დავით შავიძე", 59, 0)
sort_users("ნიკოლოზ მელიქიძე", 60, 0)
sort_users("საბა ზარდიაშვილი", 60, 0)
sort_users("საბა ზვიადაური", 60, 0)
sort_users("შალვა ყოჩიშვილი", 61, 0)
sort_users("გიგა ხუციშვილი", 61, 0)
sort_users("თორნიკე ათუაშვილი", 61, 0)
sort_users("ტარიელ ბეჟანიშვილი", 62, 0)
sort_users("მირიან გორელაშვილი", 63, 0)
sort_users("დემეტრე ნიკოლაიშვილი", 64, 0)
sort_users("ნიკოლოზ ჯანეზაშვილი", 65, 0)
sort_users("გიორგი ხორბალაძე", 65, 0)
sort_users("მიშიკო თოთლაძე", 65, 0)
sort_users("გიორგი შავაძე", 65, 0)
sort_users("დათა თეზელაშვილი", 65, 0)
sort_users("ნიკოლოზ ყველაშვილი", 67, 0)
sort_users("საბა სამსონიძე", 68, 0)
sort_users("გიორგი სვანიძე", 70, 0)
sort_users("გიორგი ნაცარაშვილი", 70, 0)
sort_users("დათო ახალაშვილი", 72, 0)
sort_users("რომა ჩეკურაშვილი", 74, 0)
sort_users("ლუკა ლეფსვერიძე", 74, 0)
sort_users("საბა სომხიშვილი", 78, 0)
sort_users("რეზიკო დუმბაძე", 82, 0)
sort_users("თემური მჭედლიშვილი", 84, 0)
sort_users("ნიკოლოზ წულაია", 91, 0)
sort_users("თორნიკე ბეღელური", 95, 0)
sort_users("ლუკა ბეჟანიძე", 95, 0)
sort_users("ნიკოლოზ ლიჩელი", 100, 0)
sort_users("ნიკოლოზ ლომიძე", 110, 0)
# sort_users("", , 0)

# მახასიათებლის გამოთვლა
sorted_list = []
def sort_data(list): sorted_list.append([list[0], (list[2] * list[1] / 20)])

for i in range(len(starting_list)): sort_data(starting_list[i])

# სიის დასორტირება
sorted_list.sort(key=lambda x: x[1], reverse=True)

# dict-ის სახით დაბეჭვდა
user_dict = dict()
for list in sorted_list: user_dict[list[0]] = list[1]
print(user_dict)

# result