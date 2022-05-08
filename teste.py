intervalo = (1263,1705)
alcance = intervalo[1] - intervalo[0]
dados_completos = []

trecho = 90

for i in range(intervalo[0],intervalo[1],trecho):
    fim = i+trecho-1
    if fim > intervalo[1]: inter_gerado = (i,intervalo[1])
    else: inter_gerado = (i,fim)
    print(inter_gerado)