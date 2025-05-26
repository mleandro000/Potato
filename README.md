# 🥔 Sistema de Gestão - Batatas Recheadas

Um sistema completo de gestão financeira desenvolvido especialmente para pequenos empreendedores do ramo alimentício. Esta solução nasceu da necessidade real de ajudar minha sogra a contabilizar suas vendas de batatas recheadas no iFood e visualizar estatísticas importantes para o crescimento do negócio.

Desenvolvido em Python com Streamlit, oferece controle detalhado de custos, vendas e lucratividade com interface moderna e intuitiva.

## ✨ Funcionalidades

### 📊 Painel de Controle
- Visão geral completa das vendas e lucros
- Métricas em tempo real de performance
- Gráficos de produtos mais vendidos
- Histórico detalhado de transações

### 💰 Calculadora de Lucro
- Cálculo automático de custos por ingrediente
- Análise de margem de lucro em tempo real
- Simulação de diferentes cenários de preço
- Consideração automática de taxas de comissão (iFood, Uber Eats, etc.)

### 🍽️ Gestão de Produtos
- Cadastro detalhado de ingredientes e custos
- Editor dinâmico para receitas
- Controle de peso por ingrediente
- Atualização e exclusão de produtos

### 📈 Registro de Vendas
- Registro rápido de vendas por produto
- Controle de quantidade e data
- Cálculo automático de comissões
- Histórico completo de vendas

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/batatas-recheadas.git
cd batatas-recheadas
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
streamlit run app.py
```

5. **Acesse no navegador**
```
http://localhost:8501
```

## 📦 Dependências

```txt
streamlit>=1.28.0
pandas>=2.0.0
```

## 🎯 Como Usar

### 1. Cadastrar Produtos
1. Acesse a página "Adicionar Produto"
2. Insira o nome do produto (ex: "Batata com Frango")
3. Adicione os ingredientes com seus respectivos:
   - Custo por kg (R$)
   - Quantidade em gramas por unidade
4. Clique em "Adicionar Produto"

### 2. Calcular Lucro
1. Vá para "Calculadora de Lucro"
2. Defina o preço de venda
3. Configure a taxa de comissão da plataforma
4. Visualize automaticamente:
   - Custo total de produção
   - Receita líquida
   - Lucro por unidade
   - Percentual de margem

### 3. Registrar Vendas
1. Na página "Calculadora de Lucro"
2. Selecione o produto vendido
3. Informe quantidade e data
4. Clique em "Registrar Venda"

### 4. Acompanhar Performance
1. Acesse o "Painel Geral"
2. Visualize métricas consolidadas
3. Analise gráficos de performance
4. Monitore produtos mais vendidos

## 🎨 Características da Interface

### Temas Personalizáveis
- **Tema Escuro**: Design moderno com efeito glassmorphism
- **Tema Claro**: Interface clean e profissional

### Elementos Visuais
- Cards com efeito de vidro fosco
- Gradientes modernos
- Animações suaves em hover
- Layout responsivo
- Tipografia profissional (Inter)

## 📊 Estrutura de Dados

### Produtos
```python
{
    "nome_produto": {
        "Ingrediente": ["Batata", "Frango", "Queijo"],
        "Custo do kg (R$)": [6.00, 12.00, 25.00],
        "Gramas por unidade": [250, 100, 50]
    }
}
```

### Vendas
```python
{
    "Produto": "Batata com Frango",
    "Data": "2024-01-15",
    "Quantidade": 3,
    "Preco_Venda": 25.00,
    "Comissao_iFood": 15.2
}
```

## 🔧 Configuração Avançada

### Personalização de Temas
Edite as funções CSS em `apply_theme()` para customizar:
- Cores principais
- Efeitos de transparência
- Animações
- Tipografia

### Adição de Plataformas
Para adicionar novas plataformas de delivery:
1. Modifique o campo de comissão
2. Adicione validações específicas
3. Implemente cálculos diferenciados

## 📈 Métricas Calculadas

### Custos
- **Custo por grama**: `(Custo do kg ÷ 1000)`
- **Custo por unidade**: `Custo por grama × Gramas por unidade`
- **Custo total**: `∑ Custos por unidade`

### Receitas
- **Receita bruta**: `Preço de venda × Quantidade`
- **Receita líquida**: `Receita bruta × (1 - Taxa de comissão)`

### Lucros
- **Lucro por unidade**: `Receita líquida - Custo total`
- **Margem de lucro**: `(Lucro ÷ Receita líquida) × 100`

## 🛡️ Considerações de Segurança

- Dados armazenados localmente na sessão
- Não há persistência automática de dados
- Recomenda-se backup regular via exportação
- Ambiente local seguro para dados sensíveis

## 🚀 Roadmap

### Próximas Funcionalidades
- [ ] Exportação de relatórios (PDF/Excel)
- [ ] Persistência de dados (SQLite/PostgreSQL)
- [ ] Sistema de login e usuários
- [ ] Integração com APIs de delivery
- [ ] Dashboard avançado com mais gráficos
- [ ] Controle de estoque de ingredientes
- [ ] Alertas de margens baixas
- [ ] Comparativo temporal de vendas

### Melhorias Técnicas
- [ ] Testes automatizados
- [ ] Docker containerization
- [ ] Deploy em nuvem
- [ ] API REST complementar
- [ ] Mobile responsiveness aprimorado

## 🤝 Contribuição

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um **Pull Request**

### Padrões de Código
- Use formatação PEP 8 para Python
- Comente funções complexas
- Mantenha consistência no estilo
- Teste suas alterações localmente

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

- **Email**: menezesleandro@usp.br
- **Telefone**: (11) 94523-4207
- **Issues**: [GitHub Issues](https://github.com/seu-usuario/batatas-recheadas/issues)

## 👥 Autor

- **Leandro Menezes** - [GitHub](https://github.com/seu-usuario)
- **Email**: menezesleandro@usp.br
- **Telefone**: (11) 94523-4207

## 💡 História do Projeto

Este sistema foi desenvolvido especialmente para ajudar pequenos empreendedores do ramo alimentício a ter controle financeiro preciso de seus negócios. A inspiração veio da necessidade real de auxiliar minha sogra a contabilizar suas vendas de batatas recheadas no iFood e visualizar estatísticas importantes para o crescimento do negócio.

### O Problema Original
- Dificuldade em calcular custos reais por produto
- Falta de visibilidade sobre margens de lucro
- Controle manual propenso a erros
- Ausência de dados para tomada de decisões

### A Solução
Um sistema completo que automatiza cálculos, organiza dados de vendas e fornece insights visuais para otimizar o negócio, permitindo que empreendedores foquem no que fazem de melhor: preparar comida deliciosa!

## 🙏 Agradecimentos

- Comunidade Streamlit pela excelente documentação
- Pandas pela manipulação eficiente de dados
- Minha sogra, que inspirou este projeto com sua determinação empreendedora
- Todos os pequenos empreendedores que lutam diariamente para fazer seus negócios prosperarem

---

<div align="center">
  <p><strong>Desenvolvido com 🥔 e ❤️ para ajudar pequenos empreendedores</strong></p>
  <p><em>"Transformando necessidades reais em soluções tecnológicas"</em></p>
  <p>⭐ Se este projeto foi útil para seu negócio, deixe uma estrela!</p>
</div>