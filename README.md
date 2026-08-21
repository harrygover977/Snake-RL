# Snake Reinforcement Learning

---

A Reinforcement learning model that learns to play the classic game of snake made using Python and Pygame. 

---

## Demo 



## ⏳ Work flow 
- The current game state is passed to an agent.
- The agent then chooses the next move and is rewarded based on the outcome.
- The agent then uses Q-learning to improve its decisions based on the rewards.
- The game state is then updated and the process is repeated. 

---

## ⚙️ Tech Stack 
- Pygame for the snake environment 
- Numpy for the Q-table
- Python for the agent logic

--- 

## 📝 Current Q-learning values 
- Discount factor: 0.9
- Learning Rate: 0.1
- Decay Rate: 0.995

---

## 💡Challenges/Solutions

The main challenge I faced when building this project was representing the position of the fruit relative to the snakes current direction. I found by determining the fruits absolute postion first (LEFT, RIGHT, UP, or DOWN) I was more easily able to then finds its position relative to the snake (STRAIGHT, LEFT, RIGHT, or BEHIND). 

---

## ⏭️ What's next

After ~2000 game iterations I was able to acheive a high score of 37. I will be experiementing with different Q-learning and reward values to see if I can improve this number. 
I might also look at adding more state variables to better represent the game environment. 