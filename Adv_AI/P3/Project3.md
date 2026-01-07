
# Go, Pac-Man Go!

## Problem 1

## 1.a

```math
\boxed{
V_{\textrm{minimax}}(s,d)=\left\{\begin{array}{ll}

    \textrm{Utility}(s) & \textrm{IsEnd}(s) \\
    \textrm{Eval}(s) & d = 0 \\
    \underset{a\in\textrm{Actions}(s)}{\textrm{max}}V_{\textrm{minimax}}(\textrm{Succ}(s,a),d) & \textrm{Player}(s)=\textrm{agent} \\ 
    \underset{a\in\textrm{Actions}(s)}{\textrm{min}}V_{\textrm{minimax}}(\textrm{Succ}(s,a),d) & \textrm{Player}(s)=\textrm{opp}_1 \\
    \vdots \\
    \underset{a\in\textrm{Actions}(s)}{\textrm{min}}V_{\textrm{minimax}}(\textrm{Succ}(s,a),d-1) & \textrm{Player}(s)=\textrm{opp}_n
    
\end{array}\right.} 
```

## 1.b

See the file `submission.py`.

Test it with 

```bash
python grader.py
```

or 

```bash
python3 pacman.py -p MinimaxAgent
```

## Problem 2

## 2.a

See the file `submission.py`.

Also, if you are in linux, I wrote a command to check whether `AlphaBetaAgent` and `MinimaxAgent` give the same results.

```bash
for i in $(seq 1 3);
do
    if [[ $(python3 pacman.py -p AlphaBetaAgent -g DirectionalGhost -a depth=$i -f -q) == $(python3 pacman.py -p MinimaxAgent -g DirectionalGhost -a depth=$i -f -q) ]]; then
        echo -e "\033[0;32mDepth $i is OK\033[0m";
    else
        echo -e "\033[0;31mDepth $i is not OK\033[0m";
    fi
done
```

Here are the results:

```bash
time python3 pacman.py -p MinimaxAgent -g DirectionalGhost -a depth=4 -f -q
```

```
Pacman died! Score: 692
('Average Score:', 692.0)
('Scores:       ', '692')
Win Rate:      0/1 (0.00)
('Record:       ', 'Loss')

real	0m4.668s
user	0m4.642s
sys	0m0.025s

```

```bash
time python3 pacman.py -p AlphaBetaAgent -g DirectionalGhost -a depth=4 -f -q
```

```
Pacman died! Score: 692
('Average Score:', 692.0)
('Scores:       ', '692')
Win Rate:      0/1 (0.00)
('Record:       ', 'Loss')

real	0m1.472s
user	0m1.437s
sys	0m0.033s
```

## Problem 3

## 3.a

## 3.b

## Problem 4

## 4.a

## 4.b

## Problem 5

## 5.a

## 5.b

## 5.c



