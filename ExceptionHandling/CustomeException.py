class pintError(Exception):
    pass
currpin = 1212
pin = int(input('Enter 4 digit pin'))

try:
    if pin == currpin:
        print('Account unblocked')
    else:
        raise pintError('Entered pin is', pin)
except pintError as e:
    print('Account is still blocked Incorrect pin',e)