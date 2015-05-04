### Coding
Q:

- Linguagens: Quais linguagens de programação você conhece? Java, Groovy, Python, C, C++, Scala, Ruby? Alguma linguagem de script? Que nota (de 1 a 10) você daria para teu conhecimento/experiência? Que experiência de trabalho possui com cada linguagem? Quais projetos realizados? Quantos usuários haviam?
- Linux: Qual teu conhecimento de Linux? Somente usuário ou desenvolvimento? Bash script?

A:

- Pass

Q:

- Linguagens funcionais: Qual teu conhecimento em linguagens funcionais? Quais são as características que destacam programação funcional?

A:

- Treats computation as the evaluation of mathematical functions
- The output of a function depends only on its inputs and is not dependent on state.

Q:

- Qual a diferença entre linguagens fortemente e fracamente tipadas?

A:

- Strong and weak typing is about how strictly types are distinguished. A very weakly typed language e.g. js or HyperTalk could do something like this `"12" + "34" => "46", "12" + "34Q" => "1234Q"`. A strongly typed language e.g. C, java, normally won't allow modifying the type of a variable after it has been declared.
- Static-typing is when programs are checked at compile time. Dynamic, when they are checked at runtime.

Q:

- Você sabe o que é condição de corrida (race condition)?  O que é? O que usa para sincronizar acesso a um recurso compartilhado?

A:

- When multiple threads have been executed which modify the same output and may not be executed in the intended order. (e.g. two threads incrementing a global integer, this is why javascript is single threaded so as not to modify the same element)

### OO Design

Q:

- Conhece padrões de projeto? Padrões de arquitetura? Quais? Sabe o que é DDD? GoF? Patterns of Enterprise Application Architectures?

A:

- Many ways of coding the same thing

Q:

- Qual a diferença entre sobrecarga e sobrescrita de método?

A:

- pass

Q:

- O que é polimorfismo? E ducktyping?

A:

Polymorphism is a single interface to multiple types.

- e.g. ints and floats both have methods `.add()`, `.subtract()`, `.divide()` and `.mulitply()`
- e.g. `Circle` and `Square` inherit from super class `Shape` and both have the method `.draw()`

Ducktyping:

- > "If it looks like a duck and quacks like a duck, it's a duck".
- You don't need the object to be of a specific type to invoke a method, if it has that method you may invoke it.
- e.g. `Duck().quack()` and `Person().quack()`

- O que é herança múltipla? Quais os efeitos colaterais?
- Qual a diferença entre um método estático e um método de instância?

### Algoritmos, data structures and optimization

- Quais estruturas de dados você conhece? Qual a diferença entre uma lista ligada e um array? Qual a complexidade das operações em cada uma delas?
- Você sabe o que é uma busca binária?
- Explique o funcionamento de um hash map? Qual o impacto de uma boa função de hash nesta estrutura?
- Você já trabalhou com otimização de algoritmos? Qual foi tua experiência? Já fez análise de complexidade de algoritmos?
- Conhece ferramentas de profiling e testes de stress? Em que contexto utilizou?

### Bits and Bytes

- Quantos bits tem um byte?
- Em uma arquitetura de 32 bits com a liguagem C, quantos bytes tem um inteiro?
- Para que serve o operador lógico XOR? Em que situação ele retorna true?
- Em C, qual a diferença entre tipos signed e unsigned?
- Como é representado numericamente um float?


### Software Engineering

- Quais metodologias de desenvolvimento você conhece? Com quais delas você já teve experiência profissional? Scrum? Kanban?
- Quais práticas de XP você conhece? Quais você costuma utilizar? Pair programming?  Ja teve uma experiência no dia-a-dia com ela?
- Conhece TDD? Utiliza bastante? Usa Mock/Stub? Qual ferramenta?
- Conhece integração contínua? Qual ferramenta utiliza? Utilizou pra que? Qual o benefício dessa prática?
- Sabe o que é coesão em desenvolvimento de software? Qual a relação com acoplamento? Por que não é interessante duplicar código?

### Java

- O que conhece de Java? Com quais bibliotecas teve experiência?
- Frameworks? Spring, Hibernate?
- Quando o Garbage Collector é disparado?
- Existe memory leak em Java? Explique.
- Existe uma regra para o uso do método hashCode e equals. Sabe qual é esta regra? Por que ela existe?

### Web & DB

- Sabe o que é tableless? Qual a vantagem de se utilizar esta técnica?
- Qual biblioteca de Javascript costuma utilizar? Por que?
- Já implementou Web Services? Cliente ou provedor? Prefere REST ou SOAP? Por que?
- Conhece SQL? Que nota você daria para teus conhecimento em SQL? O que você faz para otimizar queries? Conhece “explain”?
- Quais banco de dados você conhece? Como você mapearia uma estrutura hierarquica OO em um modelo relacional?

### Extras

- Que nota (de 1 a 10) você daria para teus conhecimentos de matemática, cálculo e estatística?
- Já trabalhou com grids/clusters computacionais?
- Já trabalhou com AWS? O que conhece? EC2? S3?
- Experiência com desenvolvimento de algoritmos de IA? Redes Neurais?
- Conhece algum NoSQL? Cassandra?

# [Entrevista técnica - front end engineer](https://docs.google.com/a/chaordicsystems.com/document/d/1uGCChsFEWqFIDjv9BbmsvL1x8Ch8AhDyuDFM11pMHzg/edit?pli=1#heading=h.x60n2iviyesk)

# Perguntas gerais

1. O que você usa para desenvolver? Quais ferramentas, sistema operacional, navegadores etc?

2. Quais os navegadores que você usa? Porque?

3. Qual sistema de controle de versão você usa? Por quê?

4. Quais os sites que você admira?

5. Quais autores/desenvolvedores você admira?

6. O que é *graceful degradation*?

7. O que é HTTP? Quais métodos existem e quais as suas diferenças?

8. O que são cookies e para que servem?

9. Sabe como servidores controlam seções?

# HTML

1. Qual a diferença entre XHTML e HTML? Qual você prefere usar? Por quê?

2. Qual a importância do DOCTYPE? Quirksmode?

	*Ele diz ao navegador como interpretar o html da página, definindo a versão do html usada.*

3. Para que servem os atributos *id* e *class*? Como você faz uso deles? Qual a política que você adota?

4. Para que serve o elemento **`<label**>`?

5. Comente sobre alguns elementos **`<meta**>` (e.g. keywords e description) e para que servem?

6. O que são *html entities*? Quando é interessante usar?

7. Quais as funcionalidades de HTML5 que você já brincou?

# CSS

1. Qual a diferença entre um elemento *inline* e um elemento *block*?

2. Como funciona a precedência/especificidade de regras em CSS? Como o **`!importan**t` afeta a precedência?

3. O que você entende por CSS reset? Você já usou algum? Quais?

4. Quais os seletores que você usa? Dê exemplos.

5. Qual a diferença entre as unidades de medida *px*, *pt*, e *em*? Qual outra medida vc usa?

6. Quais modos que podem ser utilizados para especificar cores em CSS?

7. Descreva o funcionamento de *float* e *clear*. Qual a relação entre eles?

8. Qual a diferença entre position *static, relative, fixed* e *absolute*?

9. Explique o que é *margin collapsing*

10. Como funciona o *z-index*?

11. O que é um *CSS sprite*? Para que serve?

# JavaScript

1. **Quais são os tipos de dados disponíveis na linguagem JavaScript?**

*Number (42, 3.13, -127)*

*String ("Aspas duplas", ‘aspas simples’)*

*Boolean (true, false)*

*null*

*undefined*

*Object*

*Array*

*Function*

2. **Qual a diferença entre == e ===?**

	*== avalia o valor*

*=== avalia o valor e o tipo*

*"1" == 1*

*true*

*"1" === 1*

*false*

3. **O que é uma closure?**

4. O que é *module pattern*?

5. Como funcionam os métodos *call* e *apply*? Qual a diferença entre eles?

6. O que é o DOM? (explique de forma geral)

	*Document Object Model. É um modelo formado por nós que representa a árvore html. Cada nó pode ser um elemento, texto, atributo ou comentário.*

7. Como funciona a propagação de eventos?

8. O que é AJAX? Quais os modos que é possivel fazer AJAX?

9. **O que você entende por ****_Same Origin Policy_****? Como lidar com isso?**

10. **O que é minificação e ofuscação?**

11. Como funciona a herança prototipal em JavaScript?

# Extras

1. Comente sobre quais linguagens de programação você teve contato.

2. Você conhece Node.js? Fale sobre o assunto.

3. Quais as estruturas de dados que você conhece e/ou usa?

4. Sabe o que é JSON? Para que serve?

	*JavaScript Object Notation é um formato muito utilizado atualmente para troca de dados. É um formato independente de linguagem que usa convenções das linguagens mais usadas: listas e objetos.*

5. Quais os principais conceitos e boas práticas de OO?

6. Conhece Coffee Script? Quais são seus sentimentos em relação?

7. Conhece pré-processadores CSS? Quais são seus sentimentos em relação à eles?

8. O que você entende por encoding?

9. Projeto

    1. Você consegue desenvolver um projeto de desenvolvimento de software ou produto completo?

    2. Conhece todas as fases envolvidas?

    3. Quais processos você conhece?

    4. Consegue lidar com clientes?

    5. Consegue lidar com a fase de captação de requisitos? (Avaliar a capacidade de entender um problema e criar a solução)

    6. Conhece metodologias ágeis?

10. O que você quer aprender este ano?

11. Qual é o seu ponto forte?