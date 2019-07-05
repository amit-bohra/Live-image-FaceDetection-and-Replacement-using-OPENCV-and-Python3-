import cv2
kite=cv2.imread(r'a.png')#provide any imagepath
v=cv2.VideoCapture(0)
#fd=cv2.CascadeClassifier(r'C:\Program Files (x86)\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
fd=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
while(True):
    ret,i=v.read()  #THRESHOLD AND READ HAS TWO PARAMETERS
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j) #2 2 times kernel, 7 is striding i.e making block after 7 pixels
    print(f)
    for(x,y,w,h) in f:
        cv2.rectangle(i,(x,y,w,h),(0,0,255),50)
        tuply=i[y:y+h,x:x+h,:].shape
        r=cv2.resize(kite,(tuply[1],tuply[0]),interpolation=cv2.INTER_AREA)
        i[y:y+h,x:x+h,:]=r
    cv2.imshow('image',i)
    key=cv2.waitKey(5)
    if key==ord('q'):
        cv2.destroyAllWindows()
        cv2.release()
        break
