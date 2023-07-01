import subprocess
from tkinter import *
import customtkinter
#from PIL import Image
from testonedrivedown import baixarprogs, file_ids
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT
import os
import concurrent.futures
import time

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("green")

win = customtkinter.CTk()

w = 620
h = 550

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

win.geometry("%dx%d+%d+%d" % (w, h, x, y))
win.title('Instalador de Programas EPF')

#win.wm_iconbitmap(r'C:\Users\lucas.b\Desktop\instaladorepf\img\epf_logo.ico')
win.resizable(False, False)

frameessenciais = customtkinter.CTkFrame(master=win, width=600, height=300)
frameessenciais.grid(padx=10,pady=10,row=1,column=0)

frameespecificos = customtkinter.CTkFrame(master=win, width=600, height=300)
frameespecificos.grid(padx=10,pady=10, column=0, row=2, sticky=W)

framebotao = customtkinter.CTkFrame(master=win, width=600, height=200)
framebotao.grid(padx=10,pady=10)

#app_image = customtkinter.CTkImage(Image.open(r"C:\Users\lucas.b\Desktop\instaladorepf\img\epf_logo.png"), size=(108, 35))
#app_image_bt = customtkinter.CTkLabel(text="Instalador de \n Programas EPF",font=("Arial",18,"bold"),master=win,compound=LEFT)
#app_image_bt.grid(row=0,column=0, padx=30, sticky=W)

#func para dark/light mode
switch_var = customtkinter.StringVar(value="Dark")

def switch_event():
    if switch_var.get() == "Dark":
     customtkinter.set_appearance_mode("Light")
    else:
      customtkinter.set_appearance_mode("Dark")
switch_1 = customtkinter.CTkSwitch(master=win, text="Modo Dark/Light", command=switch_event,
                                   variable=switch_var, onvalue="Light", offvalue="Dark")
switch_1.grid(column=0, row=0, padx=30, pady=10, sticky=E)

#programas essenciais
titulo_programas_essenciais = customtkinter.CTkLabel(frameessenciais, text="Programas Essenciais")
titulo_programas_essenciais.grid(row=0, column=0, padx=5, pady=5)

#programas especificos
titulo_programas_especificos = customtkinter.CTkLabel(frameespecificos, text="Programas Específicos")
titulo_programas_especificos.grid(row=1, column=0, padx=5, pady=5)

#arrays com os programas
programas = ['Adobe Reader', 'Winrar','Java','Google Chrome','Google Earth','Office 365','Bitdefender','Openvpn','Teamviewer']
progs = [str(i) for i in range(len(programas))]
programas_selecionados=[]

#func para verificar os programas selecionados no checkbox
def seestaselecionado(programa, var):
  if var.get() == "off":
    try:
      programas_selecionados.remove(programa)
    except KeyError:
      pass
  else:
      programas_selecionados.append(programa)

# criando as checkbox      
for x in range(0,5):
    progs[x] = customtkinter.StringVar(value="off")
    l = customtkinter.CTkCheckBox(frameessenciais, text=programas[x], variable=progs[x],onvalue="on", offvalue="off",command=lambda x=programas[x],y=progs[x]:seestaselecionado(x,y))
    l.grid(padx=5, pady=5, row=1, column=x)

for x in range(5,9):
    progs[x] = customtkinter.StringVar(value="off")
    l2 = customtkinter.CTkCheckBox(frameespecificos, text=programas[x], variable=progs[x],onvalue="on", offvalue="off",command=lambda x=programas[x],y=progs[x]:seestaselecionado(x,y))
    l2.grid(padx=5, pady=5, row=2, column=x-5, sticky = W)

botaox = customtkinter.CTkButton(framebotao, text="Instalar Programas",width=600, command=lambda: [print(programas_selecionados),instalar_programas(programas_selecionados)], state=NORMAL).grid(row=7,column=1, padx=5, pady=5)
titulo_progress = customtkinter.CTkLabel(framebotao, text="Progresso de Instalação")
titulo_progress.grid(row=10, column=1, padx=5, pady=5)
progressbar = customtkinter.CTkProgressBar(framebotao, orientation="horizontal",width=600, height=20)
progressbar.grid(column=1)
progressbar.set(0)

textbox = customtkinter.CTkTextbox(framebotao, width=600, padx=10, pady=10)
textbox.grid(row=14,column=1)

#func para instalar todos os programas
def instalartudo(codwinget):
  #print(codwinget)
  # increment = 10 / len(programas_selecionados) / 10
  #titulo_progress.configure(text = 'Instalando Adobe Reader...')
  #titulo_progress.configure(text = codwinget)
  #textbox.insert("0.0","Instalando \n")
  #textbox.insert("0.0",codwinget)
  prog_run = subprocess.run(['winget', 'install', '-e' ,'-h', '--id', codwinget], stdout=subprocess.PIPE).stdout.decode('utf-8')
  return prog_run
  #titulo_progress.configure(text = "Não foi possivel instalar o")
  #titulo_progress.configure(text = codwinget)
  #textbox.insert("0.0","Não foi possivel instalar o", codwinget,".\n")
  #textbox.insert("0.0", prog_run)
  #progressbar.set(+increment)

instalar = []

#func para inserir os programas selecionados no array
def instalar_programas(programas_selecionados):
 instalar.clear()
 if not programas_selecionados:
   erronenhumprograma()
 if len(programas_selecionados) > 0:
   textbox.delete('1.0', END)
   print('tem programas selecionados')
   #botaox['state'] = DISABLED
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
      titulo_progress.configure('Nenhum programa válido selecionado')
      textbox.insert("0.0","Nenhum programa válido selecionado.\n")

 #instalar os programas com MultiThreading       
 print("Running threaded:")
 threaded_start = time.time()
 with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for prog in instalar:
        futures.append(executor.submit(instalartudo, codwinget=prog))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
        textbox.insert("0.0", future.result())
 print("Threaded time:", time.time() - threaded_start)

def openvpn_install():
  titulo_progress.configure(text = 'Instalando OpenVPN..')
  textbox.insert("0.0","Instalando OpenVPN...\n")
  openvpn_installer = file_ids.append('01JI7CLSXBVMLDGNNS3VBJME4R2S5DY6PI')
  baixarprogs(file_ids)
  caminhoopenvpn = os.getcwd()
  print(caminhoopenvpn)
  testee = subprocess.run(['openvpn-install-2.4.7-I607-Win10.exe', '/S'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
  textbox.insert("0.0", "Openvpn instalado com sucesso")


#func e info para caso nenhum programa seja selecionado
def erronenhumprograma():
  global pop

  w = 310
  h = 110

  screen_width = win.winfo_screenwidth()
  screen_height = win.winfo_screenheight()

  x = (screen_width/2) - (w/2)
  y = (screen_height/2) - (h/2)

  pop = customtkinter.CTkToplevel(win)
  pop.geometry("%dx%d+%d+%d" % (w, h, x, y))
  pop.title = ('Nenhum programa Selecionado')
  pop.resizable(False,False)
  pop.focus()
  
  pop_label = customtkinter.CTkLabel(pop,text='Você não escolheu nenhum programa para instalar')
  pop_label.grid(row=1, column=0, padx=10, pady=10)
  
  ok = customtkinter.CTkButton(pop,text='OK', command=lambda: pop.destroy())
  progressbar.set(0)
  ok.grid()

win.mainloop()