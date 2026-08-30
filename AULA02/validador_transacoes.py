trancasoes = [150.0, 3200.5, 12500.0, 450.0, -50.0, 800.0, 0]
for valor in trancasoes:
    if valor>10000.0:
        print("[ALERTA] transação suspeita de R$",valor," Encaminhada para auditoria")
        continue
    if valor <=0:
        print("[ERRO CRITICO] Transação Invalidada encontrada R$",valor,"interrompendo Bot . . .")
        break
    else :
        print("[SUCESSO] Transação de R$",valor,"Processada")
    