import os,time,sys
class main():
    def banner(self):
        print("""
        ################
        #   HaSec156   #
        ################""")
    def setup(self):
        print("[+] Installing . . .!")
        time.sleep(2)
        os.rename("modules.py","ip")
        os.system("mv ip /bin")
        os.system("pkg install curl")
        print("Installed Succeed ! Put [ip] And You Will Get Your ip" )
main().banner()
main().setup()
