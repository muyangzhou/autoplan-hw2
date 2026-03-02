(define (problem kitten_q2-problem)
 (:domain kitten_q2-domain)
 (:objects
   kitten0 - kitten
 )
 (:init
              (connected kitchen playroom)
              (connected playroom kitchen)
              (toy_free)
              (current_room kitten0 playroom)
 )
 (:goal (and 
           (has_drunk kitten0)
           (has_played kitten0)
        )
 )
)
