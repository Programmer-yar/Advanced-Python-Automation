#Checks Whether the file directly run by python or if it is being imported
#if this file is imported in another file then '__name__' will return file_name

#Below 'if' statement is used to encapsulate 'tests' in files containing classes
#The tests will not run when class is imported into another program/file
if __name__ == '__main__':
    print(f'First Module name: {__name__}')
    print('Running directly')

else:
    print(f'First Module name: {__name__}')
    print('Running from import\n')

#will give output as __main__
#print(__name__)


