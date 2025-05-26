import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import random

def popular_dados_ficticios():
    # Limpar dados existentes
    st.session_state['produtos'] = {}
    st.session_state['vendas'] = pd.DataFrame(columns=['Produto', 'Data', 'Quantidade', 'Preco_Venda', 'Comissao_iFood'])
    
    # Produtos fictícios com ingredientes
    produtos = {
        'Batata Frango Cremoso': pd.DataFrame({
            'Ingrediente': ['Batata', 'Frango', 'Creme de Leite', 'Queijo Mussarela'],
            'Custo do kg (R$)': [6.00, 15.00, 8.00, 25.00],
            'Gramas por unidade': [250, 150, 100, 80]
        }),
        'Batata Bacon Crocante': pd.DataFrame({
            'Ingrediente': ['Batata', 'Bacon', 'Queijo Cheddar', 'Cebola Crocante'],
            'Custo do kg (R$)': [6.00, 30.00, 28.00, 10.00],
            'Gramas por unidade': [250, 100, 80, 30]
        }),
        'Batata Vegetariana': pd.DataFrame({
            'Ingrediente': ['Batata', 'Brócolis', 'Cenoura', 'Queijo Parmesão'],
            'Custo do kg (R$)': [6.00, 12.00, 5.00, 35.00],
            'Gramas por unidade': [250, 100, 80, 50]
        }),
        'Batata Camarão ao Coco': pd.DataFrame({
            'Ingrediente': ['Batata', 'Camarão', 'Leite de Coco', 'Queijo Mussarela'],
            'Custo do kg (R$)': [6.00, 80.00, 15.00, 25.00],
            'Gramas por unidade': [250, 120, 100, 80]
        }),
        'Batata Carne Seca': pd.DataFrame({
            'Ingrediente': ['Batata', 'Carne Seca', 'Requeijão', 'Cebola'],
            'Custo do kg (R$)': [6.00, 40.00, 20.00, 8.00],
            'Gramas por unidade': [250, 150, 100, 50]
        }),
        'Batata Quatro Queijos': pd.DataFrame({
            'Ingrediente': ['Batata', 'Queijo Mussarela', 'Queijo Parmesão', 'Queijo Gorgonzola', 'Queijo Cheddar'],
            'Custo do kg (R$)': [6.00, 25.00, 35.00, 50.00, 28.00],
            'Gramas por unidade': [250, 80, 50, 40, 60]
        }),
        'Batata Strogonoff': pd.DataFrame({
            'Ingrediente': ['Batata', 'Carne Bovina', 'Creme de Leite', 'Molho de Tomate'],
            'Custo do kg (R$)': [6.00, 30.00, 8.00, 6.00],
            'Gramas por unidade': [250, 150, 100, 80]
        })
    }
    
    # Adicionar produtos ao session_state
    st.session_state['produtos'] = produtos
    
    # Gerar vendas fictícias para os últimos 30 dias
    data_inicio = datetime.now() - timedelta(days=30)
    vendas_list = []
    for i in range(30):
        data_venda = data_inicio + timedelta(days=i)
        for produto in produtos.keys():
            # Quantidade vendida aleatória entre 0 e 10 por dia
            quantidade = random.randint(0, 10)
            if quantidade > 0:
                vendas_list.append({
                    'Produto': produto,
                    'Data': data_venda.date(),
                    'Quantidade': quantidade,
                    'Preco_Venda': round(random.uniform(20.0, 35.0), 2),
                    'Comissao_iFood': 15.2
                })
    
    # Adicionar vendas ao session_state
    st.session_state['vendas'] = pd.DataFrame(vendas_list)
    
    return f"Dados fictícios adicionados com sucesso! {len(produtos)} produtos e {len(vendas_list)} vendas registradas."
