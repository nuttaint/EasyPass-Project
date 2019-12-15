"""Easy Pass Motorway"""
#สมมติให้ ถ้ารถยนต์ขับผ่านด่านเก็บเงิน จะส่ง Input "PASS" เข้ามา พอรถออกจากทางด่วนก็ส่ง "STOP" เข้ามา
#สมมติให้ ค่าผ่านทาง 40 บาททุกด่าน
dic_car = {}
def status():    
    """ check position """
    num_car = int(input()) #จำนวนรถที่ผ่าน
    stat = []
    for i in range(num_car):
        name_car = input() #ชื่อของรถนั้น
        while True:
            cars = input()
            if cars == "STOP":
                print(stat)
                break
            stat.append(cars)
        round_pass = len(stat)
        total_money  = 40 * round_pass
        dic_car[name_car] = total_money
    print(dic_car)
    f = open("file1.txt", "w")
    f.write(str(dic_car))
    f.close()
status()


