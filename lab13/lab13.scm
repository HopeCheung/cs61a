; Q1
(define (compose-all funcs)
	(if (null? funcs)
		 (lambda (x) (+ x 0))
		 (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))
    )
)

; Q2
(define (tail-replicate x n)
  (define (replicate lst x c)
  	(if (= c 0)
  		lst
  		(replicate (append lst (cons x nil)) x (- c 1)) 
  	)
  )
  	(replicate () x n)
)