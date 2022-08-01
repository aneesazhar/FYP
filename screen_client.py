import socket, cv2, pickle, struct
import imutils
import pyautogui
import numpy as np


def student_screen_show():
    camera = True
    if camera == True:
        vid = cv2.VideoCapture(0)
    else:
        vid = cv2.VideoCapture('videos/mario.mp4')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = '192.168.43.58'
    port = 9999
    client_socket.connect((host_ip, port))

    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "Recording.avi"
    fps = 60.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)


    if client_socket:
        while (vid.isOpened()):
            try:
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                frame = imutils.resize(frame, width=380)
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a
                client_socket.sendall(message)
                cv2.imshow(f"TO: {host_ip}", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    client_socket.close()
            except:
                print('VIDEO FINISHED!')
                break



