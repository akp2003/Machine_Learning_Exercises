from util import manhattan_distance
from game import Directions
import random
import util
from typing import Any, DefaultDict, List, Set, Tuple

from game import Agent
from pacman import GameState



class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def __init__(self):
        self.last_positions = []
        self.dc = None

    def get_action(self, game_state: GameState):
        """
        get_action chooses among the best options according to the evaluation function.

        get_action takes a GameState and returns some Directions.X for some X in the set {North, South, West, East}
        ------------------------------------------------------------------------------
        Description of GameState and helper functions:

        A GameState specifies the full game state, including the food, capsules,
        agent configurations and score changes. In this function, the |game_state| argument
        is an object of GameState class. Following are a few of the helper methods that you
        can use to query a GameState object to gather information about the present state
        of Pac-Man, the ghosts and the maze.

        game_state.get_legal_actions(agent_index):
            Returns the legal actions for the agent specified. Returns Pac-Man's legal moves by default.

        game_state.generate_successor(agent_index, action):
            Returns the successor state after the specified agent takes the action.
            Pac-Man is always agent 0.

        game_state.get_pacman_state():
            Returns an AgentState object for pacman (in game.py)
            state.configuration.pos gives the current position
            state.direction gives the travel vector

        game_state.get_ghost_states():
            Returns list of AgentState objects for the ghosts

        game_state.get_num_agents():
            Returns the total number of agents in the game

        game_state.get_score():
            Returns the score corresponding to the current state of the game


        The GameState class is defined in pacman.py and you might want to look into that for
        other helper methods, though you don't need to.
        """
        # Collect legal moves and successor states
        legal_moves = game_state.get_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(
            game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(
            len(scores)) if scores[index] == best_score]
        # Pick randomly among the best
        chosen_index = random.choice(best_indices)


        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state: GameState, action: str) -> float:
        """
        The evaluation function takes in the current GameState (defined in pacman.py)
        and a proposed action and returns a rough estimate of the resulting successor
        GameState's value.

        The code below extracts some useful information from the state, like the
        remaining food (old_food) and Pacman position after moving (new_pos).
        new_scared_times holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successor_game_state = current_game_state.generate_pacman_successor(
            action)
        new_pos = successor_game_state.get_pacman_position()
        old_food = current_game_state.get_food()
        new_ghost_states = successor_game_state.get_ghost_states()
        new_scared_times = [
            ghost_state.scared_timer for ghost_state in new_ghost_states]

        return successor_game_state.get_score()


def score_evaluation_function(current_game_state: GameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return current_game_state.get_score()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, eval_fn='score_evaluation_function', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluation_function = util.lookup(eval_fn, globals())
        self.depth = int(depth)

######################################################################################
# Problem 1b: implementing minimax


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (problem 1)
    """

    def get_action(self, game_state: GameState) -> str:
        """
          Returns the minimax action from the current game_state using self.depth
          and self.evaluation_function. Terminal states can be found by one of the following:
          pacman won, pacman lost or there are no legal moves.

          Don't forget to limit the search depth using self.depth. Also, avoid modifying
          self.depth directly (e.g., when implementing depth-limited search) since it
          is a member variable that should stay fixed throughout runtime.

          Here are some method calls that might be useful when implementing minimax.

          game_state.get_legal_actions(agent_index):
            Returns a list of legal actions for an agent
            agent_index=0 means Pacman, ghosts are >= 1

          game_state.generate_successor(agent_index, action):
            Returns the successor game state after an agent takes an action

          game_state.get_num_agents():
            Returns the total number of agents in the game

          game_state.get_score():
            Returns the score corresponding to the current state of the game

          game_state.is_win():
            Returns True if it's a winning state

          game_state.is_lose():
            Returns True if it's a losing state

          self.depth:
            The depth to which search should continue

          Hint: To implement minimax recursively, consider creating a helper function that
          takes the current game state, current depth, and current agent index as parameters.
        """

        # BEGIN_YOUR_CODE (our solution is 22 line(s) of code, but don't worry if you deviate from this)
        # Extra
        # I added a feature where you can define order for directions
        # so you can tell it to prefer north if going south results in the same score
        # Uncomment the following code it you want to see the magic!
        
        #self.Dir_order = [Directions.NORTH,Directions.WEST,Directions.SOUTH,Directions.EAST]
        #if random.randint(0,3)==0: random.shuffle(self.Dir_order);print(self.Dir_order) # Add randomness with this line of code
        #keyFunc = lambda x : x[0] + (self.Dir_order.index(x[1])/10)
        
        keyFunc = lambda x : x[0] # This does not change anything
        # if you set the keyFunc to None then the results DO NOT match alpha beta pruning
        # Extra
        
        def is_end(s,i):
            return s.is_win() or s.is_lose() #or (len(s.get_legal_actions(i))==0)
            
        def V(s,d,i):
            if is_end(s,i):
                return (s.get_score(), None) # I assume this function will not be called at end state.
            elif d == 0: 
                return (self.evaluation_function(s), None)
            elif i == 0:
                #if d == self.depth: print(i,[(V(s.generate_successor(i,action),d,i+1)[0], action) for action in s.get_legal_actions(i)])
                return max([(V(s.generate_successor(i,action),d,i+1)[0], action) for action in s.get_legal_actions(i)], key = keyFunc)
            elif i == s.get_num_agents()-1:
                #print(i,[(V(s.generate_successor(i,action),d-1,0)[0], action) for action in s.get_legal_actions(i)])
                return min([(V(s.generate_successor(i,action),d-1,0)[0], action) for action in s.get_legal_actions(i)])
            else:
                #print(i,[(V(s.generate_successor(i,action),d,i+1)[0], action) for action in s.get_legal_actions(i)])
                return min([(V(s.generate_successor(i,action),d,i+1)[0], action) for action in s.get_legal_actions(i)])
        
        V_score, best_move = V(game_state,self.depth,0)
        #print(V_score, best_move)
        return best_move
        # END_YOUR_CODE

######################################################################################
# Problem 2a: implementing alpha-beta


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (problem 2)
      You may reference the pseudocode for Alpha-Beta pruning here:
      en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
    """

    def get_action(self, game_state: GameState) -> str:
        """
          Returns the minimax action using self.depth and self.evaluation_function
        """

        # BEGIN_YOUR_CODE (our solution is 43 line(s) of code, but don't worry if you deviate from this)
        # I want to implement it in russel norvig style
        
        def is_end(s,i):
            return s.is_win() or s.is_lose()
            
        def MinValue(s,d,i,alpha,beta):
            pass

        def MaxValue(s,d,i,alpha,beta):
            if is_end(s,i):
                return (s.get_score(), None) 
            elif d == 0: 
                return (self.evaluation_function(s), None)
            elif i ==0:
                v = -float('inf')
                move = None
                for a in s.get_legal_actions(i):
                  (v2,a2) = MinValue(s.generate_successor(i,a),d,i+1,alpha,beta)
                  if v2 > v :
                      v,move = v2,a
                      alpha = max(alpha,v)
                  if v >= beta:
                      return (v,move)
                return (v,move)

        def MinValue(s,d,i,alpha,beta):
            if is_end(s,i):
                return (s.get_score(), None) 
            elif d == 0: 
                return (self.evaluation_function(s), None)
            
            v = float('inf')
            move = None
            for a in s.get_legal_actions(i):
              v2 = None
              if i == s.get_num_agents()-1:
                  (v2,_) = MaxValue(s.generate_successor(i,a),d-1,0,alpha,beta)
              else:
                  (v2,_) = MinValue(s.generate_successor(i,a),d,i+1,alpha,beta)
              if v2 < v :
                  v,move = v2,a
                  beta = min(beta,v)
              if v <= alpha:
                  return (v,move)
            return (v,move)
        
        V_score, best_move = MaxValue(game_state,self.depth,0,-float('inf'),float('inf'))
        #print(V_score, best_move)
        return best_move
        # END_YOUR_CODE

######################################################################################
# Problem 3b: implementing expectimax


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (problem 3)
    """

    def get_action(self, game_state: GameState) -> str:
        """
          Returns the expectimax action using self.depth and self.evaluation_function

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """

        # BEGIN_YOUR_CODE (our solution is 22 line(s) of code, but don't worry if you deviate from this)
        def is_end(s,i):
            return s.is_win() or s.is_lose()
            
        def V(s,d,i):
            if is_end(s,i):
                return (s.get_score(), None)
            elif d == 0: 
                return (self.evaluation_function(s), None)
            elif i == 0:
                return max([(V(s.generate_successor(i,action),d,i+1)[0], action) for action in s.get_legal_actions(i)])
            elif i == s.get_num_agents()-1:
                policy = 1 / len(s.get_legal_actions(i))
                return (sum([policy*V(s.generate_successor(i,action),d-1,0)[0] for action in s.get_legal_actions(i)]),None)
            else:
                policy = 1 / len(s.get_legal_actions(i))
                return (sum([policy*V(s.generate_successor(i,action),d,i+1)[0] for action in s.get_legal_actions(i)]),None)
        
        V_score, best_move = V(game_state,self.depth,0)
        #print(V_score, best_move)
        return best_move
        # END_YOUR_CODE

######################################################################################
# Problem 4a (extra credit): creating a better evaluation function


def better_evaluation_function(current_game_state: GameState) -> float:
    """
      Your extreme, unstoppable evaluation function (problem 4). Note that you can't fix a seed in this function.
    """

    # BEGIN_YOUR_CODE (our solution is 16 line(s) of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE


# Abbreviation
better = better_evaluation_function
