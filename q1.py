from unified_planning.shortcuts import *
from unified_planning.io import PDDLWriter
import os


# ============================
# TYPES
# ============================

Kitten = UserType("kitten")
Room = UserType("room")

# ============================
# FLUENTS
# ============================

connected = Fluent("connected", rm1=Room, rm2=Room)
current_room = Fluent("current_room", k=Kitten, rm=Room)
has_drunk = Fluent("has_drunk", k=Kitten)
has_played = Fluent("has_played", k=Kitten)


# ============================
# ACTIONS
# ============================

# -------- MOVE --------
move = InstantaneousAction("move", k=Kitten, rm_from=Room, rm_to=Room)
k = move.parameter("k")
rm_from = move.parameter("rm_from")
rm_to = move.parameter("rm_to")

move.add_precondition(connected(rm_from, rm_to))
move.add_precondition(current_room(k, rm_from))

# Add new location
move.add_effect(current_room(k, rm_to), True)

# Remove old location
move.add_effect(current_room(k, rm_from), False)


# -------- DRINK --------
drink = InstantaneousAction("drink", k=Kitten)
k_d = drink.parameter("k")
kitchen_const = Object("kitchen", Room)
drink.add_precondition(current_room(k_d, kitchen_const))
drink.add_effect(has_drunk(k_d), True)


# -------- PLAY --------
play = InstantaneousAction("play", k=Kitten)
k_p = play.parameter("k")

# Must be in playRoom
playroom_const = Object("playRoom", Room)

play.add_precondition(current_room(k_p, playroom_const))
play.add_effect(has_played(k_p), True)


# ============================
# DOMAIN BUILDER
# ============================

def build_base_problem():
    problem = Problem("kitten_q1")

    # Add fluents
    problem.add_fluent(connected)
    problem.add_fluent(current_room)
    problem.add_fluent(has_drunk)
    problem.add_fluent(has_played)

    # Add actions
    problem.add_action(move)
    problem.add_action(drink)
    problem.add_action(play)

    # Add room objects
    kitchen = problem.add_object("kitchen", Room)
    playroom = problem.add_object("playRoom", Room)

    # Connectivity
    problem.set_initial_value(connected(kitchen, playroom), True)
    problem.set_initial_value(connected(playroom, kitchen), True)

    return problem


# ============================
# FAMILY GENERATOR
# ============================

def generate_instance(n):
    """
    Generate instance with n kittens.
    Each kitten must drink and play.
    """
    problem = build_base_problem()

    kitchen = problem.object("kitchen")
    playroom = problem.object("playRoom")

    for i in range(n):
        kitten = problem.add_object(f"kitten{i}", Kitten)

        # Alternate starting positions
        if i % 2 == 0:
            problem.set_initial_value(current_room(kitten, playroom), True)
        else:
            problem.set_initial_value(current_room(kitten, kitchen), True)

        problem.set_initial_value(has_drunk(kitten), False)
        problem.set_initial_value(has_played(kitten), False)

        # Goals
        problem.add_goal(has_drunk(kitten))
        problem.add_goal(has_played(kitten))

    return problem


# ============================
# WRITE FAMILY
# ============================

def write_family():
    os.makedirs("q1", exist_ok=True)

    # Generate first problem to extract domain
    first_problem = generate_instance(1)
    writer = PDDLWriter(first_problem)
    writer.write_domain("q1/domain.pddl")

    # Generate 5 increasing instances
    for i in range(1, 6):
        problem = generate_instance(i)
        writer = PDDLWriter(problem)
        writer.write_problem(f"q1/problem{i}.pddl")

    print("Q1 family generated successfully.")


if __name__ == "__main__":
    write_family()