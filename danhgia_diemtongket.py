def xeploai_hocsinh(input):
    XEP_LOAI = dict()
    global Ma_HS
    Ma_HS = []
    diem_TB = []
    global xep_loai
    xep_loai = []
    f = open(input) 
    for line in f:
        if line.startswith('Ma'):       #Bỏ qua dòng đầu tiên
            continue
        else:
            ma_hs = line.strip().rstrip().split(';')[0]
            Ma_HS.append(ma_hs)         #tách lấy list Mã học sinh
            global line1
            line1 = line.strip().rstrip().split(';')[1:]
            diem_tb = ((float(line1[0]) + float(line1[4]) + float(line1[5])) * 2 + (float(line1[1]) + float(line1[2])+ float(line1[3]) + float(line1[6]) + float(line1[7]))*1)/11
            diem_TB.append(diem_tb)     # Lấy list điểm trung bình
            if diem_tb > 9:             # Xét điểm trung bình và xếp loại theo thứ tự vào list
                for i in line1:
                    if float(i) < 8:
                        xep_loai.append('Gioi')
                        break
                else:
                    xep_loai.append('Xuat_sac')
            elif diem_tb > 8:
                for i in line1:
                    if float(i) < 6.5:
                        xep_loai.append('Kha')
                        break
                else:
                    xep_loai.append('Gioi')
            elif diem_tb > 6.5:
                for i in line1:
                    if float(i) < 5:
                        xep_loai.append('Trung binh')
                        break
                else:
                    xep_loai.append('Kha')
            else:
                xep_loai.append('Trung binh')            
    XEP_LOAI = dict(zip(Ma_HS,xep_loai))        # Gộp Mã học sinh và xếp loại tương ứng thành 1 dict
    return XEP_LOAI

def xeploai_thidaihoc_hocsinh(input): 
    f = open(input)
    XEPLOAI_TDH = dict()
    global Ma_HS
    Ma_HS = []
    global xeploai_TDH1
    xeploai_TDH1 = []
    for line in f:
        if line.startswith('Ma'):               # Bỏ qua dòng đầu tiên
            continue
        else:
            xeploai_TDH = []
            ma_hs = line.strip().rstrip().split(';')[0]
            Ma_HS.append(ma_hs)                 # Tách lấy list Mã học sinh
            global line1
            line1 = line.strip().rstrip().split(';')[1:]
            khoiA = float(line1[0]) + float(line1[1]) + float(line1[2])             # tính điểm và xếp loại phù hợp của học sinh theo tiêu chí từng khối
            khoiA1 = float(line1[0]) + float(line1[1]) + float(line1[4])
            khoiB = float(line1[0]) + float(line1[2]) + float(line1[3])
            khoiC = float(line1[4]) + float(line1[6]) + float(line1[7])
            khoiD = float(line1[0]) + float(line1[4]) + float(line1[5])*2
            if khoiA >= 24:                                                         
                xeploai_TDH.append('1')
            elif 24 > khoiA >=18:
                xeploai_TDH.append('2')
            elif 18 > khoiA >=12:
                xeploai_TDH.append('3')
            elif 12 > khoiA:
                xeploai_TDH.append('4')

            if khoiA1 >= 24:
                xeploai_TDH.append('1')
            elif 24 > khoiA1 >=18:
                xeploai_TDH.append('2')
            elif 18 > khoiA1 >=12:
                xeploai_TDH.append('3')
            elif 12 > khoiA1:
                xeploai_TDH.append('4')

            if khoiB >= 24:
                xeploai_TDH.append('1')
            elif 24 > khoiB >=18:
                xeploai_TDH.append('2')
            elif 18 > khoiB >=12:
                xeploai_TDH.append('3')
            elif 12 > khoiB:
                xeploai_TDH.append('4')

            if khoiC >= 21:
                xeploai_TDH.append('1')
            elif 21 > khoiC >=15:
                xeploai_TDH.append('2')
            elif 15 > khoiC >=12:
                xeploai_TDH.append('3')
            elif 12 > khoiC:
                xeploai_TDH.append('4')

            if khoiD >= 32:
                xeploai_TDH.append('1')
            elif 32 > khoiD >=24:
                xeploai_TDH.append('2')
            elif 24 > khoiD >20:
                xeploai_TDH.append('3')
            elif 20 > khoiD:
                xeploai_TDH.append('4')
            xeploai_TDH1.append(xeploai_TDH)
            XEPLOAI_TDH.update({Ma_HS[-1]: xeploai_TDH })           #Ghép list Mã HS và List xép loại học sinh để trả về 1 dict có mã học sinh tương ứng với xếp loại
    return XEPLOAI_TDH



def main():
    input = './diem_trungbinh.txt'
    output ='./danhgia_hocsinh.txt'
    xeploai_hocsinh(input)
    xeploai_thidaihoc_hocsinh(input)


    f = open(output, 'w')
    f.write("Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1 , xeploai_B , xeploai_C , xeploai_D" + "\n")
    for i in range(len(Ma_HS)):
        my_string = ";".join(str(x) for x in xeploai_TDH1[i])
        line = str(Ma_HS[i]) + ' ; ' + xep_loai[i] + ' ; ' + my_string
        f.write(line + '\n')
    f.close()



print(main())