# 📘 Tesseract Finance

**Tesseract Finance** é uma aplicação desktop simples desenvolvida em **Python** utilizando a biblioteca **CustomTkinter**, projetada para gerenciar receitas e despesas de forma prática.  
O projeto conta com uma interface moderna, tema dark, menu lateral interativo, exibição de horário em tempo real e espaço reservado para futuras funcionalidades como histórico financeiro e dashboards.

---

## 📸 Interface

A interface é composta por:

### 🔹 Topo:
- Barra azul com título  
- Ícone  
- Relógio em tempo real  

### 🔹 Menu Lateral:
- Botões de adicionar e salvar Receita  
- Botões de adicionar e salvar Despesa  
- Campos de entrada dinâmicos  

### 🔹 Área Principal:
- Exibe o último valor salvo  

### 🔹 Rodapé:
- Área reservada para logs e histórico  

---

## 🚀 Funcionalidades

### ✔️ Exibição de horário em tempo real
Atualiza automaticamente a cada 1 segundo usando `datetime.now()`.

### ✔️ Adicionar Receita
Mostra um campo de input no menu lateral para digitar o valor da receita.

### ✔️ Salvar Receita
O valor digitado é exibido na área principal.

### ✔️ Adicionar Despesa
Mostra um campo de input no menu lateral para digitar o valor da despesa.

### ✔️ Salvar Despesa
O valor digitado também é exibido na área principal.

### ✔️ Interface moderna (Dark Mode)
Utiliza **CustomTkinter** para uma aparência mais profissional.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- CustomTkinter  
- Pillow (PIL)  
- datetime  

---

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/E-Danillo/Tesseract-Controle-Financeiro.git

2.  **Instale as Dependências:**
     ```bash
     pip install customtkinter pillow

3. **Rode o projeto:**
   ```bash
   principal.py
