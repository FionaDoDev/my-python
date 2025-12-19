from basic2 import multiplication

def test_multiplication():
    x=3
    y=5
    resMult=multiplication(x,y)
    #print("multiplication(3,5)=" + str(resMult))
    #print("multiplication(3,5)=" , resMult)
    print(f'multiplication avec x={x} et y={y} le res vaut {resMult}')
    assert resMult == 15
   
# nb: lancement du test via la commande:
#     pytest test_basic2.py   
