Name = input("Enter employee's name: ")
hrs = eval(input('Enter number of hours worked in a week: '))
rate = eval(input('Enter hourly pay rate: '))
ftax = eval(input('Enter federal tax withholding rate: '))
stax = eval(input('Enter state tax withholding rate: '))
print('Employee Name:',Name)
print('Hours Worked: ',str(format(hrs,'.2f')))
print('Pay Rate: $',str(format(rate,'.2f')))
print('Gross Pay: $',str(format(rate*hrs,'.2f')))
print('Deductions: \n'\
      '  Federal Withholding ({}):'.format(format(ftax,'.2%')),'$',format(rate*hrs*ftax,'.2f'),\
      '\n  State Withholdong ({}):'.format(format(stax,'.2%')),'$',format(rate*hrs*stax,'.2f'),\
      '\n  Total Deduction: ','$',format(rate*hrs*(ftax+stax),'.2f'))
npay = (rate*hrs) - (rate*hrs*(ftax+stax))
print('Net Pay: $',format(npay,'.2f'))
