import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Calculadora de Lucro por Batata', page_icon='🥔', layout='wide')

# ---------- Custom modern CSS ----------
def apply_theme(theme):
    if theme == 'Escuro':
        st.markdown(
            '''
            <style>
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(to right, #2c3e50, #3498db);
                color: #f1f1f1;
            }
            .stApp {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }
            /* Glassy cards for metrics */
            div[data-testid="stMetric"] {
                background: rgba(255, 255, 255, 0.15);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(5px);
                color: #ffffff;
            }
            /* Data editor rounded corners and modern styling */
            div[data-testid="stDataFrame"] > div {
                border-radius: 12px;
                overflow: hidden;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.15);
            }
            /* Input fields styling */
            .stNumberInput input {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: #ffffff;
                border-radius: 8px;
                padding: 10px;
            }
            /* Buttons */
            .stButton > button {
                background-color: #3498db;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: 600;
                transition: all 0.3s ease;
                border: none;
            }
            .stButton > button:hover {
                background-color: #2980b9;
                box-shadow: 0 0 10px rgba(52, 152, 219, 0.5);
            }
            /* Title and headers */
            h1, h2, h3 {
                color: #ffffff;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            }
            .sidebar .sidebar-content {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
            }
            </style>
            ''',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '''
            <style>
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(to right, #f1f2f6, #dfe4ea);
                color: #2c3e50;
            }
            .stApp {
                background: rgba(255, 255, 255, 0.8);
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }
            /* Glassy cards for metrics */
            div[data-testid="stMetric"] {
                background: rgba(255, 255, 255, 0.5);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(5px);
                color: #2c3e50;
            }
            /* Data editor rounded corners and modern styling */
            div[data-testid="stDataFrame"] > div {
                border-radius: 12px;
                overflow: hidden;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.15);
            }
            /* Input fields styling */
            .stNumberInput input {
                background: rgba(255, 255, 255, 0.5);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: #2c3e50;
                border-radius: 8px;
                padding: 10px;
            }
            /* Buttons */
            .stButton > button {
                background-color: #3498db;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: 600;
                transition: all 0.3s ease;
                border: none;
            }
            .stButton > button:hover {
                background-color: #2980b9;
                box-shadow: 0 0 10px rgba(52, 152, 219, 0.5);
            }
            /* Title and headers */
            h1, h2, h3 {
                color: #2c3e50;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            }
            .sidebar .sidebar-content {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
            }
            </style>
            ''',
            unsafe_allow_html=True
        )

# Função para inicializar os dados dos produtos
if 'produtos' not in st.session_state:
    st.session_state['produtos'] = {}

# Função para inicializar os dados de vendas
if 'vendas' not in st.session_state:
    st.session_state['vendas'] = pd.DataFrame(columns=['Produto', 'Data', 'Quantidade', 'Preco_Venda', 'Comissao_iFood'])

# Função para calcular lucro de um produto
def calcular_lucro_produto(dados_produto, sale_price, ifood_fee):
    if not dados_produto.empty:
        dados_produto['Custo por grama (R$)'] = (dados_produto['Custo do kg (R$)'] / 1000).round(3)
        dados_produto['Custo por unidade (R$)'] = (dados_produto['Custo por grama (R$)'] * dados_produto['Gramas por unidade']).round(2)
        total_cost = dados_produto['Custo por unidade (R$)'].sum()
        net_revenue = sale_price * (1 - ifood_fee / 100)
        profit = net_revenue - total_cost
        profit_percentage = (profit / net_revenue * 100) if net_revenue > 0 else 0
        dados_produto['Porcentagem do Custo (%)'] = (dados_produto['Custo por unidade (R$)'] / total_cost * 100).round(1) if total_cost > 0 else 0
        return total_cost, net_revenue, profit, profit_percentage, dados_produto
    return 0, 0, 0, 0, dados_produto

# Sidebar para navegação e configurações
with st.sidebar:
    st.image('https://via.placeholder.com/150x80?text=Batata+Logo', use_container_width=True)
    st.header('Configurações')
    theme_choice = st.radio('Tema', ['Escuro', 'Claro'])
    apply_theme(theme_choice)
    
    st.header('Navegação')
    pagina = st.radio('Selecione a Página', ['Painel Geral', 'Calculadora de Lucro', 'Adicionar Produto'])
    
    # Adicionando botão para popular dados fictícios
    st.header('Dados de Demonstração')
    try:
        from dados_ficticios import popular_dados_ficticios
        if st.button('Popular com Dados Fictícios'):
            resultado = popular_dados_ficticios()
            st.success(resultado)
            st.rerun()
    except ImportError:
        st.warning('Arquivo de dados fictícios não encontrado.')

st.title('🥔 Sistema de Gestão · Batatas Recheadas')

# Navegação entre páginas
if pagina == 'Painel Geral':
    st.markdown('''Visualize as estatísticas gerais da sua loja.''')
    
    st.subheader('Estatísticas Gerais')
    if not st.session_state['vendas'].empty:
        total_vendas = st.session_state['vendas']['Quantidade'].sum()
        receita_total = (st.session_state['vendas']['Preco_Venda'] * st.session_state['vendas']['Quantidade']).sum()
        comissao_total = ((st.session_state['vendas']['Preco_Venda'] * st.session_state['vendas']['Comissao_iFood'] / 100) * st.session_state['vendas']['Quantidade']).sum()
        custo_total = 0
        lucro_total = 0
        
        for _, venda in st.session_state['vendas'].iterrows():
            produto = venda['Produto']
            if produto in st.session_state['produtos']:
                dados_produto = st.session_state['produtos'][produto]
                total_cost, _, profit, _, _ = calcular_lucro_produto(dados_produto, venda['Preco_Venda'], venda['Comissao_iFood'])
                custo_total += total_cost * venda['Quantidade']
                lucro_total += profit * venda['Quantidade']
        
        col1, col2, col3, col4 = st.columns(4, gap='medium')
        col1.metric('Total de Vendas', f'{total_vendas}', delta=None, delta_color='off')
        col2.metric('Receita Total', f'R$ {receita_total:.2f}', delta=None, delta_color='off')
        col3.metric('Custo Total', f'R$ {custo_total:.2f}', delta=None, delta_color='off')
        col4.metric('Lucro Total', f'R$ {lucro_total:.2f}', delta=None, delta_color='off')
        
        st.subheader('Detalhes das Vendas')
        st.dataframe(st.session_state['vendas'], use_container_width=True, hide_index=True)
        
        st.subheader('Produtos Mais Vendidos')
        vendas_por_produto = st.session_state['vendas'].groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).reset_index()
        fig1 = px.bar(vendas_por_produto, x='Produto', y='Quantidade', color='Produto',
                      title='Quantidade Vendida por Produto',
                      labels={'Quantidade': 'Unidades Vendidas', 'Produto': 'Produto'},
                      template='plotly_dark' if theme_choice == 'Escuro' else 'plotly_white')
        fig1.update_layout(showlegend=False, title_x=0.5, title_font_size=20)
        st.plotly_chart(fig1, use_container_width=True)
        
        st.subheader('Receita por Produto')
        receita_por_produto = st.session_state['vendas'].groupby('Produto').apply(lambda x: (x['Preco_Venda'] * x['Quantidade']).sum()).sort_values(ascending=False).reset_index(name='Receita')
        fig2 = px.pie(receita_por_produto, values='Receita', names='Produto',
                      title='Distribuição da Receita por Produto',
                      template='plotly_dark' if theme_choice == 'Escuro' else 'plotly_white')
        fig2.update_layout(title_x=0.5, title_font_size=20)
        st.plotly_chart(fig2, use_container_width=True)
        
        st.subheader('Vendas ao Longo do Tempo')
        vendas_por_data = st.session_state['vendas'].groupby('Data')['Quantidade'].sum().reset_index()
        fig3 = px.line(vendas_por_data, x='Data', y='Quantidade',
                       title='Vendas por Data',
                       labels={'Quantidade': 'Unidades Vendidas', 'Data': 'Data'},
                       template='plotly_dark' if theme_choice == 'Escuro' else 'plotly_white')
        fig3.update_layout(title_x=0.5, title_font_size=20)
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info('Nenhuma venda registrada. Registre vendas na página "Calculadora de Lucro" para ver as estatísticas.')

elif pagina == 'Calculadora de Lucro':
    st.markdown('''Preencha os dados de venda e visualize o lucro de cada produto cadastrado.''')
    
    # Parâmetros de venda globais
    with st.container():
        st.subheader('Parâmetros de Venda')
        col1, col2 = st.columns(2, gap='medium')
        with col1:
            sale_price = st.number_input('Preço de venda no iFood (R$)', min_value=0.01, value=25.0, step=0.5, format='%.2f', key='sale_price_global')
        with col2:
            ifood_fee = st.number_input('Percentual de comissão do iFood (%)', min_value=0.0, max_value=100.0, value=15.2, step=0.1, format='%.1f', key='ifood_fee_global')
    
    st.divider()
    
    # Registro de vendas
    st.subheader('Registro de Venda')
    if st.session_state['produtos']:
        produto_selecionado = st.selectbox('Selecione o Produto Vendido', list(st.session_state['produtos'].keys()))
        quantidade_vendida = st.number_input('Quantidade Vendida', min_value=1, value=1, step=1)
        data_venda = st.date_input('Data da Venda')
        if st.button('Registrar Venda'):
            nova_venda = pd.DataFrame({
                'Produto': [produto_selecionado],
                'Data': [data_venda],
                'Quantidade': [quantidade_vendida],
                'Preco_Venda': [sale_price],
                'Comissao_iFood': [ifood_fee]
            })
            st.session_state['vendas'] = pd.concat([st.session_state['vendas'], nova_venda], ignore_index=True)
            st.success(f'Venda de {quantidade_vendida} {produto_selecionado} registrada com sucesso!')
            st.rerun()
    else:
        st.info('Nenhum produto cadastrado. Vá para a página "Adicionar Produto" para incluir novos produtos.')
    
    st.divider()
    
    # Exibir resultados para cada produto
    st.subheader('Resultados por Produto')
    if st.session_state['produtos']:
        for nome_produto, dados in st.session_state['produtos'].items():
            st.markdown(f'### {nome_produto}')
            total_cost, net_revenue, profit, profit_percentage, dados_calculados = calcular_lucro_produto(dados, sale_price, ifood_fee)
            col1, col2, col3, col4 = st.columns(4, gap='medium')
            col1.metric('Custo Total', f'R$ {total_cost:.2f}', delta=None, delta_color='off')
            col2.metric('Receita Líquida', f'R$ {net_revenue:.2f}', delta=None, delta_color='off')
            col3.metric('Lucro', f'R$ {profit:.2f}', delta=None, delta_color='off')
            col4.metric('Porcentagem de Lucro', f'{profit_percentage:.1f}%', delta=None, delta_color='off')
            with st.expander(f'Detalhamento dos Custos - {nome_produto}'):
                st.dataframe(dados_calculados, use_container_width=True, hide_index=True)
            st.divider()
    else:
        st.info('Nenhum produto cadastrado. Vá para a página "Adicionar Produto" para incluir novos produtos.')

elif pagina == 'Adicionar Produto':
    st.markdown('''Adicione novos produtos e detalhe os ingredientes utilizados para calcular o custo de produção.''')
    
    # Formulário para adicionar novo produto
    with st.container():
        st.subheader('Novo Produto')
        nome_produto = st.text_input('Nome do Produto', placeholder='Ex: Batata Recheada com Frango')
        
        # Dados iniciais do produto
        sample_data = pd.DataFrame({
            'Ingrediente': ['Batata'],
            'Custo do kg (R$)': [6.00],
            'Gramas por unidade': [250]
        })
        
        edited = st.data_editor(
            sample_data,
            num_rows='dynamic',
            use_container_width=True,
            key=f'ingredientes_editor_{nome_produto}',
            column_config={
                'Ingrediente': st.column_config.TextColumn('Nome do Ingrediente'),
                'Custo do kg (R$)': st.column_config.NumberColumn('Custo por Kg (R$)', format='%.2f'),
                'Gramas por unidade': st.column_config.NumberColumn('Gramas por Unidade')
            }
        )
        
        if st.button('Adicionar Produto') and nome_produto:
            st.session_state['produtos'][nome_produto] = edited
            st.success(f'Produto "{nome_produto}" adicionado com sucesso!')
            st.rerun()
        elif not nome_produto:
            st.warning('Por favor, insira um nome para o produto antes de adicionar.')
    
    st.divider()
    
    # Lista de produtos salvos com opção de editar ou excluir
    st.subheader('Produtos Cadastrados')
    if st.session_state['produtos']:
        for nome_produto, dados in list(st.session_state['produtos'].items()):
            with st.expander(f'Editar/Excluir - {nome_produto}'):
                edited_data = st.data_editor(
                    dados,
                    num_rows='dynamic',
                    use_container_width=True,
                    key=f'editor_{nome_produto}',
                    column_config={
                        'Ingrediente': st.column_config.TextColumn('Nome do Ingrediente'),
                        'Custo do kg (R$)': st.column_config.NumberColumn('Custo por Kg (R$)', format='%.2f'),
                        'Gramas por unidade': st.column_config.NumberColumn('Gramas por Unidade')
                    }
                )
                col1, col2 = st.columns(2)
                with col1:
                    if st.button('Atualizar Dados', key=f'update_{nome_produto}'):
                        st.session_state['produtos'][nome_produto] = edited_data
                        st.success(f'Dados de "{nome_produto}" atualizados!')
                        st.rerun()
                with col2:
                    if st.button('Excluir Produto', key=f'delete_{nome_produto}'):
                        del st.session_state['produtos'][nome_produto]
                        st.success(f'Produto "{nome_produto}" excluído!')
                        st.rerun()
    else:
        st.info('Nenhum produto cadastrado ainda.')

# Footer
st.markdown('---')
st.markdown('<p style="text-align: center; color: rgba(255,255,255,0.6);">Desenvolvido com 🥔 por Potato Sistema</p>', unsafe_allow_html=True)
