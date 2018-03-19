import time
import os
import sys
# Imports the monkeyrunner modules used by this program
try:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
    from com.android.monkeyrunner.easy import EasyMonkeyDevice
    from com.android.monkeyrunner.easy import By
except:
    print 'This bot uses monkeyrunner python module & tesseract-cli, Please make sure they\'re installed'
    sys.exit()



def get_ips(new_flag):
    print '[+] Generating IPs ....'
    if new_flag:
        result = os.popen('python ./get_ips.py').read()
        if result == 'false':
            print 'Error occured while generating ips'
            print 'Trying to open old generated file'
    ips_file = open('ips.txt', 'r')
    return ips_file


def ocr():
    text = os.popen('tesseract -l eng ./screen.png stdout').read()
    if 'Scan failed! Update your Scan Software.' in text or 'Trojan success chance:' in text or 'Target not found' in text:
        if '[i] Trojan success chance: 90%' in text:
            return 'Attack'
        else:
            return 'Pass'
    elif 'TROJAN TRANSFER successful.' in text:
        return 'Pass'
    else:
        return 'Wait'


def main():
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    easy_device = EasyMonkeyDevice(device)

    # sets a variable with the package's internal name
    package = 'org.vhack.dev.vhack'

    # sets a variable with the name of an Activity in the package
    activity = 'org.vhack.dev.vhack.SplashActivity'

    # sets the name of the component to start
    runComponent = package + '/' + activity

    # Runs the component
    device.startActivity(component=runComponent)

    ips = get_ips(0)
    time.sleep(3)
    print 'Start Playing........'

    easy_device.touch(By.id('id/btnNetwork'), MonkeyDevice.DOWN_AND_UP)
    time.sleep(1.5)

    for ip in ips:
        for i in xrange(15):
            device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
        device.type(ip.strip())
        easy_device.touch(By.id('id/btnScanIP'), MonkeyDevice.DOWN_AND_UP)
        output = 1
        print '[+] Scanning %s' % ip.strip()
        while output:
            time.sleep(3)
            # Takes a screenshot
            result = device.takeSnapshot()

            # Writes the screenshot to a file
            result.writeToFile('./screen.png', 'png')

            ocr_res = ocr().strip()
            if ocr_res == 'Attack':
                output = 0
                easy_device.touch(By.id('id/btnTransferIP'), MonkeyDevice.DOWN_AND_UP)
                print '[#] Attacking Target'
                time.sleep(2)
            elif ocr_res == 'Pass':
                output = 0
                print '[-] Pass Target'
            elif ocr_res == 'Wait':
                print '[!] Waiting'
            else:
                output = 0
                print 'Unknown'

if __name__ == '__main__':
    main()
