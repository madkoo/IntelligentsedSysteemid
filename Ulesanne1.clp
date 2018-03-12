
;;;======================================================
;;;======================================================

(defmodule MAIN (export ?ALL))

;;****************
;;* DEFFUNCTIONS *
;;****************

(deffunction MAIN::ask-question (?question ?allowed-values ?number-question ?allowed-values)
   (printout t ?question and ?number-question)
   (bind ?answer (read))
   (if (lexemep ?answer) then (bind ?answer (lowcase ?answer)))
   (while (not (member ?answer ?allowed-values)) do
     (printout t ?question and ?number-question)
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
  (focus QUESTIONS CHOOSE-SHOP TRANSPORTS PRINT-RESULTS))

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


(deftemplate QUESTIONS::number-question
   (slot attribute (default ?NONE))
   (slot the-question (default ?NONE))
   (multislot valid-answers (type NUMBER) (default ?NONE))
   (slot already-asked (default FALSE))
   (multislot precursors (default ?DERIVE)))

    (defrule QUESTIONS::ask-a-question2
   ?f <- (number-question (already-asked FALSE)
                   (precursors)
                   (the-question ?the-question)
                   (attribute ?the-attribute)
                   (valid-answers $?valid-answers))
   =>
   (modify ?f (already-asked TRUE))
   (assert (attribute (name ?the-attribute)
                      (value (ask-question ?the-question ?valid-answers)))))

(defrule QUESTIONS::precursor-is-satisfied2
   ?f <- (number-question (already-asked FALSE)
                   (precursors ?name is ?value $?rest))
         (attribute (name ?name) (value ?value))
   =>
   (if (eq (nth 1 ?rest) and) 
    then (modify ?f (precursors (rest$ ?rest)))
    else (modify ?f (precursors ?rest))))

(defrule QUESTIONS::precursor-is-not-satisfied2
   ?f <- (number-question (already-asked FALSE)
                   (precursors ?name is-not ?value $?rest))
         (attribute (name ?name) (value ~?value))
   =>
   (if (eq (nth 1 ?rest) and) 
    then (modify ?f (precursors (rest$ ?rest)))
    else (modify ?f (precursors ?rest))))


(deftemplate QUESTIONS::question
   (slot attribute (default ?NONE))
   (slot the-question (default ?NONE))
   (multislot valid-answers (default ?NONE))
   (slot already-asked (default FALSE))
   (multislot precursors (default ?DERIVE)))

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

(question (attribute popularity)
            (the-question "Kas eelistad, et poes oleks vÃµimalikult vÃ¤he rahvast, jah vÃµi ei")
            (valid-answers jah ei))
(question (attribute handicaped)
            (the-question "Kas lähed ratastooli, vankri, mÃµlemaga vÃµi ilma?(vanker, ratastool, molemad, ei)")
            (valid-answers ratastool vanker molemad ei ))
(question (attribute maximum-people)
            (the-question "Kui palju inimesi poodi tootele järgi läheb?(nt 1,2,3,4,5)")
            (valid-answers 1 2 3 4 5))
(question (attribute language)
            (the-question "Mis keelt sa räägid? (inglise, vene, eesti, prantsuse, itaalia, hispaania)")
            (valid-answers inglise vene eesti prantsuse itaalia hispaania))
(question (attribute area)
            (the-question "Kas on oluline, et piirkond oleks turvaline, jah või ei ")
            (valid-answers jah ei))
  (question (attribute product)
            (the-question "Mida soovid osta, kas piim, leib, sai, viin")
            (valid-answers piim leib sai viin))
  (question (attribute preferred-selection-size)
            (the-question "Kui suur valik on poes sinu kaup, kas kauplus, supermarket, hypermarket?")
            (valid-answers kauplus supermarket hypermarket))
  (question (attribute expected-arrival)
            (the-question "Kui kiiresti soovid poodi jõuda, 5min, 30min, 1h, 2h?")
            (valid-answers 5min 30min 1h 2h))
  (question (attribute preferred-transport)
            (the-question "Millist transporti soovid kasutada kaubale järgi minemiseks, kas jalgsimatk, yhistransport, eratransport voi auto?")
            (valid-answers jalgsimatk yhistransport eratransport auto))
  (number-question (attribute maximum-budget)
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

  ; Rules for picking the best transport

  (rule (if maximum-budget is 5)
        (then best-transport is on-foot))
		
  (rule (if maximum-budget >= 0 and maximum-budget <=10)
        (then best-transport is on-foot))
  (rule (if maximum-budget >= 10 and maximum-budget <=20)
        (then best-transport is on yhistransport))

     ;jalgi matka reeglid 
  (rule (if maximum-budget >= 0 and maximum-budget <=10 and expected-arrival is 5min and handicaped is ei and maximum-people <= 2 and preferred-transport is jalgsimatk)
        (then best-transport is on jalgsi))
  
  (rule (if maximum-budget >= 0 and maximum-budget <=5 and expected-arrival is 30min and handicaped is ei and maximum-people <= 5 and preferred-transport is jalgsimatk)
        (then best-transport is on jalgsi))
  
  (rule (if maximum-budget >= 0 and maximum-budget <=5 and expected-arrival is 1h and handicaped is ei and maximum-people <= 5 and preferred-transport is jalgsimatk)
        (then best-transport is on jalgsi))
  
  (rule (if maximum-budget >= 0 and maximum-budget <=5 and expected-arrival is 2h and handicaped is ei and maximum-people <= 5 and preferred-transport is jalgsimatk)
        (then best-transport is jalgsi))

  (rule (if maximum-budget >= 0 and maximum-budget <=5 and handicaped is ei and maximum-people <= 5 and preferred-transport is yhistransport)
  (then best-transport is on jalgsi))
  
  (rule (if maximum-budget >= 0 and maximum-budget <=10 and expected-arrival is 1h and handicaped is ei and maximum-people <= 4 and preferred-transport is eratransport)
        (then best-transport is on jalgsi))
  
  ;uber , takso jne
        
  (rule (if maximum-budget >= 50 and maximum-budget <=100 and expected-arrival is 30min and handicaped is ei and maximum-people <= 4 and preferred-transport is eratransport)
        (then best-transport is on eratransport))
  
  (rule (if maximum-budget >= 50 and maximum-budget <=100 and expected-arrival is 5min and handicaped is ei and maximum-people <= 4 and preferred-transport is eratransport)
        (then best-transport is on eratransport))

  (rule (if maximum-budget >= 50 and maximum-budget <=100 and expected-arrival is 30min and handicaped is jah and maximum-people <= 4 and preferred-transport is eratransport)
        (then best-transport is on eratransport))
  
  (rule (if maximum-budget >= 50 and maximum-budget <=100 and expected-arrival is 5min and handicaped is jah and maximum-people <= 4 and preferred-transport is eratransport)
        (then best-transport is on eratransport))


      ;yhistranspordi reeglid
   
  (rule (if maximum-budget >= 10 and maximum-budget <= 49 and expected-arrival is 30min handicaped is ei and maximum-people <= 5 and preferred-transport is yhistransport)
        (then best-transport is on yhistransport))
  (rule (if maximum-budget >= 10 and maximum-budget <= 49 and expected-arrival is 30min handicaped is jah and maximum-people <= 5 and preferred-transport is yhistransport)
        (then best-transport is on yhistransport))
  (rule (if maximum-budget >= 10 and maximum-budget <= 49 and expected-arrival is 1h handicaped is ei and maximum-people <= 5 and preferred-transport is yhistransport)
        (then best-transport is on yhistransport))
  (rule (if maximum-budget >= 10 and maximum-budget <= 49 and expected-arrival is 1h handicaped is jah and maximum-people <= 5 and preferred-transport is yhistransport)
        (then best-transport is on yhistransport))
  (rule (if maximum-budget >= 10 and maximum-budget <= 49 and expected-arrival is 2h handicaped is jah and maximum-people <= 5 and preferred-transport is yhistransport)
        (then best-transport is on yhistransport))
  (rule (if maximum-budget >= 10 and maximum-budget <= 49 and expected-arrival is 2h handicaped is ei and maximum-people <= 5 and preferred-transport is yhistransport)
        (then best-transport is on yhistransport))


  ; Rules product best product price

  ; Rules product best shop location and name

  ; Rules product best transport


  
)

;;************************
;;* SHOPS SELECTION RULES
;;************************

(defmodule SHOPS (import MAIN ?ALL))

;valjundmoisted
(deffacts any-attributes
  (attribute (name product-budget) (value any))
  (attribute (name best-transport) (value any))
  (attribute (name transport-budget) (value any))
  (attribute (name best-transport-time) (value any))
  (attribute (name parking-wish) (value any))
  (attribute (name parking-can-pay) (value any))
  (attribute (name language) (value any))
  (attribute (name wheelchair-or-pram) (value any))
  (attribute (name best-crowd) (value any))
  (attribute (name best-selection-size) (value any))
  
  )

;poodide valjad
(deftemplate SHOPS::shop
  (slot name (default ?NONE))
  (multislot product-price(default any))
  (multislot transport(default any))
  (multislot transport-price(default any))
  (multislot transport-time(default any))
  (multislot parking(default any))
  (multislot parking-charge(default any))
  (multislot service-language(default any))
  (multislot wheelchair-accessibility(default any))
  (multislot crowd(default any))
  (multislot selection-size(default any)))

; poodide nimekiri
(deffacts SHOPS::the-shop-list 
  (shop (name Rimi) (product-price 10) (transport jalgsi) (transport-price 0) (transport-time 1h) (parking yes) (parking-charge yes) 
    (service-language estonian) (wheelchair-accessibility no) (crowd no) (selection-size hypermarket))
  (shop (name Felixi-kaubad) (product-price 15) (transport yhistransport) (transport-price 3) (transport-time 10min) (parking no)
    (service-language estonian) (wheelchair-accessibility yes) (crowd no) (selection-size kauplus))
)
  
(defrule SHOPS::generate-shops
  (shop (name ?name)
        (product-price $? ?pp $?)
        (transport $? ?t $?)
        (transport-price $? ?tp $?)
        (transport-time $? ?tt $?)
        (parking $? ?p $?)
        (parking-charge $? ?pc $?)
        (service-language $? ?sl $?)
        (wheelchair-accessibility $? ?wa $?)
        (crowd $? ?c $?)
        (selection-size $? ?ss $?))
  (attribute (name product-budget) (value ?pp))
  (attribute (name best-transport) (value ?t))
  (attribute (name transport-budget) (value ?tp))
  (attribute (name best-transport-time) (value ?tt))
  (attribute (name parking-wish) (value ?p))
  (attribute (name parking-can-pay) (value ?pc))
  (attribute (name language) (value ?sl))
  (attribute (name wheelchair-or-pram) (value ?wa))
  (attribute (name best-crowd) (value ?c))
  (attribute (name best-selection-size) (value ?ss))
  =>
  (assert (attribute (name shop) (value ?name))))

;;*****************************
;;* PRINT SELECTED  RULES  prindime tulemused  peab muutma *
;;*****************************

(defmodule PRINT-RESULTS (import MAIN ?ALL))

(defrule PRINT-RESULTS::header ""
   (declare (salience 10))
   =>
   (printout t t)
   (printout t " -------------------------------" t)
   (assert (phase print-wines)))

(defrule PRINT-RESULTS::print-wine ""
  ?rem <- (attribute (name dd) (value ?name) (certainty ?per))		  
  (not (attribute (name transport) (certainty ?per1&:(> ?per1 ?per))))
  =>
  (retract ?rem)
  (format t " %-24s %2d%%%n" ?name ?per))

(defrule PRINT-RESULTS::remove-poor-wine-choices ""
  ?rem <- (attribute (name transport) (certainty ?per&:(< ?per 20)))
  =>
  (retract ?rem))

(defrule PRINT-RESULTS::end-spaces ""
   (not (attribute (name transport)))
   =>
   (printout t t))
