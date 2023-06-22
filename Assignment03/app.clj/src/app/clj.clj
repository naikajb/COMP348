(ns app.clj
  (:gen-class))
(defn displayCourses []
  (println "displaying Courses: ")
  ;; (def courses (slurp "courses.txt"))
  ;; (println courses)
  (def courses (slurp "courses.txt"))
  (println courses))

(defn displayStudents []
  (println "displaying Students: ")
  (def students (slurp "studs.txt"))
  (println students))

(defn displayGrades []
  (println "displaying Grades: ")
  (def grades (slurp "grades.txt"))
  (println grades))

(defn pickOption [choice]
  (case choice 1 (displayCourses)
        2 (displayStudents)
        3 (displayGrades)
        4 (println "4")
        5 (println "5")
        6 (println "6")
        7 (println "Quitting...")
        (println "Invalid option")))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  ;(println "Hello, World!")
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
  (pickOption (Integer/parseInt x))
  
)

;; (def x (read-line))
;; ; (println (str "this is what was enetered\"" x "\""))
;; (pickOption (Integer/parseInt x))

