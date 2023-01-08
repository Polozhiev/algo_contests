# Условия задач

## 1. Компоненты связности

Вам задан неориентированный граф с N вершинами и M ребрами (1≤N≤20000, 1≤M≤200000). В графе отсутствуют петли и кратные ребра.

Определите компоненты связности заданного графа.

## 2. Долой списывание!

Во время теста Михаил Дмитриевич заметил, что некоторые лкшата обмениваются записками. Сначала он хотел поставить им всем двойки, но в тот день Михаил Дмитриевич был добрым, а потому решил разделить лкшат на две группы: списывающих и дающих списывать, и поставить двойки только первым.

У Михаила Дмитриевича записаны все пары лкшат, обменявшихся записками. Требуется определить, сможет ли он разделить лкшат на две группы так, чтобы любой обмен записками осуществлялся от лкшонка одной группы лкшонку другой группы.

## 3. Поиск цикла

Дан ориентированный невзвешенный граф. Необходимо определить есть ли в нём циклы, и если есть, то вывести любой из них.

## 4. Конденсация графа

Требуется найти количество ребер в конденсации ориентированного графа. Примечание: конденсация графа не содержит кратных ребер.

## 5. Противопожарная безопасность

В Судиславле n домов. Некоторые из них соединены дорогами с односторонним движением.

В последнее время в Судиславле участились случаи пожаров. В связи с этим жители решили построить в посёлке несколько пожарных станций. Но возникла проблема: едущая по вызову пожарная машина, конечно, может игнорировать направление движения текущей дороги, однако возвращающаяся с задания машина обязана следовать правилам дорожного движения (жители Судиславля свято чтут эти правила!).

Ясно, что, где бы ни оказалась пожарная машина, у неё должна быть возможность вернуться на ту пожарную станцию, с которой она выехала. Но строительство станций стоит больших денег, поэтому на совете посёлка было решено построить минимальное количество станций таким образом, чтобы это условие выполнялось. Кроме того, для экономии было решено строить станции в виде пристроек к уже существующим домам.

Ваша задача — написать программу, рассчитывающую оптимальное положение станций.


## 6. 2-SAT

Широко известна задача 2-SAT. Решите её. Гарантируется, что решение существует.

Формулировка 2-SAT: нужно подобрать значения n булевых переменных так, чтобы все m утверждений вида xi1=e1∨xi2=e2 обратились в истину.

Входной файл состоит из одного или нескольких тестов.

Каждый тест описывается следующим образом. На первой строке число переменных n и число утверждений m. Каждая из следующих m строк содержит числа i1,e1,i2,e2, задает утверждение xi1=e1∨xi2=e2 (0≤ij<n, 0≤ej≤1).

Ограничения: сумма всех n не больше 100000, сумма всех m не больше 300000.

## 7. Олег Игоревич Мингалёв

Олег Игоревич Мингалёв играет в игру «Кубб». В определенный момент игры ему нужно поднять лежащие на игровом поле чурбаны: каждый чурбан нужно поставить вертикально, и по правилам это можно сделать только поставив его в точку, где находился один из его концов.

Когда чурбаны будут подняты, противоположная команда будет их сбивать. И если чурбаны оказались стоящими близко, то их при должном умении легко сбить одним ударом. Поэтому Олегу Игоревичу важно максимизировать величину D: минимальное расстояние между какой-либо парой чурбанов (длина отрезка от основания первого до основания второго).

Помогите ему поставить каждый чурбан на один из своих концов так, чтобы величина D была максимальной.

## 8. Chip Installation

Новый ЧИП скоро установят в новый летательный апарат, недавно выпущенной компанией Airtram. ЧИП имеет форму диска. Есть n проводов, которые нужно подсоединить к ЧИПу.

Каждый провод можно подсоединить в один из двух разъемов, допустимых для этого провода. Все 2n разъемов расположены на границе диска. По кругу. Каждый провод имеет свой цвет. Для повышения безопасности два провода одного цвета не могут быть подсоединены к соседним разъемам.

Дана конфигурация разъемов на ЧИПе, найдите способ подсоединить все провода, не нарушающий условия про цвета.

## 10. Из истории банка Гринготтс

Чтобы понять название задачи, можно прочитать красивую легенду.

Задача же заключается в том, чтобы рёбра неориентированного графа разбить на минимальное число путей.

## 11. Кодовый замок

Петя опоздал на тренировку по программированию! Поскольку тренировка проходит в воскресенье, главный вход в учебный корпус, где она проходит, оказался закрыт, а вахтёр ушёл куда-то по своим делам. К счастью, есть другой способ проникнуть в здание — открыть снаружи боковую дверь, на которой установлен кодовый замок.

На пульте замка есть d кнопок с цифрами 0, 1, …, d−1. Известно, что код, открывающий замок, состоит из k цифр. Замок открывается, если последние k нажатий кнопок образуют код.

Поскольку Петя не имеет понятия, какой код открывает замок, ему придётся перебрать все возможные коды из k цифр. Но, чтобы как можно скорее попасть на тренировку, нужно минимизировать количество нажатий на кнопки. Помогите Пете придумать такую последовательность нажатий на кнопки, при которой все возможные коды были бы проверены, а количество нажатий при этом оказалось бы минимально возможным.


## 12. Таня и пароль

Пока папа был на работе, маленькая девочка Таня решила поиграть с папиным паролем к секретной базе данных. Папин пароль представляет собой строку, состоящую из n+2 символов. Она выписала все возможные n трёхбуквенных подстрок пароля на бумажки, по одной на каждую бумажку, а сам пароль выкинула. Каждая трёхбуквенная подстрока была выписана на бумажки столько раз, сколько она встречалась в пароле. Таким образом, в итоге у Тани оказалось n бумажек.

Потом Таня поняла, что папа расстроится, если узнает о ее игре, и решила восстановить пароль или, по крайней мере, хотя бы какую-то строку, соответствующую получившемуся набору трёхбуквенных строк. Вам предстоит помочь ей в этой непростой задаче. Известно, что папин пароль состоял из строчных и заглавных букв латинского алфавита, а также из цифр. Строчные и заглавные буквы латинского алфавита считаются различными.