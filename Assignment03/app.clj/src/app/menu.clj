(ns menu
  (:require [db]))
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

(defn displayMenu []
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
    (flush))

(defn readOption []
  (let [input (read-line)]
    (Integer/parseInt input)))
;; (defn pickOption [choice]
;;   (case choice 1 (displayCourses)
;;         2 (displayStudents)
;;         3 (displayGrades)
;;         4 (println "4")
;;         5 (println "5")
;;         6 (println "6")
;;         7 (println "Quitting...")
;;         (println "Invalid option")))

(defn -main-loop []
  (while true
    (try 
      (displayMenu)
      (let [option (readOption)]
        (cond 
          (= option 1) (db/display-courses)
          (= option 2) (db/display-students)
          (= option 3) (db/display-grades)
          (= option 4) (do
                        (print "Enter student ID: ")
                        (let [studID (read-line)]
                          (doseq [course-info (db/get-student-record studID)]
                            (println course-info))))
          (= option 5) (do
                        (print "Enter student ID: ")
                        (let [studID (read-line)]
                          (println (str "GPA for student " studID ": " (db/calculate-gpa studID)))))
          
           (= option 6) (do
                        (print "Enter course ID: ")
                        (let [courseID (read-line)]
                          (println (str "Course average for course " courseID ": " (db/calculate-course-average courseID)))))
          (= option 7) (do
                        (println "Exiting...")
                        (System/exit 0))
          :else (println "Invalid option. Please try again."))))
    (catch Exception e
      (println "Error occurred: " (.getMessage e)))))

(main-loop)

;; (def x (read-line))
;; ; (println (str "this is what was enetered\"" x "\""))
;; (pickOption (Integer/parseInt x))

