
# Go, Pac-Man Go!

## Problem 1

## 1.a

$$ 
\boxed{
V_{\textrm{minimax}}(s,d)=\left\{\begin{array}{ll}

    \textrm{Utility}(s) & \textrm{IsEnd}(s) \\
    \textrm{Eval}(s) & d = 0 \\
    \underset{a\in\textrm{Actions}(s)}{\textrm{max}}V_{\textrm{minimax}}(\textrm{Succ}(s,a),d) & \textrm{Player}(s)=\textrm{agent} \\ 
    \underset{a\in\textrm{Actions}(s)}{\textrm{min}}V_{\textrm{minimax}}(\textrm{Succ}(s,a),d) & \textrm{Player}(s)=\textrm{opp}_1 \\
    \vdots \\
    \underset{a\in\textrm{Actions}(s)}{\textrm{min}}V_{\textrm{minimax}}(\textrm{Succ}(s,a),d-1) & \textrm{Player}(s)=\textrm{opp}_n
    
\end{array}\right.} 
$$

## 1.b

See the file `submission.py`.

Test it with 

```
python grader.py
```

or 

```
python3 pacman.py -p MinimaxAgent
```

## Problem 2

## 2.a

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



