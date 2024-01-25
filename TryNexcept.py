'''
The python function, find_average() given below, is written to accept a list of marks and return the average marks. On execution, the program is resulting in an error.

def find_average(mark_list):
          total=0
          for i in range(0, len(mark_list)):
                   total+=mark_list1[i]
          marks_avg=total/len(mark_list)
          return marks_avg
m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))
1: Add code to handle the exception occurring in the code.

2: Make the necessary correction in the program to remove the error.

3: Make the following changes in the code, execute, observe the results. Add code to handle the errors occurring in each case.

Case – 1: Initialize m_list as ["1",2,3,4]

Case – 2: Initialize m_list as given below

mark1="A"
mark1=int("A")
m_list=[mark1,2,3,4]
Case – 3: Initialize m_list as []

Case – 4: Make the following change in the for loop statement

for i in range(0, len(mark_list)+1):
'''

def find_average(mark_list):
    total=0
    marks_avg = 0
    try:
        for i in range(0, len(mark_list)):
            total+=mark_list[i]
            marks_avg=total/len(mark_list)
    except NameError:
        print("Name of variable error")
        return
    except TypeError:
        print("Type mismatch error")
        return
    except IndexError:
        print("Index out of range")
        return
    return marks_avg
m_list=["a",1,2,3,4]
print("Average marks:", find_average(m_list))
