import matplotlib.pyplot as plt
import csv

# Índice 19 se estão no berçario
# Índice 21 se tem internet

nursery = []
internet = []

with open("student-mat.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    for coluna in leitor:
        nursery.insert(len(nursery), coluna[19])
        internet.insert(len(internet), coluna[21])
        
nursery.pop(0)
internet.pop(0)

tam = [0, 0, 0, 0]

if len(nursery) == len(internet):
    for n, s in zip(nursery, internet):
        if (n == "yes") and (s == "yes"):
            tam[0] = tam[0] + 1
        elif (n == "yes") and (s == "no"):
            tam[1] = tam[1] + 1
        elif (n == "no") and (s == "yes"):
            tam[2] = tam[2] + 1
        elif (n == "no") and (s == "no"):
            tam[3] = tam[3] + 1

else:
    print("O número de elementos são distintos entre os índices")
    exit()

activities = [
                'Está no berçario e usa internet', 
                'Está no berçario e não usa internet', 
                'Não está no berçario e usa internet', 
                'Não está no berçario e não usa internet'
            ] 

slices = [tam[0], tam[1], tam[2], tam[3]]
  
colors = ['r', 'b', 'g', 'y'] 
  
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
  
plt.legend() 
  
plt.show()