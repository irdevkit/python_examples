import serial

# configure the serial connections (the parameters differs on the device you are connecting to)

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser.isOpen()

startLearningModeCmd = bytearray([224])
ser.write(startLearningModeCmd)

# read the start leaning mode response.
data = ser.readline().rstrip()

# wait for the ir signal
while 1:
    data = ser.readline().rstrip()

    if not data:
        continue
                          
    ba = bytearray(data)    
    ir = ",".join(str(bit) for bit in ba)
    print ir