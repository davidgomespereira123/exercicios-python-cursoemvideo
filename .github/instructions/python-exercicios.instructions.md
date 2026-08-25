---
description: "Use when writing or correcting Python exercises involving names, text input, variables, tuples, lists, or random selection. Prevents undefined-name errors such as may not defined."
name: "Exercicios Python"
applyTo: "**/*.py"
---
# Exercicios Python

- Escreva valores textuais, como nomes, entre aspas simples ou duplas. Sem aspas, o Python interpreta o texto como uma variável.
- Defina uma variável antes de usá-la e preserve exatamente o mesmo nome em todas as referências.
- Para ler um nome ou outro texto, use `input()` sem `int()` ou `float()`; use conversão numérica somente quando a entrada representar um número.
- Para sortear um item de uma tupla ou lista, use `random.choice()` e importe `random` antes do uso.
- Execute o arquivo ou uma checagem de sintaxe após corrigir o exercício, confirmando que não há nomes indefinidos nem erros de conversão.

Exemplo:

```python
import random

alunos = ('david', 'gabi', 'lucas', 'may')
print(random.choice(alunos))
```
