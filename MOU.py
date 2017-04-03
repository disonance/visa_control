import visa
import time

rm = visa.ResourceManager()
resources = rm.list_resources()
resource_name = []
psu_idx = 0
voltage = 0
print resources

voltage = float(raw_input("Voltage Input:"))
output = raw_input("on||off\r\n")
if voltage > 4.6:
    voltage = 4.6
    print ("Voltage selected too high. Capped to 4.6")

for x in range(0,len(resources)):

    try:
        id = rm.open_resource(resources[x])
        resource_name.append(id.query('*idn?'))
        if (id.query('*idn?').find("E3631A") != -1):
            psu_idx = x
            print ('psu found at index %d' % x)
        id.close()
    except:
        continue


print resource_name

# for x in range(0,len(resource_name)):
#     # print resource_name[x]
#     if(resource_name[x].find("E3631A") != -1):
#         psu_idx = x
#         print ('psu found at index %d' % x)


psu = rm.open_resource(resources[psu_idx])
# time.sleep(2)
# print (psu.query('*IDN?'))
if output == 'on':
    psu.write('outp off')
    psu.write('volt %f' % voltage)
    psu.write('outp on')
    print("PSU ON @ %f" % voltage)
else:
    psu.write('outp off')
    print ("PSU OFF")

psu.close()
