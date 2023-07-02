import subprocess
from testonedrivedown import baixarprogs, file_ids
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT
import os
import concurrent.futures
import time
from art import *

#titulo com ascii art
tprint("Instalador EPF",font="tarty1")

#arrays com os programas
programas = ['1','2','3','4','5','6','7','8','9']

programas_selecionados=[]

programas_selecionados = input('Selecione os programas que quer instalar separados por espaço: \n Adobe Reader, Winrar, Java, Google Chrome, Google Earth, Office 365, Bitdefender, Openvpn, Teamviewer \n').split()
print(programas_selecionados)

#func para instalar todos os programas
def instalartudo(codwinget):
 prog_run = subprocess.run(['winget', 'install', '-e' ,'-h', '--id', codwinget], stdout=subprocess.PIPE).stdout.decode('utf-8')
 return prog_run

instalar = []

#func e info para caso nenhum programa seja selecionado
def erronenhumprograma():
  print("nenhum programa selecionado")

def pause():
    programPause = input("Script Terminado, pressione <ENTER> para terminar")

#func para inserir os programas selecionados no array
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
    case '8':
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
 pause()

#func para programas especificos - openvpn - baixar e instalar silently
def openvpn_install():
  file_ids.append('01JI7CLSXBVMLDGNNS3VBJME4R2S5DY6PI')
  baixarprogs(file_ids)
  openpvn_setup = subprocess.run(['openvpn-install-2.4.7-I607-Win10.exe', '/S'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
  print(openpvn_setup)

#func para programas especificos - teamviewer - baixar somente - instalar manualmente
def teamviewer_install():
 print('not defined')

#func para programas especificos - office 365 - baixar somente - instalar manualmente
def office_install():
  print('not defined')

#func para programas especificos - bitdefender - baixar somente - instalar manualmente
def bitdefender_install():
  print('not defined')

instalar_programas(programas_selecionados)