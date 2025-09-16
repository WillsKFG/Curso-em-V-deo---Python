import customtkinter as ctk

# Inicialização do app
ctk.set_appearance_mode("System")  # "Dark", "Light", "System"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Flashcards - Federalismo no Brasil")
app.geometry("600x400")

# Lista de flashcards
flashcards = [
    {
        "pergunta": "1. Quais são os quatro temas principais que organizam o texto?",
        "resposta": "• Gênese do federalismo no Brasil\n• Federalismo e representação política\n• Federalismo e governabilidade\n• Federalismo e políticas públicas"
    },
    {
        "pergunta": "2. O que a autora entende por 'campo em formação' no estudo do federalismo brasileiro?",
        "resposta": "Falta consolidação teórica e empírica, com pouca integração com a literatura internacional."
    },
    {
        "pergunta": "3. Como a gênese do federalismo brasileiro é caracterizada?",
        "resposta": "Adotado de cima para baixo pelas elites, sem pressão regional, com descentralização assimétrica."
    },
    {
        "pergunta": "4. Qual a relação entre federalismo e governabilidade?",
        "resposta": "Cria múltiplos centros de poder e dificulta coordenação nacional. A Constituição de 1988 intensificou isso."
    },
    {
        "pergunta": "5. Cite uma limitação conceitual e uma metodológica mencionadas no texto.",
        "resposta": "• Conceitual: Definições amplas de federalismo\n• Metodológica: Falta de dados sistematizados"
    },
    {
        "pergunta": "6. Por que a falta de fundamentação empírica enfraquece as hipóteses?",
        "resposta": "Sem dados concretos, as hipóteses são frágeis e difíceis de validar."
    },
    {
        "pergunta": "7. Como representação política se relaciona com políticas públicas?",
        "resposta": "A forma de representação afeta alocação de recursos e prioridades públicas."
    },
    {
        "pergunta": "8. Como centralização e descentralização se relacionam com o papel da União pós-1988?",
        "resposta": "A União mantém controle sobre políticas sociais mesmo após maior autonomia formal de estados e municípios."
    },
    {
        "pergunta": "9. As Constituições de 1967 e 1988 mudaram o pacto federativo?",
        "resposta": "• Sim: A de 1988 ampliou a autonomia local\n• Não totalmente: Centralização de receitas e controle federal continua"
    },
    {
        "pergunta": "10. Quais indicadores ajudam a avaliar se autonomia local fortalece ou enfraquece a democracia?",
        "resposta": "Participação política, qualidade da gestão, corrupção, efetividade de políticas, desigualdade intermunicipal."
    }
]

index = 0

# Funções
def mostrar_pergunta():
    pergunta_label.configure(text=flashcards[index]["pergunta"])
    resposta_label.configure(text="")

def mostrar_resposta():
    resposta_label.configure(text=flashcards[index]["resposta"])

def proxima_pergunta():
    global index
    if index < len(flashcards) - 1:
        index += 1
        mostrar_pergunta()
    else:
        pergunta_label.configure(text="Fim dos flashcards!")
        resposta_label.configure(text="Você revisou todas as perguntas.")

# Interface
pergunta_label = ctk.CTkLabel(app, text="", wraplength=550, font=ctk.CTkFont(size=16, weight="bold"), justify="left")
pergunta_label.pack(pady=20)

resposta_label = ctk.CTkLabel(app, text="", wraplength=550, font=ctk.CTkFont(size=14), justify="left")
resposta_label.pack(pady=10)

botoes_frame = ctk.CTkFrame(app)
botoes_frame.pack(pady=20)

mostrar_button = ctk.CTkButton(botoes_frame, text="Mostrar Resposta", command=mostrar_resposta)
mostrar_button.grid(row=0, column=0, padx=10)

proximo_button = ctk.CTkButton(botoes_frame, text="Próxima Pergunta", command=proxima_pergunta)
proximo_button.grid(row=0, column=1, padx=10)

mostrar_pergunta()
app.mainloop()
