import subprocess
from testonedrivedown import baixarprogs, file_ids, path
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT
import concurrent.futures
#import time
import os
from art import *

# Titulo com ascii art
tprint("Instalador EPF",font="tarty1")

# Arrays com os programas
programas = ['1','2','3','4','5','6','7','8','9','10']

programas_selecionados=[]

programas_selecionados = input('\n Selecione os programas que quer instalar separados por espaço(Ex: 2 3 para Winrar e Java): \n \n 1- Adobe Reader \n 2- Winrar \n 3- Java \n 4- Google Chrome \n 5- Google Earth \n 6- Office 365 \n 7- Bitdefender \n 8- Openvpn \n 9- Teamviewer \n 10- Todos \n \n').split()
print(programas_selecionados)

# Func para instalar todos os programas
def instalartudo(codwinget):
 prog_run = subprocess.run(['winget', 'install', '-e' ,'-h', '--id', codwinget], stdout=subprocess.PIPE).stdout.decode('utf-8')
 return prog_run

instalar = []

# Func e info para caso nenhum programa seja selecionado
def erronenhumprograma():
  print("nenhum programa selecionado")

def pause():
    programPause = input("Script Terminado, pressione <ENTER> para terminar")

# Func para inserir os programas selecionados no array
def instalar_programas(programas_selecionados):
 instalar.clear()
 if not programas_selecionados:
   erronenhumprograma()
 if len(programas_selecionados) > 0:
  for programa in programas_selecionados:
   match programa:
    case '1':
       instalar.append('Adobe.Acrobat.Reader.64-bit')
    case '2':
       instalar.append('RARLab.WinRAR')
    case '3':
       instalar.append('Oracle.JavaRuntimeEnvironment')
    case '4':
      instalar.append('Google.Chrome')
    case '5':
      instalar.append('Google.EarthPro')
    case '6':
      office_install()
    case '7':
      bitdefender_install()
    case '8':
      openvpn_install()
    case '9':
      teamviewer_install()
    case '10':
       instalar.append('Adobe.Acrobat.Reader.64-bit')
       instalar.append('RARLab.WinRAR')
       instalar.append('Oracle.JavaRuntimeEnvironment')
       instalar.append('Google.Chrome')
       instalar.append('Google.EarthPro')
       office_install()
       bitdefender_install()
       openvpn_install()
       teamviewer_install()
    case _:
      print('Nenhum programa válido selecionado')

 # Instalar os programas com MultiThreading       
 if instalar:
 # print("Running threaded:")
 # threaded_start = time.time()
  with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for prog in instalar:
        futures.append(executor.submit(instalartudo, codwinget=prog))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
 # print("Threaded time:", time.time() - threaded_start)
  pause()

# Func para programas especificos - openvpn - baixar e instalar silently
def openvpn_install():
  file_ids.append('01JI7CLSXBVMLDGNNS3VBJME4R2S5DY6PI')
  baixarprogs(file_ids)
  os.chdir(path)
  openpvn_setup = subprocess.run(['openvpn-install-2.4.7-I607-Win10.exe', '/S'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
  print(openpvn_setup)
  pause()

# Func para programas especificos - teamviewer - baixar somente - instalar manualmente
def teamviewer_install():
 print('Baixando Teamviewer 11 Host')
 file_ids.append('01JI7CLSSL4HCKYSIYEBHIA5OTZHT3EXOZ')
 baixarprogs(file_ids)
 print('Teamviewer 11 Host instalado com sucesso')
 pause()

# Func para programas especificos - office 365 - baixar somente - instalar manualmente
def office_install():
  print ('Baixando Office 365')
  file_ids.append('01JI7CLSV43KDWB26UT5A32UIJER63GHQG')
  baixarprogs(file_ids)
  print('Office 365 baixado com sucesso')
  pause()

# Func para programas especificos - bitdefender - baixar somente - instalar manualmente
def bitdefender_install():
  print ('Baixando Bitdefender')
  file_ids.append('01JI7CLSVCHNKE4EJRLFBIP74WWWNQGBVF')
  file_ids.append('01JI7CLSVUT2PEFRFK3NG2XYQ457VVNJ3X')
  baixarprogs(file_ids)
  print('Bitdefender baixado com sucesso')
  pause()

instalar_programas(programas_selecionados)