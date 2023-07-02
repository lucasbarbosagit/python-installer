import subprocess
from testonedrivedown import baixarprogs, file_ids
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT
import os
import concurrent.futures
import time
from art import *

tprint("Instalador EPF",font="tarty1")
#arrays com os programas
programas = ['Adobe Reader', 'Winrar','Java','Google Chrome','Google Earth','Office 365','Bitdefender','Openvpn','Teamviewer']

programas_selecionados=[]

programas_selecionados = input('Selecione os programas que quer instalar separados por espaço: \n Adobe Reader, Winrar, Java, Google Chrome, Google Earth, Office 365, Bitdefender, Openvpn, Teamviewer \n').split()
 
#func para instalar todos os programas
def instalartudo(codwinget):
 prog_run = subprocess.run(['winget', 'install', '-e' ,'-h', '--id', codwinget], stdout=subprocess.PIPE).stdout.decode('utf-8')
 return prog_run

instalar = []

#func e info para caso nenhum programa seja selecionado
def erronenhumprograma():
  print("nenhum programa selecionado")

#func para inserir os programas selecionados no array
def instalar_programas(programas_selecionados):
 instalar.clear()
 if not programas_selecionados:
   erronenhumprograma()
 if len(programas_selecionados) > 0:
  for programa in programas_selecionados:
   match programa:
    case 'Adobe Reader':
       instalar.append('Adobe.Acrobat.Reader.64-bit')
    case 'Winrar':
       instalar.append('RARLab.WinRAR')
    case 'Java':
       instalar.append('Oracle.JavaRuntimeEnvironment')
    case 'Google Chrome':
      instalar.append('Google.Chrome')
    case 'Google Earth':
      instalar.append('Google.EarthPro')
    case 'Openvpn':
      openvpn_install()
    case _:
      print('Nenhum programa válido selecionado')

 #instalar os programas com MultiThreading       
 print("Running threaded:")
 threaded_start = time.time()
 with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for prog in instalar:
        futures.append(executor.submit(instalartudo, codwinget=prog))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
 print("Threaded time:", time.time() - threaded_start)

def openvpn_install():
  openvpn_installer = file_ids.append('01JI7CLSXBVMLDGNNS3VBJME4R2S5DY6PI')
  baixarprogs(file_ids)
  caminhoopenvpn = os.getcwd()
  print(caminhoopenvpn)
  testee = subprocess.run(['openvpn-install-2.4.7-I607-Win10.exe', '/S'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')

instalar_programas(programas_selecionados) 

