(defn displayCourses []
  (println "displaying Courses: ") 
  #_{:clj-kondo/ignore [:inline-def]}
  (def courses (slurp "courses.txt"))
  (println courses))

(defn pickOption [choice]
  (case choice 1 (displayCourses)
        2 (println "2")
        3 (println "3")
        4 (println "4")
        5 (println "5")
        6 (println "6")
        7 (println "7")
        (println "Invalid option")))

(println "*** SIS Menu ***
         \n----------------
         \n1. Display Courses
         \n2. Display Students
         \n3. Display Grades
         \n4. Display Student Record
         \n5. Calculate GPA
         \n6. Course Average
         \n7. Exit
         \nEnter an option?")
(def x (read-line))
; (println (str "this is what was enetered\"" x "\""))
(pickOption (Integer/parseInt x))

