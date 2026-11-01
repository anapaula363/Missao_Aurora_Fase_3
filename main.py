import customtkinter as ctk

ctk.set_appearance_mode("dark") 
janela = ctk.CTk() 
janela. title("Missao Aurora - fase 3")
janela.geometry("800x600")

titulo = ctk.CTkLabel(
    janela,
    text="MISSAO AURORA - COLONIA EM MARTE",
    
)

titulo.pack(pady=30)  

ctk.CTkLabel(janela, text="Energia inicial").pack()
entrada_energia = ctk.CTkEntry(janela)
entrada_energia.pack(pady=10)
resultado = ctk.CTkLabel(janela, text="")
ctk.CTkLabel(janela, text="Consumo").pack()
entrada_consumo = ctk.CTkEntry(janela)
entrada_consumo.pack(pady=5)
ctk.CTkLabel(janela, text="Recarga").pack()
entrada_recarga = ctk.CTkEntry(janela)
entrada_recarga.pack(pady=5)
resultado.pack(pady=10)
def verificar_energia():
    try:
      energia = float(entrada_energia.get())
      consumo = float(entrada_consumo.get())
      recarga = float(entrada_recarga.get())
      energia_Final = energia - consumo + recarga
      if energia_Final >= 80:
        resultado.configure(text=f"energia final: {energia_Final} - colonia funcionando")
      else:
       resultado.configure(text=f"energia final: {energia_Final} - Pouso abortado: pouca energia")
    except ValueError:
       resultado.configure(text="Erro: digite apenas numeros")
resultado.pack(pady=10)

botao = ctk.CTkButton(                                    
    janela,
    text="Verificar energia",
    command= verificar_energia,
)    
botao.pack(pady=10)
janela.mainloop()




