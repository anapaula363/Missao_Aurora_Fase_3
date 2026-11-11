import customtkinter as ctk

colonia = {
  "energia": {
  "solar": 50,
  "eolica": 30

  },
  "sistemas":{
    "suporte_vida": "essencial",
    "laboratorio": "secundario",
    "comunicacao": "importante"
  }

}

def verificar_prioridade(energia):
  if energia < 50:
    return "ALERTA: energia baixar! Priorizar suporte de vida."
  else:
    return "Energia suficiente. Manter sistemas funcionando."

vento = [8,10, 12]
energia_gerada = [20,25,30]

def prever_energia(velocidade_vento):
    n = len(vento)
    media_vento = sum(vento) / n
    media_energia = sum(energia_gerada) / n
    numerador = 0
    denominador = 0
    for i in range(n):
      numerador += (vento[i] - media_vento) * (energia_gerada[i] - media_energia)
      denominador += (vento[i] - media_vento) ** 2
    coeficiente = numerador / denominador
    intercepto = media_energia - coeficiente * media_vento
    previsao = coeficiente * velocidade_vento + intercepto
    return previsao  
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
ctk.CTkLabel(janela, text="velocidade de vento").pack()
entrada_vento = ctk.CTkEntry(janela) 
entrada_vento.pack(pady=5) 

def verificar_energia():
    try:
      energia = float(entrada_energia.get())
      consumo = float(entrada_consumo.get())
      recarga = float(entrada_recarga.get())
      velocidade_vento = float(entrada_vento.get())
      previsao_vento = prever_energia(velocidade_vento)
      energia_final = energia - consumo + recarga
      prioridade = verificar_prioridade(energia_final)
      mensagem_previsao = f"\nPrevisao de energia pelo vento: {previsao_vento:.2f}"
      if energia_final >= 80:
        resultado.configure(text=f"Energia final: {energia_final}\n{prioridade} Colônia funcionando{mensagem_previsao}")
      else:
       resultado.configure(text=f"Energia final: {energia_final}\nPouso abordado: pouca energial" + mensagem_previsao)
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




