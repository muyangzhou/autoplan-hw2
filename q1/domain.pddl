(define (domain kitten_q1-domain)
 (:requirements :strips :typing)
 (:types room kitten)
 (:constants
   playroom kitchen - room
 )
 (:predicates 
             (connected ?rm1 - room ?rm2 - room)
             (current_room ?k - kitten ?rm - room)
             (has_drunk ?k - kitten)
             (has_played ?k - kitten)
 )
 (:action move
  :parameters ( ?k - kitten ?rm_from - room ?rm_to - room)
  :precondition (and (connected ?rm_from ?rm_to) (current_room ?k ?rm_from))
  :effect (and (current_room ?k ?rm_to) (not (current_room ?k ?rm_from))))
 (:action drink
  :parameters ( ?k - kitten)
  :precondition (and (current_room ?k kitchen))
  :effect (and (has_drunk ?k)))
 (:action play
  :parameters ( ?k - kitten)
  :precondition (and (current_room ?k playroom))
  :effect (and (has_played ?k)))
)
