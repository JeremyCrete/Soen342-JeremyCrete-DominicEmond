## Consider the following requirements which you must specify in the Object Constraint Language.

English: Offerings are unique. In other words, multiple offerings on the same day and time slot must be offered at a different location.

OCL: ```context Offering```
</br>```inv: Offering.allInstances() --> forAll(of1, of2| of1 <> of2 implies (of1.date <> of2.date or of1.timeSlots <> of2.timeSlots or of1.location <> of2.location))```
</br>
</br>
English: Any client who is underage must necessarily be accompanied by an adult who acts as their guardian.

OCL: ```context Client```
</br>```inv: self.age < 18 implies self.guardian --> notEmpty()```
</br>
</br>
English: The city associated with an offering must be one the city’s that the instructor has indicated in their availabilities.

OCL: ```context Offering```
</br>```inv: self.instructor.availableCities --> includes(self.city)```
</br>
</br>
English: A client does not have multiple bookings on the same day and time slot.

OCL: ```context Client```
</br>```inv: self.Bookings --> forAll(bo1, bo2 | bo1 <> bo2 implies bo1.date <> bo2.date and bo1.timeSlot <> bo2.timeSlot)```
