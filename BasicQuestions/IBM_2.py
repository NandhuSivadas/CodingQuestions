def processQueries(queries, k):
 
    P = list(range(1, k + 1))
    result = []

   
    for q in queries:
        pos = P.index(q)          
        result.append(pos)       
        P.pop(pos)               
        P.insert(0, q)            
    
    return result


queries = [3, 1, 2, 1]
k = 5
print(processQueries(queries, k))  
