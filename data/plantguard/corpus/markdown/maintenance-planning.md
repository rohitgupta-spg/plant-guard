# Preventive Maintenance Planning Standard

**DOCUMENT ID:** VPW-SOP-ENG-412  
**EFFECTIVE DATE:** 14 January 2026  
**SUBJECT:** Preventive and Predictive Maintenance Planning Standard  
**AUTHOR:** Marcus Vance, Maintenance Engineering Lead  
**APPLIES TO:** All Plant Technicians, Reliability Engineers, and Maintenance Planners at Vindhya Precision Works  

---

### 1.0 PURPOSE AND SCOPE
1.1 This standard defines the mandatory intervals, classification criteria, work order generation rules, and scheduling priority protocols for all mechanical, electrical, and pneumatic assets at Vindhya Precision Works.  
1.2 Compliance with this standard is mandatory for all maintenance personnel. Deviations require written authorization from the Maintenance Engineering Lead.

---

### 2.0 ASSET CRITICALITY CLASSIFICATION AND INSPECTION INTERVALS
2.1 All plant assets shall be assigned a Criticality Classification of A, B, or C based on safety risk, environmental impact, and production downtime cost as determined by the Reliability Committee.  

2.2 **Criticality A (High Criticality):**  
*   **Definition:** Assets whose failure results in total plant shutdown, severe environmental breach, or immediate safety hazard (e.g., Primary Stamping Press Line 04, Main Induction Furnaces).  
*   **Inspection Interval:** Every 7 calendar days ($\pm$ 4 hours).  
*   **Mandatory Task Type:** Dynamic vibration analysis, thermographic scan of electrical panels, lubrication top-up, and visual wear inspection.

2.3 **Criticality B (Medium Criticality):**  
*   **Definition:** Assets whose failure results in reduced line output or significant secondary repair costs, but does not halt the entire facility (e.g., Sub-Assembly Conveyor Belts 01 through 08, Automated Guided Vehicles).  
*   **Inspection Interval:** Every 30 calendar days ($\pm$ 24 hours).  
*   **Mandatory Task Type:** Visual inspection, belt tension verification, filter replacement, and acoustic bearing checks.

2.4 **Criticality C (Low Criticality):**  
*   **Definition:** Non-essential assets with installed redundancy or those whose failure causes negligible impact on production schedules (e.g., Exhaust Fan Units in Warehouse B, Tool Room Bench Grinders).  
*   **Inspection Interval:** Every 90 calendar days ($\pm$ 72 hours).  
*   **Mandatory Task Type:** General cleaning, mechanical fastener torque check, and manual lubrication.

---

### 3.0 CONDITION-MONITORING (CM) TO WORK ORDER CONVERSION RULE
3.1 Condition-monitoring data collected via the Enterprise Asset Management (EAM) system shall be evaluated automatically against predefined baseline thresholds.  

3.2 **Conversion Trigger:** When a condition-monitoring parameter (e.g., vibration velocity in mm/s RMS, oil particulate count, or motor winding temperature) exceeds **80%** of the ISO 10816 alarm threshold, the predictive maintenance software shall automatically generate a Corrective Work Order (CMWO) within **2 hours** of data ingestion.  

3.3 The generated CMWO must be reviewed by the assigned Reliability Engineer within **24 hours** to verify fault validity and assign craft resource codes.

---

### 4.0 BACKLOG THRESHOLD AND ESCALATION PROTOCOL
4.1 Maintenance backlog is defined as the total man-hours of approved, uncompleted work orders divided by the available technician man-hours per week.  

4.2 **Warning Threshold:** If the maintenance backlog exceeds **120%** of normal weekly capacity for two consecutive reporting periods, the Maintenance Planner shall issue an internal advisory to shift supervisors to freeze non-essential plant modifications.  

4.3 **Escalation Trigger:** If the maintenance backlog exceeds **150%** of normal weekly capacity (equivalent to 600 unexecuted man-hours across all crafts), or if any Criticality A work order remains unexecuted past its scheduled due date by more than **48 hours**, the following escalation chain is mandatory:  
1.  **Immediate Notification (Within 4 hours):** Written escalation report submitted by Marcus Vance (Maintenance Engineering Lead) to Plant Operations Director.  
2.  **Action Mandate:** Mandatory authorization of weekend overtime shifts for off-schedule Tier A assets, or invocation of Service Level Agreements (SLAs) with approved external contractors (Vindhya-certified vendors only).

---

### 5.0 PLANNING HORIZON
5.1 The maintenance planning horizon at Vindhya Precision Works shall operate on a rolling **12-week** cycle.  

5.2 **Week 1 (Frozen Schedule):** No modifications permitted except for emergency break-in work orders approved by the Shift Maintenance Supervisor.  

5.3 **Weeks 2 through 4 (Locked Window):** Resource-leveled and scheduled tasks with confirmed spare parts availability in the central stores warehouse.  

5.4 **Weeks 5 through 12 (Indicative Window):** Demand forecasts based on historical asset degradation models, preventive maintenance intervals, and projected major overhaul windows.

---

### 6.0 PRIORITIZATION: PREDICTIVE ALERTS VS. SCHEDULED TASKS
6.1 When a predictive alert (generated per Section 3.0) conflicts with a pre-scheduled preventive maintenance task, the following strict hierarchy of execution applies:  

*   **Priority 1:** Emergency Break-In / Unplanned Plant Safety Stops  
*   **Priority 2:** Predictive Alert Work Orders (Condition-Monitoring triggers at >80% threshold)  
*   **Priority 3:** Criticality A Scheduled Preventive Maintenance Tasks  
*   **Priority 4:** Criticality B & C Scheduled Preventive Maintenance Tasks  
*   **Priority 5:** Plant Improvement and Modification Projects  

6.2 **Rescheduling Protocol:** If a Priority 2 predictive alert supersedes a Priority 3 or 4 scheduled task, the Maintenance Planner shall automatically defer the scheduled task. The deferred task must be rescheduled and executed within **14 calendar days** of its original due date to prevent asset drift. Under no circumstances may a Criticality A scheduled inspection be deferred more than once.
