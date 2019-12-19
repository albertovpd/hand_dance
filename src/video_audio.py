import cv2
import numpy as np
import multiprocessing
import time
#import os
#manager = multiprocessing.Manager()
#shared_list_area = manager.list()
from synthesizer import Player, Synthesizer, Waveform

from my_functions import transforming_to_tones, plotting_notes

notes=[] # to plot notes per frame in the end
print("VIDEO-AUDIO ENGAGED")
def handsgame():    
    #Open Camera object
    cap = cv2.VideoCapture(0) 
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)


    count=300 # to give some space
    while True:
        count+=1
        #Measure execution time
        start_time = time.time()

        ret, frame = cap.read() #Capture frames from the camera
        blur = cv2.blur(frame,(3,3)) #Blur the image	
        hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV) #Convert to HSV color space
        mask2 = cv2.inRange(hsv,np.array([2,50,50]),np.array([15,255,255])) #Create a binary image with where white will be skin colors and rest is black  
        kernel_square = np.ones((11,11),np.uint8) #Kernel matrices for morphological transformation    
        kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) #Perform morphological transformations to filter out the background noise   
        dilation = cv2.dilate(mask2,kernel_ellipse,iterations = 1) #Dilation increase skin color area
        erosion = cv2.erode(dilation,kernel_square,iterations = 1) #Erosion increase skin color area
        dilation2 = cv2.dilate(erosion,kernel_ellipse,iterations = 1)    
        filtered = cv2.medianBlur(dilation2,5)
        kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))
        dilation2 = cv2.dilate(filtered,kernel_ellipse,iterations = 1)
        kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        dilation3 = cv2.dilate(filtered,kernel_ellipse,iterations = 1)
        median = cv2.medianBlur(dilation2,5)
        ret,thresh = cv2.threshold(median,127,255,0)    
        
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find contours of the filtered frame for python3 
        
        #Find Max contour area (Assume that hand is in the frame)
        max_area=100
        ci=0	
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i   
                        
        cnts = contours[ci] #Largest area contour
        hull = cv2.convexHull(cnts) #Find convex hull
        
        hull2 = cv2.convexHull(cnts,returnPoints = False) #Find convex defects
        defects = cv2.convexityDefects(cnts,hull2)
        
        FarDefect = [] #Get defect points and draw them in the original image
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnts[s][0])
            end = tuple(cnts[e][0])
            far = tuple(cnts[f][0])
            FarDefect.append(far)
            cv2.line(frame,start,end,[0,255,0],1)
            cv2.circle(frame,far,10,[100,255,255],3)

        moments = cv2.moments(cnts) #Find moments of the largest contour
        
        if moments['m00']!=0: #Central mass of first order moments
            cx = int(moments['m10']/moments['m00']) # cx = M10/M00
            cy = int(moments['m01']/moments['m00']) # cy = M01/M00
        centerMass=(cx,cy)    

        cv2.circle(frame,centerMass,10,[100,0,255],2)  #Draw center mass
        font = cv2.FONT_HERSHEY_SIMPLEX

        distanceBetweenDefectsToCenter = [] #Distance from each finger defect(finger webbing) to the center mass
        for i in range(0,len(FarDefect)):
            x =  np.array(FarDefect[i])
            centerMass = np.array(centerMass)
            distance = np.sqrt(np.power(x[0]-centerMass[0],2)+np.power(x[1]-centerMass[1],2))
            distanceBetweenDefectsToCenter.append(distance)

    
        #----------------------------------------------------
        # AREA  
        #Print bounding rectangle
        x,y,w,h = cv2.boundingRect(cnts) 
        area=w*h
        #print(area)
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)    
        cv2.drawContours(frame,[hull],-1,(255,255,255),2)
        # --------------------------------------------------

        # turning area size intro notes
        note,areatone = transforming_to_tones(area)
        notes.append(note)

        # multiprocess. sound
        if count>=5: #to catch 1 of 5 frames 
            def worker(): 
                player = Player()
                player.open_stream()
                synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)        
                return player.play_wave(synthesizer.generate_constant_wave(areatone, 0.14))    
        count=0      

        process = multiprocessing.Process(target=worker)
        process.start()
        process.join()  
        
        # show tone and frequency
        cv2.putText(frame,"{}: {}Hz".format(note,areatone) ,(100,100),font,1,(0,255,0),2)
        
        # final image
        cv2.imshow('Dilation',frame)        
        
        k = cv2.waitKey(5) & 0xFF #close the output video by pressing 'ESC'
        if k == 27:
            break

    # def closing_cameta_in_time(counttoclose=0):
    #     counttoclose+=1
    #     print(counttoclose)
    #     if counttoclose == 15:
    #         cap.release()
    
    # counttoclose = 0

    cap.release()
    cv2.destroyAllWindows()

handsgame()
    #---------- here ends audio/video -------------

print("-----42-----")
print("Game finished. Working on your report")

# Plotting notes. Sending mail.
plotting_notes(notes) 

from fpdf import FPDF
pdf.cell(75, 10, "A Tabular and Graphical Report of Professor Criss's Ratings by Users Charles and Mike", 0, 2, 'C')
print("Please, cntrl + C to access the terminal")



