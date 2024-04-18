CREATE VIEW ServicePull AS
SELECT service_id, ServiceRecord.customer_id, service_cost, cu_first_name, cu_last_name
FROM ServiceRecord JOIN Customer ON ServiceRecord.customer_id = Customer.customer_id