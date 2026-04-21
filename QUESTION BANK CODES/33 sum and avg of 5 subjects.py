def sum_avg():
    t=0
    for i in range(1,6):
        a=int(input(f"Enter marks of subject {i}:"))
        t=t+a
    print("Total of 5 subjects:",t)
    print("Average of 5 subjects:",t/5)
sum_avg()    
