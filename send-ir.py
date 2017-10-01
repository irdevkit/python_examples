import serial

# configure the serial connection

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser.isOpen()

# format:
# [227, your ir goes here]
      
irSignal = bytearray([227, 152,35,181,140,247,128,95,185,73,94,94,240,253,178,78,139,68,93,94,98,96,179,78,4,64,35,18,137,174,124,6,11,253,43,26,145,182,132,14,19,5,51,34,153,190,140,22,27,13,59,42,161,198,148,30,35,21,67,50,169,206,156,38,43,29,75,58,177,214,121,35,38,24,69,35,152,204,137,18,39,8,69,51,168,188,137,34,23,24,69,51,169,205,153,18,23,24,70,18,169,204,154,35,23,7,68,34,152,205,138,35,39,24,69,50,153,204,153,18,39,23,53,50,169,204,137,19,39,24,69,51,169,205,154,35,23,24,53,51,153,189,154,35,39,8,69,50,153,188,138,37,48])
ser.write(irSignal)

# read the response.
data = ser.readline().rstrip()
