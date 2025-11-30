# 🟦 Tesseract Finance 💵

**Tesseract Finance** é uma aplicação desktop desenvolvida em **Python** utilizando a biblioteca **CustomTkinter**, projetada para gerenciar receitas e despesas de forma prática e segura.  
O projeto conta com uma interface moderna, tema dark, menu lateral interativo, exibição de horário em tempo real, histórico financeiro, gráficos e validação de entradas para garantir dados corretos.

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
- Botão para exibir Gráfico financeiro  
- Campos de entrada dinâmicos para receitas e despesas  

### 🔹 Área Principal:
- Exibe o último valor salvo  
- Caixa de histórico mostrando receitas e despesas  

### 🔹 Rodapé:
- Área reservada para logs e mensagens de validação  

---

## 🚀 Funcionalidades

### ✔️ Exibição de horário em tempo real
Atualiza automaticamente a cada 1 segundo usando `datetime.now()`.

### ✔️ Adicionar Receita / Despesa
Mostra um campo de input no menu lateral para digitar o valor da receita ou despesa.

### ✔️ Salvar Receita / Despesa
- O valor digitado é exibido na área principal.  
- Atualiza automaticamente o **saldo financeiro**, indicando lucro, prejuízo ou equilíbrio.  

### ✔️ Validação de entradas
- Garante que os valores sejam números positivos.  
- Garante que as descrições sejam textos válidos.  
- Mensagens de erro aparecem no log caso os dados estejam incorretos.  

### ✔️ Exibição de gráficos
- Mostra gráfico comparativo de **Receitas x Despesas** usando **matplotlib**.  

### ✔️ Interface moderna (Dark Mode)
- Utiliza **CustomTkinter** para uma aparência profissional e intuitiva.  

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- CustomTkinter (Interface)  
- Pillow (PIL) (Manipulação de imagens)  
- datetime (Hora ao vivo)  
- matplotlib (Gráficos)  
- unittest (Testes automatizados para validação de entradas)  

---

## 🧪 Testes Automatizados

O projeto inclui testes de validação de entradas com `unittest`.  
Para rodar os testes, execute:

```bash
python test_validacao.py