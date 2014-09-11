from PyQt4 import QtCore
import serial
import struct

class SerialController(QtCore.QThread):

    portname = 'COM8'
    data_received = QtCore.pyqtSignal(dict)

    def __init__(self):
        super(SerialController,self).__init__()
        self.serial_fd = None
        self.runFlag = False


    def open_serial(self):
        self.serial_fd = serial.Serial(self.portname,115200)
        self.runFlag = True
        self.start()

    def stop_serial(self):
        self.runFlag = False
        self.join()


    def run(self):

        while self.runFlag:
            magic = self.serial_fd.read()
            if ord(magic) != 0x7e:
                print('first magic doesnt match')
                continue
            magic = self.serial_fd.read()
            if ord(magic) != 0x45:
                print('second magic doesnt match')
                continue
            length = ord(self.serial_fd.read())
            data = self.serial_fd.read(length)
            num = length / 3
            i = 0
            emitData={}
            while i < num:
                coordinate = (data[i*3])
                pressure = struct.unpack('>H',data[i*3+1:i*3+3])
                i += 1
                #print("%d:%d"%(coordinate,pressure[0]))
                emitData[coordinate]=pressure[0]
            self.data_received.emit(emitData)
            checksum = self.serial_fd.read()






