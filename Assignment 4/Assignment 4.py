'''
Created on 2/18/2022
@author:   Akshatha Vasant Hegde
filename: hw4.py
pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS515 - Hw 4
'''

#Required functions

def pascal_row(rows) :
    ''' Returns only relevent row '''
    if rows < 0 :
        return "invalid"
    else:
        z = make_triangle(rows+1, x = 0, whole_tri_lst = [])
        return z[-1:]


    
def pascal_triangle(rows):
    ''' Returns the triangle '''
    if rows < 0 :
        return "invalid"
    else:
        z = make_triangle(rows+1, x = 0, whole_tri_lst = [])
        return z


#Helper functions    

def make_curr_row(n, prev_row, r = 0, current_row = []) :
    """This function takes n-row number, prev_row the list, r is counter, and current row
        The function returns the current rows list"""
    if r == n+1 :
        return current_row
    elif r == 0 or r == n:
        return make_curr_row(n, prev_row, r+1, current_row = current_row + [1])
    else :
        return make_curr_row(n, prev_row, r+1, current_row = current_row + [prev_row[r-1] + prev_row[r]])
    


def make_triangle(n, x = 0, whole_tri_lst = []):
    ''' let x be row number. n is number of rows. runs make_curr_row for each row '''
    if x == n :
        return whole_tri_lst
    elif x == 0 :
        whole_tri_lst = whole_tri_lst + [[1]]
        return make_triangle(n, x+1, whole_tri_lst)
    else :
        a = x - 1
        whole_tri_lst = whole_tri_lst + [make_curr_row(x, whole_tri_lst[a], r = 0, current_row = [])]
        return make_triangle(n, x+1, whole_tri_lst)

#Test functions

def test_pascal_row():
    assert pascal_row(0) == [[1]]
    assert pascal_row(-1) == 'invalid'
    assert pascal_row(5) == [[1, 5, 10, 10, 5, 1]]
    assert pascal_row(13) == [[1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1]]
    assert pascal_row(15) == [[1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1]]

def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(-1) == 'invalid'
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
    assert pascal_triangle(10) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]
