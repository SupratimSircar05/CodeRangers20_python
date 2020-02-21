import numpy as np
# path = "f_libraries_of_the_world.txt"
path = "e_so_many_books.txt"
with open(path, "r") as f:
    lines = [w.strip() for w in f.readlines()]
num_books, num_libraries, num_days = [int(x) for x in lines[0].split()]
books = [int(x) for x in lines[1].split()]
books2 = [int(x) for x in lines[1].split()]

signups = []
ships = []
books_avail_arr = []

for lib_info, x_info in zip(lines[2::2], lines[3::2]):
    _, signup, ship = [int(x) for x in lib_info.split()]
    books_avail = [int(x) for x in x_info.split()]
    signups.append(signup)
    ships.append(ship)
    books_avail_arr.append(books_avail)
print(sum(books))

books
signups
ships
books_avail_arr

pass
def library_scoring(idd, days_left=0):
    signup = signups[idd]
    ship = ships[idd]
    books_avail = books_avail_arr[idd]

    book_scores = [books2[bid] for bid in books_avail]
    book_scores = sorted(book_scores)[::-1]
    
    book_scores = book_scores[:min(len(book_scores), max(0, ship*(days_left - signup)))]    

    return -18.5*signup + sum(book_scores)/150
len(books_avail_arr[602])
day = 0
libs = []
libs_set = {}
while day < num_days:
    lib_scores = [(library_scoring(idx, num_days-day),idx) for idx in range(num_libraries) if idx not in libs_set]
    lib_scores = sorted(lib_scores)[::-1][0]
    next_lib = lib_scores[1]
    libs_set[next_lib] = "booked"
    libs.append(next_lib)
    
    counter = (num_days-day-signups[next_lib])*ships[next_lib]
    for bk in books_avail_arr[next_lib]:
        books2[bk] = 0
        counter -= 1
        if counter <= 0:
            print("b", end=" ")
            break
    
    day += signups[next_lib]
    print(day, int(lib_scores[0]), lib_scores[1], end=" | ")
order = libs
print(len(order))

with open("order.txt", "w") as f:
    f.write(str(len(order)))
    f.write("\n")
    f.write("\n".join([str(s) for s in order]))
scanned = set()

strr = []
def output(line):
    strr.append(str(line))

output(len(order))
for idd in order:
    book_list = []
    reorder = [idd for score,idd in sorted([[books[idd], idd] for idd in books_avail_arr[idd]])[::-1]]
    for book in reorder:
        if book not in scanned:
            book_list.append(book)
            scanned.add(book)
    output(str(idd) + " " + str(len(book_list)))
    output(" ".join([str(x) for x in book_list]))
with open(path+".out", "w") as f:
    f.write("\n".join(strr))
