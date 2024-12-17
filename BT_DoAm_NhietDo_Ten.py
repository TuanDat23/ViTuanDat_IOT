from sense_emu import SenseHat
import time

# Khoi tao Sense HAT
cam_bien = SenseHat()

# Mau sac cho LED
DO = [255, 0, 0]
DEN = [0, 0, 0]

# Hien thi chu "DAT" tren LED ma tran
def hien_thi_DAT():
    cam_bien.clear()  # Xoa man hinh
    cam_bien.show_message("DAT", text_colour=DO, back_colour=DEN, scroll_speed=0.1)

# Ham doc va in du lieu cam bien
def doc_cam_bien():
    # Doc nhiet do, do am
    nhiet_do = cam_bien.get_temperature()
    do_am = cam_bien.get_humidity()
    
    # Doc trang thai joystick
    su_kien = cam_bien.stick.get_events()
    for sk in su_kien:
        if sk.action == "pressed":
            print(f"Joystick: {sk.direction} nhan")

    # In du lieu ra man hinh console
    print(f"Nhiet do: {nhiet_do:.1f}°C, Do am: {do_am:.1f}%")

# Vong lap chinh
def chuong_trinh_chinh():
    while True:
        doc_cam_bien()
        hien_thi_DAT()
        time.sleep(2)  # Cho 2 giay truoc khi lap lai

# Chay chuong trinh
if __name__ == "__main__":
    chuong_trinh_chinh()
