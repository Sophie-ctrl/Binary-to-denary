'''
Author: Sophie
Date：2018/12/6
'''

print("Enter 'x' for exit.");
binary = input("Enter number in Binary Format: ");
if binary == 'x':
    exit();
else:
    decimal = int(binary, 2);
    print(binary,"in Decimal =",decimal);
while True:
    bi_nary = []
    u = eval(input('If you want to continue tap 1, if you want to stop tap 2.'))

    if u == 1:
        while u == 1:
            print('OK, repeating...')
            binary = input("Enter number in Binary Format: ")
            decimal = int(binary, 2);
            print(binary,"in Decimal =",decimal)
            break
    elif u == 2:
        print('Bye then!')
        break        
