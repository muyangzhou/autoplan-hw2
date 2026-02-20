(define (problem kitten_q1-problem)
 (:domain kitten_q1-domain)
 (:objects
   kitten0 - kitten
 )
 (:init
              (connected kitchen playroom)
              (connected playroom kitchen)
              (current_room kitten0 playroom)
 )
 (:goal (and 
           (has_drunk kitten0)
           (has_played kitten0)
        )
 )
)
