ALTER VIEW CurrentAppointments AS
SELECT appt_id, service_id, appt_date, appt_time, Appointments.customer_id, cu_first_name, cu_last_name
FROM Appointments JOIN Customer ON Appointments.customer_id = Customer.customer_id
WHERE appt_date >= GETDATE();
