import threading
import time
import os

os.system('sudo modprobe bcm2835-v4l2')

def face_detect():
	while True:
		os.system('cd /home/pi/opencv-3.3.0/samples/python && python facedetect.py')
		#time.sleep(1)

def ocr():
	thread_ocr.start()
	thread_ocr.join()
	while True:
		print("ocr")
		time.sleep(1)

def ultrasonic():
	while True:
		os.system('python /home/pi/Desktop/IEDC_opencv/ultrasonic.py')
		time.sleep(1)

def speech_recog():
	while True:
		os.system('python2.7 speech_recog.py')
		#time.sleep(1)

thread_fd = threading.Thread(target=face_detect)
thread_ocr = threading.Thread(target=ocr)
thread_sr = threading.Thread(target=speech_recog)
thread_ul = threading.Thread(target=ultrasonic)
def main():
	thread_fd.start()
	thread_ul.start()
	thread_fd.join()
	thread_ul.join()

#while __name__ == "__main__":
main()
