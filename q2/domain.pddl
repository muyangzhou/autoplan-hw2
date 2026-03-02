(define (domain kitten_q2-domain)
 (:requirements :strips :typing)
 (:types room kitten)
 (:constants
   kitchen playroom - room
 )
 (:predicates 
             (connected ?rm1 - room ?rm2 - room)
             (current_room ?k - kitten ?rm - room)
             (has_drunk ?k - kitten)
             (has_played ?k - kitten)
             (toy_free)
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
  :precondition (and (current_room ?k playroom) (toy_free))
  :effect (and (not (toy_free)) (has_played ?k)))
 (:action free_toy
  :parameters ( ?k - kitten)
  :precondition (and (current_room ?k playroom) (has_played ?k))
  :effect (and (toy_free)))
)
