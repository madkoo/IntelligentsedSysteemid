
;;;======================================================
;;;======================================================

(defmodule MAIN (export ?ALL))

;;****************
;;* DEFFUNCTIONS *
;;****************

(deffunction MAIN::ask-question (?question ?allowed-values)
   (printout t ?question)
   (bind ?answer (read))
   (if (lexemep ?answer) then (bind ?answer (lowcase ?answer)))
   (while (not (member ?answer ?allowed-values)) do
      (printout t ?question)
      (bind ?answer (read))
      (if (lexemep ?answer) then (bind ?answer (lowcase ?answer))))
   ?answer)

;;*****************
;;* INITIAL STATE *
;;*****************

(deftemplate MAIN::attribute
   (slot name)
   (slot value)
   (slot certainty (default 100.0)))

(defrule MAIN::start
  (declare (salience 10000))
  =>
  (set-fact-duplication TRUE)
  (focus QUESTIONS PRINT-RESULTS))

(defrule MAIN::combine-certainties ""
  (declare (salience 100)
           (auto-focus TRUE))
  ?rem1 <- (attribute (name ?rel) (value ?val) (certainty ?per1))
  ?rem2 <- (attribute (name ?rel) (value ?val) (certainty ?per2))
  (test (neq ?rem1 ?rem2))
  =>
  (retract ?rem1)
  (modify ?rem2 (certainty (/ (- (* 100 (+ ?per1 ?per2)) (* ?per1 ?per2)) 100))))
  
;;******************
;;* QUESTION RULES *
;;******************

(defmodule QUESTIONS (import MAIN ?ALL) (export ?ALL))

(deftemplate QUESTION::range-question
  (slot attribute (default ?NONE))
  (slot the-question (default ?NONE))
  (multislot valid-answers (type NUMBER) (default ?NONE))
  (slot already-asked (default FALSE))
  (multislot precursors (default ?DERIVE)))

(deftemplate QUESTIONS::question
   (slot attribute (default ?NONE))
   (slot the-question (default ?NONE))
   (multislot valid-answers (default ?NONE))
   (slot already-asked (default FALSE))
   (multislot precursors (default ?DERIVE)))
   

(defrule QUESTIONS::ask-a-question
   ?f <- (range-question (already-asked FALSE)
                   (precursors)
                   (the-question ?the-question)
                   (attribute ?the-attribute)
                   (valid-answers $?valid-answers))
   =>
   (modify ?f (already-asked TRUE))
   (assert (attribute (name ?the-attribute)
                      (value (ask-question ?the-question ?valid-answers)))))

(defrule QUESTIONS::precursor-is-satisfied
   ?f <- (range-question (already-asked FALSE)
                   (precursors ?name is ?value $?rest))
         (attribute (name ?name) (value ?value))
   =>
   (if (eq (nth 1 ?rest) and) 
    then (modify ?f (precursors (rest$ ?rest)))
    else (modify ?f (precursors ?rest))))

(defrule QUESTIONS::precursor-is-not-satisfied
   ?f <- (range-question (already-asked FALSE)
                   (precursors ?name is-not ?value $?rest))
         (attribute (name ?name) (value ~?value))
   =>
   (if (eq (nth 1 ?rest) and) 
    then (modify ?f (precursors (rest$ ?rest)))
    else (modify ?f (precursors ?rest))))

(defrule QUESTIONS::ask-a-question
   ?f <- (question (already-asked FALSE)
                   (precursors)
                   (the-question ?the-question)
                   (attribute ?the-attribute)
                   (valid-answers $?valid-answers))
   =>
   (modify ?f (already-asked TRUE))
   (assert (attribute (name ?the-attribute)
                      (value (ask-question ?the-question ?valid-answers)))))

(defrule QUESTIONS::precursor-is-satisfied
   ?f <- (question (already-asked FALSE)
                   (precursors ?name is ?value $?rest))
         (attribute (name ?name) (value ?value))
   =>
   (if (eq (nth 1 ?rest) and) 
    then (modify ?f (precursors (rest$ ?rest)))
    else (modify ?f (precursors ?rest))))

(defrule QUESTIONS::precursor-is-not-satisfied
   ?f <- (question (already-asked FALSE)
                   (precursors ?name is-not ?value $?rest))
         (attribute (name ?name) (value ~?value))
   =>
   (if (eq (nth 1 ?rest) and) 
    then (modify ?f (precursors (rest$ ?rest)))
    else (modify ?f (precursors ?rest))))

;;*******************
;;* Defineerime küsimusedS *
;;*******************

(defmodule TEST-QUESTIONS (import QUESTIONS ?ALL))


(deffacts TEST-QUESTIONS::question-attributes   

(question (attribute expected-arrival)
            (the-question "Kui suur valik on poes sinu kaup, kas kauplus, supermarket, hypermarket?")
            (valid-answers kauplus supermarket hypermarket)))
  (question (attribute expected-arrival)
            (the-question "Kui kiiresti soovid poodi jõuda, 5min, 30min, 1h, 2h ")
            (valid-answers 5min 30min 1h 2h))) 
  (question (attribute preferred-transport)
            (the-question "Millist transporti soovid kasutada kaubale järgi minemiseks, kas jalgsimatk, yhistransport, eratransport voi auto?")
            (valid-answers jalgsimatk yhistransport eratransport auto))) 
  (range-question (attribute maximum-budget)
            (the-question "Kui suure summa oled valmis kulutada kaubale ja transpordile poodi? 5, 10, 25 ,50 ,100")
            (valid-answers 5 10 25 50 100))) 

 
;;******************
;; The RULES module
;; See j22b veidi kysimargialla
;;******************

(defmodule RULES (import MAIN ?ALL) (export ?ALL))

(deftemplate RULES::rule
  (slot certainty (default 100.0))
  (multislot if)
  (multislot then))

(defrule RULES::throw-away-ands-in-antecedent
  ?f <- (rule (if and $?rest))
  =>
  (modify ?f (if ?rest)))

(defrule RULES::throw-away-ands-in-consequent
  ?f <- (rule (then and $?rest))
  =>
  (modify ?f (then ?rest)))

(defrule RULES::remove-is-condition-when-satisfied
  ?f <- (rule (certainty ?c1) 
              (if ?attribute is ?value $?rest))
  (attribute (name ?attribute) 
             (value ?value) 
             (certainty ?c2))
  =>
  (modify ?f (certainty (min ?c1 ?c2)) (if ?rest)))

(defrule RULES::remove-is-not-condition-when-satisfied
  ?f <- (rule (certainty ?c1) 
              (if ?attribute is-not ?value $?rest))
  (attribute (name ?attribute) (value ~?value) (certainty ?c2))
  =>
  (modify ?f (certainty (min ?c1 ?c2)) (if ?rest)))

(defrule RULES::perform-rule-consequent-with-certainty
  ?f <- (rule (certainty ?c1) 
              (if) 
              (then ?attribute is ?value with certainty ?c2 $?rest))
  =>
  (modify ?f (then ?rest))
  (assert (attribute (name ?attribute) 
                     (value ?value)
                     (certainty (/ (* ?c1 ?c2) 100)))))

(defrule RULES::perform-rule-consequent-without-certainty
  ?f <- (rule (certainty ?c1)
              (if)
              (then ?attribute is ?value $?rest))
  (test (or (eq (length$ ?rest) 0)
            (neq (nth 1 ?rest) with)))
  =>
  (modify ?f (then ?rest))
  (assert (attribute (name ?attribute) (value ?value) (certainty ?c1))))

;;*******************************
;;* Reeglid meie valikute osas  parima poe valikus*
;;*******************************

(defmodule CHOOSE-SHOP (import RULES ?ALL)
                            (import QUESTIONS ?ALL)
                            (import MAIN ?ALL))

(defrule CHOOSE-SHOP::startit => (focus RULES))

(deffacts the-shop-rules

  ; Rules for picking the best shop

  (rule (if maximum-budget >= 0 and maximum-budget <=10)
        (then transport is on Foot))

  
)

;;************************
;;* OPTIONS SELECTION RULES  PEAME MUUTMA MINGIT MOODI*
;;************************

(defmodule OPTIONS (import MAIN ?ALL))

(deffacts any-attributes
  (attribute (name transport) (value any))

(deftemplate OPTIONS::option
  (slot name (default ?NONE))
  (multislot transport(default any)))

(deffacts OPTIONS::the-wine-list 
  (result (name Tulemus) (transport Jalgsi)))
  
(defrule OPTIONS::generate-wines
  (result (name ?name)
        (transport $? ?c $?))
  (attribute (name best-color) (value ?c) (certainty ?certainty-1))
  =>
  (assert (attribute (name result) (value ?name)
                     (certainty (min ?certainty-1 ?certainty-2 ?certainty-3)))))

;;*****************************
;;* PRINT SELECTED WINE RULES  prindime tulemused  peab muutma *
;;*****************************

(defmodule PRINT-RESULTS (import MAIN ?ALL))

(defrule PRINT-RESULTS::header ""
   (declare (salience 10))
   =>
   (printout t t)
   (printout t " -------------------------------" t)
   (assert (phase print-wines)))

(defrule PRINT-RESULTS::print-wine ""
  ?rem <- (attribute (name result) (value ?name) (certainty ?per))		  
  (not (attribute (name result) (certainty ?per1&:(> ?per1 ?per))))
  =>
  (retract ?rem)
  (format t " %-24s %2d%%%n" ?name ?per))

(defrule PRINT-RESULTS::remove-poor-wine-choices ""
  ?rem <- (attribute (name result) (certainty ?per&:(< ?per 20)))
  =>
  (retract ?rem))

(defrule PRINT-RESULTS::end-spaces ""
   (not (attribute (name result)))
   =>
   (printout t t))




