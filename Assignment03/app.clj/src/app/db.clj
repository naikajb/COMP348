(ns db
  (:require [clojure.string :as str]))

;needs to process the rows of the file
; creates a MAP 
(defn checkRow [line]
  (let [[id name phone] (str/split line #"\|")]
    {:studID id
     :name name
     :phoneNum phone}))

;load the data 
(defn load-data [filename]
  (->> (slurp filename)
       (str/split-lines)
       (map checkRow)))

;functions loading info from files
(def studDB (load-data "studs.txt"))
(def courseDB (load-data "courses.txt"))
(def gradesDB (load-data "grades.txt"))

;getter to return student info from the id input
(defn get-student [studID]
  (first (filter #(= studID (:studID %)) studDB)))

;map needed to get the grades and their numerical values
(def grades-map
  {"A+" 4.3 "A" 4 "A-" 3.7
   "B+" 3.3 "B" 3 "B-" 2.7
   "C+" 2.3 "C" 2 "C-" 1.7
   "D+" 1.3 "D" 1 "D-" 0.7
   "F" 0})

(defn grade-to-numeric [grade]
  (grades-map grade))

;; Function to calculate GPA for a given student
(defn calculate-gpa [studID]
  (let [grades (get-grades studID)
        credits (map #(get-course (:courseID %)) grades)
        grade-credits (map #(grade-to-numeric (:grade %) * (get-course (:credits %))) grades)
        total-credits (reduce + credits)
        weighted-sum (reduce + grade-credits)]
    (/ weighted-sum total-credits)))

;; Function to calculate the average grade for a course based on letter grades
(defn calculate-average [courseID]
  (let [grades (filter #(= courseID (:courseID %)) gradesDB)
        grades-numeric (map #(grade-to-numeric (:grade %)) grades)
        average (if (seq grades-numeric) (/ (reduce + grades-numeric) (count grades-numeric)) 0)]
    average))

;; Export the necessary functions
(defn get-student-record [studID]
  (let [student (get-student studID)
        student-courses (get-grades studID)
        courses-info (map #(get-course (:courseID %)) student-courses)]
    (into [student] courses-info)))

(defn display-students []
  (doseq [student studDB]
    (println (vals student))))

(defn display-courses []
  (doseq [course courseDB]
    (println (vals course))))

(defn display-grades []
  (doseq [grade gradesDB]
    (println (vals grade))))
