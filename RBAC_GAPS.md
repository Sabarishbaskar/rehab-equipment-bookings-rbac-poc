# RBAC Gaps Identified

1.The role permissions are currently defined directly in the code. Any change to roles or permissions would require a code update and redeployment of the application. 

2.Assigned staff users can mark any booking  as completed. In a real-world system, staff should only be able to perform actions on bookings assigned to them.

3.The current implementation allows only one role per user. If a user needs multiple roles in the future, the system would need to be enhanced.

4.Actions such as booking cancellation and marking a booking as completed are not logged. Adding audit logs would help track who performed an action and when it was performed.