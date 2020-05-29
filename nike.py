print ('---------- PIM SNEAKERS ----------\n\n')
a=[]
r=0
while True:
    b = input (' สินค้า [a]\n แสดง [s]\n ออกจากระบบ [x]\n ')
    b = b.lower()
    if b=='a': 
        print('Vans [v]\nNike [n]\nAdidas [ad]')
        c = input('\nChoose sneakers brand(กรอก): ')
        if c == 'v':
            print( "{:20} ".format("Model Vans"))
            print('[01] aclassic slip-on: 1990,\n[02] old skool : 2800,\n[03] chima pro: 2190')
            c = input('\nChoose Model sneakers (กรอกหมายเลข): ')
            if c=='01': #ถ้าผู้ใช้เลือกหมายเลข 01 
                a.append('Vans [slip-on]:3590:30%:2513')
                r+=2513
            elif c=='02':
                a.append('Vans [old skool]:5000:30%:3500')
                r+=3500
            elif c=='03':
                a.append('Vans [chima pro]:3000:30%:2100')
                r+=2100
            print('\n*****ข้อมูลได้เข้าระบบแล้ว******\n')
        elif c == 'n':
            print( "{:20} ".format("Model Nike"))
            print('[001] air max: 2300,\n[002] roshe one : 3200,\n[003] zoom fly: 4000') 
            c = input('\nChoose Model sneakers (กรอกหมายเลข): ')
            if c=='001':
                a.append('Nike [air max]:5800:20%:4690')
                r+=4690
            elif c=='002':
                a.append('Nike [roshe one]:4800:20%:3840')
                r+=3840
            elif c=='003':
                a.append('Nike [zoom fly]:6700:20%:5360')
                r+=5360
            print('\n*****ข้อมูลได้เข้าระบบแล้ว******\n')
            
        elif c == 'ad':
            print( "{:20} ".format("Model Adidas"))
            print('[011] superstar: 2400,\n[022] Stan Smith: 2000 ,\n[033] Gazelle :2250')
            c = input('\nChoose Model sneakers (กรอกหมายเลข): ')
            if c=='011':
                a.append('Adidas [superstar]:2400:50%:1200')
                r+=1200
            elif c=='022':
                a.append('Adidas [Stan Smith]:2000:50%:1000')
                r+=1000
            elif c=='033':
                a.append('Adidas [Gazelle] :2250:50%:1125')
                r+=1125
            print('\n*****ข้อมูลได้เข้าระบบแล้ว******\n')
    elif b=='s':
        print('{0:-<23}{0:-<10}{0:-<15}{0:-<10}'.format(""))
        print('{0:-<24}{1:-<9}{2:-<14}{3:10}'.format('รุ่น','ราคา','ส่วนลด','จ่ายจริง'))
        count=0
        for d in a:
            count+=1
            e=d.split(":")
            print(count,end=")")
            print('{0[0]:<20}{0[1]:<10}{0[2]:<12}{0[3]:10}'.format(e))
            continue
        print('รวมเป็นเงิน                                  ',r)
        print('{0:-<23}{0:-<10}{0:-<15}{0:-<10}'.format(""))
    elif b=='x':
        break
print('ทำคำสั่งต่อไป')


   