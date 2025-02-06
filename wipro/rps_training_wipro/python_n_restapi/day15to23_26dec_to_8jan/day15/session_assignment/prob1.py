# Q1. Print series 0,3,8,15,24,35,48,63,80,99

n = 0
while True:
    series = n * n + 2 * n  
    if series > 99:    
        break
    print(series)      
    n += 1          
