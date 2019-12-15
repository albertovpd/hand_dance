from __future__ import division
import cv2
import numpy as np
import multiprocessing
import time
import multiprocessing
manager = multiprocessing.Manager()
shared_list_area = manager.list()


from synthesizer import Player, Synthesizer, Waveform #from src.music_from_hands import my_sound


# IN THIS SCRIPT I MULTIPROCESS AN INT (THE AREA)

cap = cv2.VideoCapture(0) #Open Camera object
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) #Decrease frame size and crop frame width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

def nothing(x):
    pass

def Angle(v1,v2): # Function to find angle between two vectors 
 dot = np.dot(v1,v2)
 x_modulus = np.sqrt((v1*v1).sum())
 y_modulus = np.sqrt((v2*v2).sum())
 cos_angle = dot / x_modulus / y_modulus
 angle = np.degrees(np.arccos(cos_angle))
 return angle

def FindDistance(A,B): # Function to find distance between two points in a list of lists
 return np.sqrt(np.power((A[0][0]-B[0][0]),2) + np.power((A[0][1]-B[0][1]),2)) 

cv2.namedWindow('HSV_TrackBar') # Creating a window for HSV track bars
h,s,v = 100,100,100 # Starting with 100's to prevent error while masking

# Creating track bar OPTIONAL
#cv2.createTrackbar('h', 'HSV_TrackBar',0,179,nothing)
#cv2.createTrackbar('s', 'HSV_TrackBar',0,255,nothing)
#cv2.createTrackbar('v', 'HSV_TrackBar',0,255,nothing)

areas=[]

while(1):
    start_time = time.time() #Measure execution time 
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
    #Find Max contour area (Assume that hand is in the frame)---- AREA---CHECK IT OUT
    max_area=100
    ci=0	
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    #Draw Contours
    #cv2.drawContours(frame, cnt, -1, (122,122,0), 3)
    #cv2.imshow('Dilation',median)            
	 			    
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
    cv2.putText(frame,'target'  ,tuple(centerMass),font,2,(100,0,255),2)     

    distanceBetweenDefectsToCenter = [] #Distance from each finger defect(finger webbing) to the center mass
    for i in range(0,len(FarDefect)):
        x =  np.array(FarDefect[i])
        centerMass = np.array(centerMass)
        distance = np.sqrt(np.power(x[0]-centerMass[0],2)+np.power(x[1]-centerMass[1],2))
        distanceBetweenDefectsToCenter.append(distance)
    
    sortedDefectsDistances = sorted(distanceBetweenDefectsToCenter) #Get an average of three shortest distances from finger webbing to center mass
    AverageDefectDistance = np.mean(sortedDefectsDistances[0:2])
 
    finger = [] #Get fingertip points from contour hull. #If points are in proximity of 80 pixels, consider as a single point in the group
    for i in range(0,len(hull)-1):
        if (np.absolute(hull[i][0][0] - hull[i+1][0][0]) > 80  ) or ( np.absolute(hull[i][0][1] - hull[i+1][0][1]) > 80):
            if hull[i][0][1] <500 :
                finger.append(hull[i][0])
      
    finger =  sorted(finger,key=lambda x: x[1]) #The fingertip points are 5 hull points with largest y coordinates
    fingers = finger[0:5]
    
    fingerDistance = [] #Calculate distance of each finger tip to the center mass
    for i in range(0,len(fingers)):
        distance = np.sqrt(np.power(fingers[i][0]-centerMass[0],2)+np.power(fingers[i][1]-centerMass[0],2))
        fingerDistance.append(distance)
    
    #----------------------------------------------------
    # AREA  
    x,y,w,h = cv2.boundingRect(cnts) #Print bounding rectangle
    area=w*h
    #print(w,h,w*h)
    areas.append(w*h)
    img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.drawContours(frame,[hull],-1,(255,255,255),2)

    #from __future__ import division
    # range1: areas,from 32k to 300k. range1=300k-32k
    # range2: frequency of guitars: from 80 to 1200Hz


    def renormalize(area):
        range1=[300000,32000]
        range2=[1200,80]
        delta1 = range1[1] - range1[0]
        delta2 = range2[1] - range2[0]
        area = (delta2 * (area - range1[0]) / delta1) + range2[0]
        return int(area)
    areatone=renormalize(areas)
    #---------------------------------------------------
    # MULTIPROC
    def worker1(areatone):
        areatone
        #l.append(area)
        #print(w,h,l)
        # esto funciona joder. Sigue adelante hijodeputa
        
    ##### Show final image ########
    cv2.imshow('Dilation',frame)
    ###############################
    
    #Print execution time
    #print time.time()-start_time
    
    #close the output video by pressing 'ESC'
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# -------------------------------------------------
    # SOUND
    def worker2():
        print("multiprocess of hand area from worker1 to worker2,MADAFAKA, which is ", area, areatone)

        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
        if areatone>50000:

            # Play A4
            player.play_wave(synthesizer.generate_constant_wave(areatone, 0.15))
            # Play C major  
            #chord = [261.626,  329.628, 391.996]
            #chord=[w,h,area]
            #player.play_wave(synthesizer.generate_chord(chord, 0.05))
#------------------------------------------------

    process1 = multiprocessing.Process(target=worker1, args=[shared_list_area])
    process2 = multiprocessing.Process(target=worker2)

    process1.start()
    process2.start()
    process1.join()
    process2.join()


cap.release()
cv2.destroyAllWindows()