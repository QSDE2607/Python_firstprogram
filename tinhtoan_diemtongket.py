MH = []
Ma_HS = []

def tinhdiem_trungbinh(input):
    big_dict = dict()
    fhand = open(input)
    for line in fhand:
        # Lấy list môn học
        if line.startswith("Ma"):
            MH = line.rstrip().split(',')[1:]
        else:
            line = line.rstrip().split(";")
            Ma_HS.append(line[0])  # lấy list mã học sinh
            small_dict = dict()
            line1 = [item.split(',')for item in line[1:]]
            for i in MH:            #Xét từng học sinh để tính điểm trung bình
                x = MH.index(i)
                a = line1[x]
                if len(a) == 4:
                    diem_tb = float(a[0])*0.05 + float(a[1])*0.1 + float(a[2])*0.15 + float(a[3])*0.7
                else:
                    diem_tb = float(a[0])*0.05 + float(a[1])*0.1 + float(a[2])*0.1 + float(a[3])*0.15 + float(a[4])*0.6
                small_dict.update({i : round(diem_tb,2)})       #tính điểm trung bình của từng học sinh và môn học sau đó cập nhập vào dict nhỏ
            big_dict.update({Ma_HS[-1] : small_dict})           #ghep mã học sinh tương ứng với thông tin điểm trung bình từng môn học
    fhand.close()
    return big_dict


def luudiem_trungbinh(input,output):        #Ghi kết quả vào file
    f = open(output, 'w')
    f.write("Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia " + "\n")    #tạo tên các cột vào dòng đầu
    for key in input:
        line = str(key)
        for x in input[key]:
            line += ";" + (str(input[key][x]))
        f.write(line + "\n")
    f.close()
    print("Đã ghi kết quả vào file")

def main():
    input = "./diem_chitiet.txt"                #truyền file  vào hàm
    output = "./diem_trungbinh.txt"             #xuất file 
    dict_DTB = tinhdiem_trungbinh('diem_chitiet.txt')
    luudiem_trungbinh(dict_DTB,output)


main()
