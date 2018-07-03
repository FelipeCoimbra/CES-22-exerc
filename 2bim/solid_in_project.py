'''
Meu projeto bimestral se chamou Webits. Tratou-se de um site desenvolvido para a
iniciativa ITABits dos alunos e pode ser acessado atualmente pelo domínio
            www.itabits.com.br
O website desenvolvido contou com diversas features como:

1) Disposição moderna da iniciativa em uma Landing Page
2) Listagem de membros atuais e passados da iniciativa
3) Listagem de projetos desenvolvidos pelo membros ao longo dos anos
4) Página com materiais de estudo em diversos assuntos pertinentes à iniciativa,
como programação competitiva e linguagens de programação
5) Sistema de deploy duplo, ora com hosted backend e sistema de rotas no frontend
ora com sistema de rotas em um backend feito em Flask

Foram imprescindíveis o uso dos princípios SOLID no projeto para que o código se
tornasse mais fácil de testar, manter e extender pelos futuros membros da iniciativa.
Alguns exemplos citáveis são:

1- Todo tipo de listagem de conteúdo houve desacoplamento entre container e o
seu conteúdo. Ex: Listagem de membros, projetos, tutoriais, etc. Isso foi feito
sob o princípio de Single Responsability, tornando mais fácil debugar problemas
advindo da lógica de listagem e iteração e problemas advindo internamente do
conteúdo.

2- Foi utilizado Reactjs como framework principal do desenvolvimento da UI/UX do
site. Isso não foi possível sem uso intensivo do princípio de Liskov, já que a
filosofia da framework gira em torno da criação dos chamados Custom React Components
a partir do React.Component base. Dessa maneira é preciso estender funcionalidades
básicas dos Components como lógica de montagem e atualização com funções como
componentDidMount() e componentDidUpdate() e renderização do frontend pelo overload
da função render().

3- Em especial nos tutoriais usei de maneira esperta Dependecy Injection em um ponto
crítico do projeto: atualização de conteúdo produzido pela iniciativa ao longo do
tempo. Para isso nos integramos um repositório separado "Tutoriais" da iniciativa
onde vão ficar os conteúdos que forem sendo produzidos e o adicionamos ao projeto do
site como um submódulo. Todo o conteúdo fica nesse submódulo e metadados a respeito
deles ficam concentrados em um único arquivo tutorials.json. Na inicialização do site,
esses metadados são lidos pela aplicação, criando-se um Javascript Object de informações
a respeito dos tutoriais que devem ser renderizados que é injetado em um componente
Sidebar por onde o usuário é capaz de navegar entre conteúdos. Desse modo a lógica de
fetching do conteúdo do site é desacoplado do objeto que estrutura sua renderização
para que seja rápido e fácil de adicionar e organizar conteúdo: novos membros não precisam
alterar nenhuma linha de código do site para por novos tutoriais, basta fazer upload desse
novo material, atualizar o repositório do site e fazer um novo deploy.
'''
