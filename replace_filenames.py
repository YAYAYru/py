import os

# --- parameter
filename_replace = ["40", "02"]
path = '../imagevideo/'
# ---

filename_list = os.listdir(path)

print("filename_list: ", filename_list)

split_filenames = [name.split(".")[0].split("_") for name in filename_list]

jj = 0
ii = 0
# def find_and_replace()
# обязательно [:] для списка
filename_list1 = filename_list[:]
for s_f in split_filenames:
    # Найти номер не желаемый номер ориентации одноручного жеста и заменить
    if len(s_f) == 3 and s_f[0][4:] == filename_replace[0]:
        ii = ii + 1
        print("Find filename_replace[0] and replace", ii)
        print("s_f[0]-: ", s_f[0])
        s_f[0] = s_f[0][0:4] + filename_replace[1]
        print("s_f[0]+: ", s_f[0])
        filename_list1[jj] = s_f[0] + "_" + s_f[1] + "_" + s_f[2] + "." + filename_list[jj].split(".")[1]

    # Найти номер не желаемый номер ориентации двуручного жеста и заменить
    if len(s_f) == 4 and s_f[0][4:] == filename_replace[0]:
        ii = ii + 1
        print("Find filename_replace[0] and replace", ii)
        print("s_f[0]--: ", s_f[1])
        s_f[0] = s_f[0][0:4] + filename_replace[1]
        print("s_f[0]++: ", s_f[0])
        filename_list1[jj] = f"{s_f[0]}_{s_f[1]}_{s_f[2]}_{s_f[3]}.{filename_list[jj].split('.')[1]}"

    if len(s_f) == 4 and s_f[1][4:] == filename_replace[0]:
        ii = ii + 1
        print("Find filename_replace[0] and replace", ii)
        print("s_f[0]--: ", s_f[1])
        s_f[1] = s_f[1][0:4] + filename_replace[1]
        print("s_f[1]++: ", s_f[1])
        filename_list1[jj] = f"{s_f[0]}_{s_f[1]}_{s_f[2]}_{s_f[3]}.{filename_list[jj].split('.')[1]}"
    jj = jj + 1
print("filename_list: ", filename_list)
print("filename_list1: ", filename_list1)

# print("splinted_filenames: ", split_filenames)

# os.rename(path + filename_list[0], path + filename_list[0])

# Найти дубликат файлов
count = 0
for i in range(0, len(filename_list1)):
    for j in range(i + 1, len(filename_list1)):
        if filename_list1[i] == filename_list1[j]:
            print("Same", i, j)
            count = count + 1
            # заменить счетчик
            fn = filename_list1[j].split(".")[0].split("_")
            arr_count = len(fn)
            fn[arr_count-1] = str(int(fn[arr_count-1])+1)
            if len(fn) == 3:
                filename_list1[j] = f"{fn[0]}_{fn[1]}_{fn[2]}.{filename_list[j].split('.')[1]}"
            if len(fn) == 4:
                filename_list1[j] = f"{fn[0]}_{fn[1]}_{fn[2]}_{fn[3]}.{filename_list[jj].split('.')[1]}"

print("count: ", count)

for i in range(0, len(filename_list)):
    # os.rename(path + filename_list[i], path + filename_list1[i])
    print("os.rename():", path + filename_list[i])
    print("os.rename()1:", path + filename_list1[i])