from tkinter import *
from tkinter import messagebox
import os
entries = []
        
def initialize(top,arr):
    E = entries[0]
    m=1
    for i in range(9):
        for j in range(9):
            if(not E.get()):
                arr[i][j] = 0
            else:
                try:
                    if int(E.get()):
                        arr[i][j] = int(E.get())
                    else:
                       messagebox.showwarning("Warning",  "Enter Integers From 1 to 9 Only")
                       button_reset.invoke() 
                except ValueError:
                    messagebox.showwarning("Warning",  "Enter Integers From 1 to 9 Only ")
                    button_reset.invoke()
            if(m<=80):
                E = entries[m]
                m+=1
    checker(top,arr)
    squarecheck(top,arr)
            
def print_maze(arr):
    clean_Mess()
    E = entries[0]
    m=1
    for i in range(9):
        for j in range(9):
            E.insert(1,arr[i][j])
            if(m<=80):
                E = entries[m]
                m+=1
        
def find_empty_location(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
def used_in_row(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
def used_in_col(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False
def check_location_is_safe(arr,row,col,num):
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)

def solve_sudoku(arr):
    l=[0,0]
    if(not find_empty_location(arr,l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,10):
        if(check_location_is_safe(arr,row,col,num)):
            arr[row][col]=num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False

def createGUI(maze):
    top = Tk()
    top.title("Sudoku")
    canvas = Canvas(top, height=320, width =350)
    createRow(canvas)
    createCol(canvas)
    createEntry(top)
    createButtons(top,maze)
    canvas.pack(side = 'top')
    top.mainloop()
    
def createButtons(top,maze):
    button_solve = Button(top, text="Solve", justify='left', default='active', command = lambda: play_Game(top,maze))
    button_reset = Button(top, text="Reset", justify='right', command = lambda: clean_Mess())
    button_solve.place(x=70, y=275, height=30, width=60)
    button_reset.place(x=230, y=275, height=30, width=60)
    
def clean_Mess():
    for e in entries:
        e.delete(0, END)
        
def checker(top,arr):
    c=0
    r=0
    for i in range(9):
        for j in range(9):
            if arr[i][j]!=0:
                for k in range(i+1,9):
                    if(arr[i][j]==arr[i][k]):
                        r=r+1
                    if(arr[i][j]==arr[k][j]):
                        c=c+1
    
    if c>0:
        messagebox.showinfo("Information",  "Numbers have repeated within the row or column")
        button_reset.invoke()

def check(arr,startRow,startCol):
    st = set()
    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
            if curr in st:
                return False
            if curr != 0:
                st.add(curr)
         
    return True
def checks(arr,row,col):
    return check(arr, row - row % 3, col - col % 3)
def squarecheck(top,arr):
    sa=0
    for i in range(9):
        for j in range(9):
            if arr[i][j]!=0:
                if not checks(arr,i,j):
                    sa=sa+1
    if sa!=0:
        messagebox.showinfo("Information",  "Numbers have repeated within the square")
        button_reset.invoke()
    
def play_Game(top,maze):
    initialize(top,maze)
    if(solve_sudoku(maze)):
        print_maze(maze)
    else:
        print ("No solution found")
    
def createEntry(top):
    p,q=41.4,41.4
    for i in range(9):
        for j in range(9):
            E = Entry(top, width=3, font = 'BOLD')
            E.grid(row=i, column=j)
            E.place(x=p, y=q, height=20, width=25)
            entries.append(E)
            p+=30.0
        q+=24.5
        p=41.2
    
def createRow(canvas):
    i,j=40,40
    p=40
    q=260
    for m in range(10):
        if(m%3==0):
            canvas.create_line(i,j,p,q,width=2.5)
        else:
            canvas.create_line(i,j,p,q,width=2)
        i+=30
        p+=30
    
def createCol(canvas):
    i,j=40,40
    p,q=310,40
    for m in range(10):
        canvas.create_line(i,j,p,q,width=2.3)
        j+=24.5
        q+=24.5

    
if __name__=="__main__":
    
    maze=[[0 for x in range(9)]for y in range(9)]
    createGUI(maze)
