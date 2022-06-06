import cv2
import numpy as np
#import matplotlib import pyplot as plt
a=0
count=0
idc=False
itc=False
f=False
t1=(0,0,1)
p1=(0,0,1)
t2=(0,0,2)
p2=(0,0,2)
t3=(0,0,3)
p3=(0,0,3)
t4=(0,0,4)
p4=(0,0,4)
t5=(0,0,5)
p5=(0,0,5)
t6=(0,0,6)
p6=(0,0,6)
t7=(0,0,7)
p7=(0,0,7)
t8=(0,0,8)
p8=(0,0,8)
t9=(0,0,9)
p9=(0,0,9)
def game():

    def tictactoe():
        def draw (event,x,y,flag,param) :
            global a,count,idc,itc,f,count
            global t1,t2,t3,t4,t5,t6,t7,t8,t9
            global p1,p2,p3,p4,p5,p6,p7,p8,p9

            if event==cv2.EVENT_LBUTTONDOWN :
                if(a==0):
                    if (x>136 and x<216) and (y>136 and y<216):
                        cv2.line(img,(176 - 10, 176 + 10),(176+10,176-10),(255,0,0),4)
                        cv2.line(img, (176 - 10, 176 - 10), (176 + 10, 176 + 10), (255, 0, 0), 4)
                        t1=(255, 0, 0)
                    elif (x>216 and x<296) and (y>136 and y<216):
                        cv2.line(img,(256 - 10, 176 + 10),(256+10,176-10),(255,0,0),4)
                        cv2.line(img, (256 - 10, 176 - 10), (256 + 10, 176 + 10), (255, 0, 0), 4)
                        t2=(255, 0, 0)
                    elif (x>296 and x<376) and (y>136 and y<216):
                        cv2.line(img,(336 - 10, 176 + 10),(336+10,176-10),(255,0,0),4)
                        cv2.line(img, (336 - 10, 176 - 10), (336 + 10, 176 + 10), (255, 0, 0), 4)
                        t3=(255, 0, 0)
                    elif (x>136 and x<216) and (y>216 and y<296):
                        cv2.line(img,(176 - 10, 256 + 10),(176+10,256-10),(255,0,0),4)
                        cv2.line(img, (176 - 10, 256 - 10), (176 + 10, 256 + 10), (255, 0, 0), 4)
                        t4=(255, 0, 0)
                    elif (x>216 and x<296) and (y>216 and y<296):
                        cv2.line(img,(256 - 10, 256 + 10),(256+10,256-10),(255,0,0),4)
                        cv2.line(img, (256 - 10, 256 - 10), (256 + 10, 256 + 10), (255, 0, 0), 4)
                        t5=(255, 0, 0)
                    elif (x>296 and x<376) and (y>216 and y<296):
                        cv2.line(img,(336 - 10, 256 + 10),(336+10,256-10),(255,0,0),4)
                        cv2.line(img, (336 - 10, 256 - 10), (336 + 10, 256 + 10), (255, 0, 0), 4)
                        t6=(255, 0, 0)
                    elif (x>136 and x<216) and (y>296 and y<376):
                        cv2.line(img,(176 - 10, 336 + 10),(176+10,336-10),(255,0,0),4)
                        cv2.line(img, (176 - 10, 336 - 10), (176 + 10, 336 + 10), (255, 0, 0), 4)
                        t7=(255, 0, 0)
                    elif (x>216 and x<296) and (y>296 and y<376):
                        cv2.line(img,(256 - 10, 336 + 10),(256+10,336-10),(255,0,0),4)
                        cv2.line(img, (256 - 10, 336 - 10), (256 + 10, 336 + 10), (255, 0, 0), 4)
                        t8=(255, 0, 0)
                    elif (x>296 and x<376) and (y>296 and y<376):
                        cv2.line(img,(336 - 10, 336 + 10),(336+10,336-10),(255,0,0),4)
                        cv2.line(img, (336 - 10, 336 - 10), (336 + 10, 336 + 10), (255, 0, 0), 4)
                        t9=(255, 0, 0)
                    a=1
                    count+=1
                    print(a)
                elif a==1:
                    if (x>136 and x<216) and (y>136 and y<216):
                        cv2.circle(img, (176,176), 1, (255, 255, 255), -1)
                        cv2.circle(img, (176,176), 10, (255, 255, 255), 4)
                        p1=(255, 255, 255)

                    elif (x>216 and x<296) and (y>136 and y<216):
                        cv2.circle(img, (256,176), 1, (255, 255, 255), -1)
                        cv2.circle(img, (256,176), 10, (255, 255, 255), 4)
                        p2=(255, 255, 255)
                    elif (x>296 and x<376) and (y>136 and y<216):
                        cv2.circle(img, (336,176), 1, (255, 255, 255), -1)
                        cv2.circle(img, (336,176), 10, (255, 255, 255), 4)
                        p3=(255, 255, 255)
                    elif (x>136 and x<216) and (y>216 and y<296):
                        cv2.circle(img, (176,256), 1, (255, 255, 255), -1)
                        cv2.circle(img, (176,256), 10, (255, 255, 255), 4)
                        p4=(255, 255, 255)
                    elif (x>216 and x<296) and (y>216 and y<296):
                        cv2.circle(img, (256,256), 1, (255, 255, 255), -1)
                        cv2.circle(img, (256,256), 10, (255, 255, 255), 4)
                        p5=(255, 255, 255)
                    elif (x>296 and x<376) and (y>216 and y<296):
                        cv2.circle(img, (336,256), 1, (255, 255, 255), -1)
                        cv2.circle(img, (336,256), 10, (255, 255, 255), 4)
                        p6=(255, 255, 255)
                    elif (x>136 and x<216) and (y>296 and y<376):
                        cv2.circle(img, (176,336), 1, (255, 255, 255), -1)
                        cv2.circle(img, (176,336), 10, (255, 255, 255), 4)
                        p7=(255, 255, 255)
                    elif (x>216 and x<296) and (y>296 and y<376):
                        cv2.circle(img, (256,336), 1, (255, 255, 255), -1)
                        cv2.circle(img, (256,336), 10, (255, 255, 255), 4)
                        p8=(255, 255, 255)
                    elif (x>296 and x<376) and (y>296 and y<376):
                        cv2.circle(img, (336,336), 1, (255, 255, 255), -1)
                        cv2.circle(img, (336,336), 10, (255, 255, 255), 4)
                        p9=(255, 255, 255)
                    a=0
                    count+=1
                    print(a)
                if(t1==t2 and t2==t3):
                    idc=True
                if(t1==t4 and t4==t7):
                    idc=True
                if(t1==t5 and t5==t9):
                    idc=True
                if(t2==t5 and t5==t8):
                    idc=True
                if(t3==t6 and t6==t9):
                    idc=True
                if(t4==t5 and t5==t6):
                    idc=True
                if(t7==t8 and t8==t9):
                    idc=True
                if(t3==t5 and t5==t7):
                    idc=True

                if(p1==p2 and p2==p3):
                    itc=True
                if(p1==p4 and p4==p7):
                    itc=True
                if(p1==p5 and p5==p9):
                    itc=True
                if(p2==p5 and p5==p8):
                    itc=True
                if(p3==p6 and p6==p9):
                    itc=True
                if(p4==p5 and p5==p6):
                    itc=True
                if(p7==p8 and p8==p9):
                    itc=True
                if(p3==p5 and p5==p7):
                    itc=True
                if(itc==False or idc==False):
                    f=True

        img= np.zeros((512,512,3),np.uint8)
        cv2.line(img,(136,216),(376,216),(0,0,255),2)
        cv2.line(img,(136,296),(376,296),(0,0,255),2)
        cv2.line(img,(216,136),(216,376),(0,0,255),2)
        cv2.line(img,(296,136),(296,376),(0,0,255),2)

        cv2.namedWindow("image",cv2.WINDOW_NORMAL)

        cv2.setMouseCallback("image",draw)
        while True:
            cv2.imshow("image", img)
            k=cv2.waitKey(1)
            if(k==27):
                cv2.destroyAllWindows()
                game()
                break
            if(itc==True):
                cv2.putText(img,"Winner Is O",(130,450), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 3)
                cv2.putText(img, "Press esc to go to startwindow", (50, 470), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 3)
                cv2.imshow("image", img)
                k = cv2.waitKey(0)
                if (k == 27):
                    cv2.destroyAllWindows()
                    game()
                    break
            elif(idc==True):
                 cv2.putText(img,"Winner Is Cross ",(130,450), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
                 cv2.putText(img, "Press esc to go to startwindow", (50, 470), cv2.FONT_HERSHEY_PLAIN, 1.5,
                             (255, 255, 255), 3)
                 cv2.imshow("image", img)
                 k=cv2.waitKey(0)
                 if(k==27):
                    cv2.destroyAllWindows()
                    game()
                    break
            elif(f==True and count==9):
                cv2.putText(img, "Draw ", (130, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
                cv2.putText(img, "Press esc to go to startwindow", (50, 470), cv2.FONT_HERSHEY_PLAIN, 1.5,
                            (255, 255, 255), 3)
                cv2.imshow("image", img)
                k = cv2.waitKey(0)
                if (k == 27):
                    cv2.destroyAllWindows()
                    game()
                    break


    def check(event,x,y,flag,param):

        if(event==cv2.EVENT_RBUTTONDOWN):
            if(x>100 and x<200 and y>200 and y < 250):
                cv2.destroyAllWindows()
                tictactoe()
            elif(x>300 and x<400 and y>200 and y < 250):
                print("1")
                cv2.destroyAllWindows()
    gameScreen= np.zeros((512,512,3),np.uint8)
    cv2.putText(gameScreen,"Tic-Tac-Toe",(150,100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
    cv2.rectangle(gameScreen,(100,200),(200,250),(0,255,0),-1)
    cv2.putText(gameScreen,"start",(105,230), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
    cv2.rectangle(gameScreen,(300,200),(400,250),(0,0,255),-1)
    cv2.putText(gameScreen,"Exit",(315,230), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)
    cv2.namedWindow("GameScreen",cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("GameScreen", check)
    cv2.imshow("GameScreen", gameScreen)
    cv2.waitKey(0)

game()




