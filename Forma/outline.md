---
title: Forma
documentclass: amsart
---

# What is a Game Engine

Game engines can either be fully built tools, or it can be just a 3D
interaction/visualization system. A game engine is a system to read data in and
display it to the screen. And frequently also allows interaction with that
data. The game engine is very data oriented, wee are mainly reading in
data/assets.

A game engine creates a set of tools to create assets for the game engine to
use. The game engine includes the tools to create assets, like level
editors, or material creators. The end result should mean that there is very
little programming, making a game can be mainly creating the assets, which
may include scripts, that the game engine then displays to the screen.

Making a game engine is a bad idea if you just want to make a game.

# Designing the Game Engine

Create something that works quickly, and then rapidly improve it over time.
Compromises will be made, but they can be improved upon in the future. These
are all of the components that will need to be implemented, not necessarily in
the order of implementation.

- Entry Point
- Application Layer
- Window Layer
  - Inputs
  - Events
- Renderer
- Render API Abstraction
  - We use the API, so that we can implement multiple different renderers for
    different platforms.
- Debugging Support
- Scripting Language
- Memory Systems
- Entity Component System (ECS)
- Physics
- File I/O
- VFS
- Build System
- Hot swappable Assets
