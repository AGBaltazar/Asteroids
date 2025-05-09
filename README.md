# Python Asteroids Game

A recreation of the classic arcade game Asteroids built with Python. Control your spaceship, destroy asteroids, and survive as long as possible in this space-themed shooter.

## Installation

### Prerequisites
- Python 3.10+
- Pygame library

### Setup
1. Clone the repository:

git clone https://github.com/AGBaltazar/Asteroids.git

cd asteroids-game


2. Install dependencies:

pip install pygame


## How to Play

Run the game using:

python main.py


### Controls
- Arrow Up: Thrust forward
- Arrow Left/Right: Rotate ship
- Spacebar: Fire bullets
- ESC: Pause game

## Game Features
- Physics-based movement with momentum and inertia
- Asteroids that split into smaller pieces when hit

## Project Structure
- `main.py`: Game initialization and main loop
- `game.py`: Core game logic and state management
- `ship.py`: Player ship class and controls
- `asteroid.py`: Asteroid generation and behavior
- `bullet.py`: Projectile handling
- `utils.py`: Utility functions and helpers
- `assets/`: Directory containing images and sounds

## Future Enhancements
- [ ] Power-ups (shields, rapid fire, etc.)
- [ ] Multiple levels with increasing difficulty
- [ ] Different asteroid types (ice, metal, etc.)
- [ ] Background music and sound effects
- [ ] Visual effects (explosions, engine thrust)
