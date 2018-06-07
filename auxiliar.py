ser.write("AC.")
          a = "["
          if ser.read() == '[':
               while 1:
                    if ser.read() == ']':
                         break
                    a = a + ser.read()
                    print a + ']'
               a = a + ']'
               acce.config(text=a)

          ser.write("TP.")
          b = ""
          if ser.read() == '{':
               while 1 :
                    if ser.read() == '}':
                         break
                    b = b + ser.read()
                    print '{' + b + '}'
               b = b + 'º'
               temper.config(text=b)
          vent.after(100,todo)
