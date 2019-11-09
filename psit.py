"""Easy Pass Motorway"""
#สมมติให้ ถ้ารถยนต์ขับผ่านด่านเก็บเงิน จะส่ง Input "PASS" เข้ามา พอรถออกจากทางด่วนก็ส่ง "STOP" เข้ามา
#สมมติให้ ค่าผ่านทาง 40 บาททุกด่าน
total = 0
def status():
    """ check position """
    stat = []
    while True:
        cars = input()
        if cars == "STOP":
            print(stat)
            break
        stat.append(cars)
    round_pass = len(stat)
    total_money  = 40 * round_pass
    print(" Amount of money is " + str(total_money))
status()
