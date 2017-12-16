import glob

ttylist = glob.glob('/dev/ttyACM*')

if len(ttylist) == 0:
    print( 'ERROR: No Arduino devices found at /dev/ttyACM*' )
    exit

if len(ttylist) > 1:
    print( 'WARNING: Multiple Arduino devices found at /dev/ttyACM*, using first device' )

for tty in ttylist:
    print(tty)
