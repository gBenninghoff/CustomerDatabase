CREATE VIEW CurrentAppointments AS
SELECT * 
FROM Appointments
WHERE appt_date > GETDATE();
