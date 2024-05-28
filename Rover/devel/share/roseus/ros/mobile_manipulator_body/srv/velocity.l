;; Auto-generated. Do not edit!


(when (boundp 'mobile_manipulator_body::velocity)
  (if (not (find-package "MOBILE_MANIPULATOR_BODY"))
    (make-package "MOBILE_MANIPULATOR_BODY"))
  (shadow 'velocity (find-package "MOBILE_MANIPULATOR_BODY")))
(unless (find-package "MOBILE_MANIPULATOR_BODY::VELOCITY")
  (make-package "MOBILE_MANIPULATOR_BODY::VELOCITY"))
(unless (find-package "MOBILE_MANIPULATOR_BODY::VELOCITYREQUEST")
  (make-package "MOBILE_MANIPULATOR_BODY::VELOCITYREQUEST"))
(unless (find-package "MOBILE_MANIPULATOR_BODY::VELOCITYRESPONSE")
  (make-package "MOBILE_MANIPULATOR_BODY::VELOCITYRESPONSE"))

(in-package "ROS")





(defclass mobile_manipulator_body::velocityRequest
  :super ros::object
  :slots (_sec_int ))

(defmethod mobile_manipulator_body::velocityRequest
  (:init
   (&key
    ((:sec_int __sec_int) 0)
    )
   (send-super :init)
   (setq _sec_int (round __sec_int))
   self)
  (:sec_int
   (&optional __sec_int)
   (if __sec_int (setq _sec_int __sec_int)) _sec_int)
  (:serialization-length
   ()
   (+
    ;; int32 _sec_int
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _sec_int
       (write-long _sec_int s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _sec_int
     (setq _sec_int (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass mobile_manipulator_body::velocityResponse
  :super ros::object
  :slots (_msg ))

(defmethod mobile_manipulator_body::velocityResponse
  (:init
   (&key
    ((:msg __msg) "")
    )
   (send-super :init)
   (setq _msg (string __msg))
   self)
  (:msg
   (&optional __msg)
   (if __msg (setq _msg __msg)) _msg)
  (:serialization-length
   ()
   (+
    ;; string _msg
    4 (length _msg)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _msg
       (write-long (length _msg) s) (princ _msg s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _msg
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _msg (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass mobile_manipulator_body::velocity
  :super ros::object
  :slots ())

(setf (get mobile_manipulator_body::velocity :md5sum-) "4a43c3133b1d7fcbde17a0d788417bc1")
(setf (get mobile_manipulator_body::velocity :datatype-) "mobile_manipulator_body/velocity")
(setf (get mobile_manipulator_body::velocity :request) mobile_manipulator_body::velocityRequest)
(setf (get mobile_manipulator_body::velocity :response) mobile_manipulator_body::velocityResponse)

(defmethod mobile_manipulator_body::velocityRequest
  (:response () (instance mobile_manipulator_body::velocityResponse :init)))

(setf (get mobile_manipulator_body::velocityRequest :md5sum-) "4a43c3133b1d7fcbde17a0d788417bc1")
(setf (get mobile_manipulator_body::velocityRequest :datatype-) "mobile_manipulator_body/velocityRequest")
(setf (get mobile_manipulator_body::velocityRequest :definition-)
      "int32 sec_int
---
string msg

")

(setf (get mobile_manipulator_body::velocityResponse :md5sum-) "4a43c3133b1d7fcbde17a0d788417bc1")
(setf (get mobile_manipulator_body::velocityResponse :datatype-) "mobile_manipulator_body/velocityResponse")
(setf (get mobile_manipulator_body::velocityResponse :definition-)
      "int32 sec_int
---
string msg

")



(provide :mobile_manipulator_body/velocity "4a43c3133b1d7fcbde17a0d788417bc1")


