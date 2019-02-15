import glob
import ic_module as monaca
import os.path as op
def test():
	
	#dirname = "Tst"#input("フォルダ名：Tst")
	files = glob.glob("/home/pi/output3" + "/*.jpg")
	cn1 = 0; cn2 = 0;
	for imgname in files :
		kind = monaca.TestProcess(imgname)
		if kind == 1:
			cn2 += 1
	cn1 += 1
 
	print("学習・非学習含め正答率は" + str(cn2*1.0/cn1) + "です。")

test()
