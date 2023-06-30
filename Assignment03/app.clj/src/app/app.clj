(ns app
  (:require [db] [menu]))

;; Load data from the file
(def studDB 
  (db/load-data "studs.txt"))
(def courseDB 
  (db/load-data "courses.txt"))
(def gradesDB
  (db/load-data "grades.txt"))

;; Start the main menu loop
(menu/main-loop)
