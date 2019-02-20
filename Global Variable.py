"""
Python全域變數宣告規則
1.要先宣告變數
2.在函式中要使用其他函式中已宣告的變數，都要再設定global
"""
def function1():
  print(x)

def function2():  
  global x      # 在函式中若要使用global，global必須放在變數宣告之前
                # 在最外層宣告不需要加上global，因為在最外層預設的變數設定就是global
  x = 10        # 執行此行時才宣告x這個變數
  print(x)
  
def function3():
  x = x + 12
  print(x)

def function4():
  global x
  x = x + 12
  print(x)
  
print(x)        # 若先執行此行，會因為尚未宣告x所以ERROR

function1()     # 若先執行此行，會因為尚未宣告x所以ERROR

funtction2()    # 若先執行此行，因為已經將x設定為全域變數並且宣告了x，
                # 所以接下來都可以在程式任何地方找的到function2()裡面的x
                # 但是不可以使用
                
print(x)        # 已經宣告x所以可以正常print出x的值

function1()     # 已經宣告x所以可以正常print出x的值

function3()     # 雖然已經在function2宣告且設定為global了，但是也只是找的到不可以去使用他

function4()     # 在函式中需要再將x設定global才可以在這個函式中使用
