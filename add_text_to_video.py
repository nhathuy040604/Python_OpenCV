import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:' + str(cap.get(3)) + ' Height:' + str(cap.get(4))
        datet = datetime.datetime.now()
        # Chuyển đổi đối tượng datetime thành chuỗi
        re
        date_str = datet.strftime('%Y-%m-%d %H:%M:%S')
        frame = cv2.putText(frame, date_str, (100, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
