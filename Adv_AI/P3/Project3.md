
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

```math
\boxed{
V_{\textrm{exptmax}}(s,d)=\left\{\begin{array}{ll}
    \textrm{Utility}(s) & \textrm{IsEnd}(s) \\
    \textrm{Eval}(s) & d = 0 \\
    \underset{a\in\textrm{Actions}(s)}{\textrm{max}}V_{\textrm{exptmax}}(\textrm{Succ}(s,a),d) & \textrm{Player}(s)=\textrm{agent} \\ 
    \underset{a\in\textrm{Actions}(s)}{\sum}\pi_{\text{opp}_1}(s,a) V_{\textrm{exptmax}}(\textrm{Succ}(s,a),d) & \textrm{Player}(s)=\textrm{opp}_1 \\
    \vdots \\
    \underset{a\in\textrm{Actions}(s)}{\sum}\pi_{\text{opp}_n}(s,a) V_{\textrm{exptmax}}(\textrm{Succ}(s,a),d-1) & \textrm{Player}(s)=\textrm{opp}_n
\end{array}\right.} 
```

We assume that $\pi_{opp_i}(s,a) = \frac{1}{|Actions(s)|}$.

## 3.b

See the file `submission.py`.

## Problem 4

## 4.a

See the file `submission.py`.

## 4.b

I tried the distance to the closest food near pacman!

If you calculate the Euclidean distance you don't get any improvement but when I tried the Manhattan distance I observed a huge improvement!

It wins 37 times out of 40 games!

## Problem 5

## 5.a

The minimax agent assumes the worst-case scenario, when it gets trapped from both ways it assumes it will die anyway so it chooses the closer opponent to avoid the constant time penalty that reduces the score.

The expectimax agent on the other hand assumes the opponent acts randomly so it gives a chance that the opponent might let it leave the trap, that is why our agent delays its death sometimes!

## 5.b

If we remove the time penalty from the Utility function, our agent might choose to delay its death, but this might cause another problem, assume only one score is left to collect, then with no time penalty our agent might keep wandering without around that last score without any concern. Another way is to consider a survival time reward in Utility function only if the agent dies. For example let's say the penalty of death is -500, then let T be the time that the agent is in the game, we can define when our agent dies to be $\frac{-500}{T+score}$. This means if an agent dies earlier, it gets a larger penalty.

## 5.c

Yesterday, I was watching reels on instagram and I saw a video of Jeffery Epstein and Trump, it was a cool video because of the song on that video (The song was Boss by Lil Pump) I liked the video and then instagram kept suggesting other videos on Jeffery Epstein and some weird conspiracy theory stuff. This is an example of reward hacking, the algorithm keeps suggesting the videos that you like regardless of whether or not it's intended to mislead or deceive people! It also happens in youtube shorts, it keeps suggesting AI slops all the time, and you feel exhausted after watching tons of AI shit that is not interesting!

