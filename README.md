# Sorting Algorithms

#Bubble Sort

O Bubble Sort é um algoritmo de ordenação. Dado um vetor, o algoritmo percorre esse vetor n-1
vezes fazendo comparações entre elementos que estão em posições consecutivas. Portanto,
começando do primeiro elemento do vetor sendo comparado com o segundo, por exemplo. Se o
elemento mais distante for menor que o elemento anterior, é feita a troca das posições e assim por
diante arrastando o maior valor para o final do vetor para que a ordenação seja feita.
É usada uma variável TRUE ou FALSE que controla se houve ou não a troca. Se o algoritmo não fizer
mais nenhuma troca de valor durante uma varredura do vetor, significa que o vetor está ordenado e
termina o processo.

O grau de complexidade do algoritmo no melhor caso é O(n), quando o vetor já está ordenado. E o
pior caso ocorre quando o vetor está ordenado em ordem decrescente, pois será necessário a troca
em todas as iterações, sendo da ordem O(n2).

#Quicksort

O quick sort é um algoritmo de ordenação e usa a técnica de dividir para conquistar. Dado um vetor é
escolhido um elemento do vetor chamado de pivô ou ponto de divisão. A função do pivô é servir de
referência para repartição dos elementos entre duas sublistas. Portanto, os elementos serão
comparados com o pivô, de forma que: os menores elementos são encaminhados para a sublista
inferior e os maiores elementos são encaminhados para a sublista superior. Convencionalmente é
escolhido como pivô o primeiro elemento da lista, no caso o primeiro código abaixo apresentado.

A complexidade do algoritmo:

Pior caso
Ocorre quando o pivô divide o vetor em dois subvetores, um com zero elementos e outro com
n – 1 elementos. Ou seja, o ponto de divisão fica muito distante dos demais elementos;
Complexidade: O (n2)

Melhor caso
Ocorre quando o pivô escolhido divide o vetor em dois subvetores de tamanho iguais a n/2. Ou
seja, o ponto de divisão fica na metade do vetor;
Complexidade: O (n log n)

#Quicksort Probabilístico

Como mostrado acima convencionalmente primeiro elemento da lista. Entretanto, para obter
uma maior eficiência no algoritmo é escolhido aleatoriamente um elemento do vetor, segundo
código abaixo apresentado, pois probabilisticamente as chances de o pivô não ser um elemento
distante das posições medianas do vetor diminuem.

Caso médio
É a média de todos os possíveis casos de posicionamento do pivô após a partição.
Complexidade: O ( n log ( n))



