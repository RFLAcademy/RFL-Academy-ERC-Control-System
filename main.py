from motor_library import *

set_motor_config("THIRTY")  # Change as needed for your device

stop_all()
print("All motors stopped and system ready.")

oled_status("   RFL ACADEMY", "System Ready", "Press START", "Hello Prashant")
wait_for_start()

while True:
#////////////////////////////////////////////////// MANAUL CONTROL SECTION/////////////////////////////////////////////////
#     wait_for_start()
#     FL(speed=40)
#     wait(1)
#     stop_drive(FL)
    # Wait until START button is pressed
   
    #if sensor_3() == 1
       
    #else:
        #stop_drive(FW)
    
#     led_on()
#     buzz(1, 10)   #buzzer (duration, no. of beeps for the duration
#     wait(1)
#                             
#     led_off()
#     wait(1)
#     
#     servo1.pos(0)
#     wait(1)
# 
#     # ---------------- Mecanum Movements ----------------
#     run("front_right", speed=50, direction=1)
#     oled_status("Front Right", "Speed = 50%", "Direction = 1", "Duration = 2 Sec")
#     wait(2)
#     
#     run("front_left", speed=50, direction=1)
#     oled_status("Front Left", "Speed = 50%", "Direction = 1", "Duration = 2 Sec")
#     wait(2)
#     stop("front_right");
#     
#     run("back_right", speed=50, direction=1)
#     oled_status("Back_Right", "Speed = 50%", "Direction = 1", "Duration = 2 Sec")
#     wait(2)
#     stop("front_left");
#     
#     run("back_left", speed=50, direction=1)
#     wait(2)
#     stop("back_right")
#     run("extra_motor", speed=60, direction =1)
#     wait(6)
#     stop("extra_motor")     
#     wait(2)     
#     run("extra_motor", speed=60, direction =0)
#     wait(7)
#     #stop("back_left")
#     stop("extra_motor")
#     # ---------------- Mecanum Movements ----------------     
#     FW(speed=50)
#     wait(1)
#     stop_drive(FW)
#     wait(2)
#     BW(speed=50)
#     wait(1)
#     stop_drive(BW)
#     wait(2)
#     L(speed=50)
#     wait(1)
#     stop_drive(L)
#     wait(2)
#     R(speed=50)
#     wait(1)
#     stop_drive(R)
#     wait(2)
#     CCW(speed=50)
#     wait(1)
#     stop_drive(CCW)
#     wait(2)
#     CW(speed=50)
#     wait(1)
#     stop_drive(CW)
#     wait(1)
#     FL(speed=50)
#     wait(1)
#     stop_drive(FL)
#     wait(2)
#     BR(speed=50)
#     wait(1)
#     stop_drive(BR)
#     wait(2)
#     FR(speed=50)
#     wait(1)
#     stop_drive(FR)
#     wait(2)
#     BL(speed=50)
#     wait(1)
#     stop_drive(BL)
#     wait(2)

    # Stop all motors at the end
stop_all()
#////////////////////////////////////////////////// MANAUL CONTROL SECTION/////////////////////////////////////////////////
# REMOVE COMMENT FROM BELOW LINE FOR REMOTE CONTROLL AND PUT ABOVE MANUAL CONTROL SECTION IN COMMENT
#     if key("UP"):
#         FW(speed=40)
#         oled_status(" FORWARD")
# 
#     elif key("DOWN"):
#         BW(speed=40)
#         oled_status(" BACKWARD")
# 
#     elif key("LEFT"):
#         L(speed=40)
#         oled_status(" LEFT")
# 
#     elif key("RIGHT"):
#         R(speed=40)
#         oled_status(" RIGHT")
# 
#     elif key("UPLEFT"):
#         FL(speed=40)
#         oled_status(" FORWARD LEFT")
# 
#     elif key("UPRIGHT"):
#         FR(speed=40)
#         oled_status(" FORWARD RIGHT")
# 
#     elif key("DOWNLEFT"):
#         BL(speed=40)
#         oled_status(" BACK LEFT")
# 
#     elif key("DOWNRIGHT"):
#         BR(speed=40)
#         oled_status(" BACK RIGHT")
# 
#     elif key("Q"):
#         CCW(speed=80)
#         oled_status(" ROTATE LEFT")
# 
#     elif key("E"):
#         CW(speed=80)
#         oled_status(" ROTATE RIGHT")
# 
#     elif key("EXTRAUP"):
#         extra_motor(speed=40, direction=1)
#         oled_status(" EXTRA UP")
# 
#     elif key("EXTRADOWN"):
#         extra_motor(speed=40, direction=0)
#         oled_status(" EXTRA DOWN")
# 
#     elif key("A"):              # A button: servo open
#         stop_drive()
#         servo1.pos(0.5)
#         oled_status(" BUTTON A")
# 
#     elif key("B"):              # B button: servo close
#         stop_drive()
#         servo2.pos(0.5)
#         oled_status(" BUTTON B")
#         
#     elif key("C"):              # C button: servo close
#         stop_drive()
#         servo3.pos(0.0)
#         oled_status(" BUTTON C")
#         
#     elif key("D"):              # D button: servo close
#         stop_drive()
#         servo4.pos(0.0)
#         oled_status(" BUTTON D")
# 
#     else:
#         stop_drive()
#         oled_status(" STOPPED")

