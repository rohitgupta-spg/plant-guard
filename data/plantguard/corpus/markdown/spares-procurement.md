# Spare Parts and Procurement Policy

**VIN-SOP-ENG-041**  
**Subject:** Spare Parts Inventory Control and Procurement Standard  
**Facility:** Vindhya Precision Works, Plant No. 3, Industrial Area Phase II, Bhopal  
**Effective Date:** 14 January 2026  
**Supersedes:** VIN-SOP-ENG-038  

---

### 1. Purpose and Scope
This document defines mandatory operational rules for the classification, minimum stock levels, reorder calculation, supplier tiering, purchasing thresholds, and obsolescence reviews for all mechanical, electrical, and pneumatic spare parts held in the Vindhya Precision Works central stores. Compliance is mandatory for all maintenance engineers, stores personnel, and procurement officers.

---

### 2. Criticality-Based Minimum Stock Rules
Parts stored in the central inventory shall be assigned a Criticality Rating of A, B, or C by the Maintenance Engineering Lead. Minimum stock levels—defined as the safety stock plus lead-time demand—shall be maintained strictly according to Table 1.

**Table 1: Criticality Parameters and Minimum Stock Rules**

| Criticality Rating | Definition / Asset Impact | Minimum Stock Rule (Safety Stock + Lead-Time Demand) | Physical Count Audit Frequency |
| :--- | :--- | :--- | :--- |
| **Class A** | Single-point failure halts primary manufacturing line; no local fallback available. | 30 days safety stock + lead-time consumption; absolute minimum floor of **2 units** for all rotating and electrical assets. | Monthly (1st working day) |
| **Class B** | Failure reduces line speed by $\ge 30\%$ or impacts secondary sub-assemblies. | 15 days safety stock + lead-time consumption; absolute minimum floor of **1 unit**. | Quarterly |
| **Class C** | Consumables, general hardware, filters, and non-critical wear items. | 7 days safety stock + lead-time consumption; minimum floor of **5 units** (where applicable). | Bi-annually |

*Exception:* Custom-machined shaft assemblies and specialized CNC spindle bearings (Drawing Nos. VPW-SP-101 through VPW-SP-115) are exempt from the standard minimum floor and shall be held strictly at a maximum and minimum stock level of exactly **1 unit** due to rapid metallurgical degradation under ambient warehouse humidity.

---

### 3. Reorder Point Calculation and Worked Example

#### 3.1 Formula
The Reorder Point (ROP) for any spare part shall be calculated using the following deterministic formula:

$$\text{ROP} = (\text{Average Daily Consumption} \times \text{Supplier Lead Time in Days}) + \text{Safety Stock}$$

Where:
*   $\text{Average Daily Consumption (ADC)}$ = Total units consumed over the preceding 365 calendar days divided by 365.
*   $\text{Supplier Lead Time (SLT)}$ = Confirmed delivery duration in days specified in the approved supplier tier agreement.
*   $\text{Safety Stock (SS)}$ = $(\text{Maximum Daily Consumption} - \text{Average Daily Consumption}) \times \text{Maximum Lead Time Variance in Days}$. For planning purposes, Lead Time Variance is fixed at **5 days** for Tier 1 suppliers and **10 days** for Tier 2 suppliers.

#### 3.2 Worked Example: Hydraulic Solenoid Valve (Part No. V-HYD-442)
*   **Asset:** Main clamping hydraulic press (Line 2)
*   **Total Consumption over Past Year:** 73 units
*   **Maximum Daily Consumption ($DC_{\max}$):** 1 unit/day (recorded during peak summer thermal expansion events)
*   **Supplier Tier:** Tier 2 (Standard industrial distributor)
*   **Supplier Lead Time ($SLT$):** 14 days
*   **Lead Time Variance:** 10 days

**Calculation Steps:**
1.  $\text{ADC} = \frac{73}{365} = 0.20 \text{ units/day}$
2.  $\text{Lead-Time Demand} = 0.20 \times 14 = 2.80 \text{ units}$
3.  $\text{Safety Stock} = (1.0 - 0.20) \times 10 = 0.80 \times 10 = 8.0 \text{ units}$
4.  $\text{ROP} = 2.80 + 8.0 = 10.80 \text{ units}$

Rounding up to the nearest whole integer per inventory policy, the **Reorder Point (ROP)** for Part No. V-HYD-442 is **11 units**. When physical inventory plus open purchase orders drops to or below 11 units, an automated replenishment requisition is triggered.

---

### 4. Approved Supplier Tiers and Lead Times
All spare parts procurement must be routed through suppliers categorized into three approved tiers, as listed in Table 2.

**Table 2: Approved Supplier Tiers**

| Supplier Tier | Classification Criteria | Standard Lead Time (Days) | Authorized Procurement Scope |
| :--- | :--- | :--- | :--- |
| **Tier 1** | Original Equipment Manufacturers (OEMs) and exclusive global distributors under active annual rate contract. | **7 days** | Class A critical items, proprietary electronics, PLC modules, precision gearboxes. |
| **Tier 2** | Regional stockists, certified secondary distributors, and vetted regional fabricators. | **14 days** | Class B standard mechanical components, valves, standard motors, hydraulic hoses. |
| **Tier 3** | Local hardware vendors, raw material stockists, and general industrial merchants. | **21 days** | Class C consumables, fasteners, gaskets, basic pneumatic fittings, lubricants. |

---

### 5. Emergency-Purchase Authorisation Thresholds
When an unplanned line stoppage occurs and required spares are not available in central stores, emergency purchases may be executed outside standard replenishment cycles. Thresholds, financial limits in Indian Rupees (INR), and mandatory signatories are defined in Table 3.

**Table 3: Emergency Purchase Authorities**

| Threshold Limit (INR) | Mandatory Authorization Role | Permitted Processing Window | Documentation Requirement |
| :--- | :--- | :--- | :--- |
| **Up to ₹25,000** | Shift Maintenance Supervisor | Immediate verbal release; PO generation within 4 hours. | Stores log entry + equipment failure ticket ID. |
| **₹25,001 to ₹100,000** | Maintenance Engineering Lead | Written email authorization prior to vendor dispatch. | Emergency Requisition Form (ERF) signed by Lead. |
| **₹100,001 to ₹500,000** | Plant Operations Manager | Formal signed physical or digital approval slip. | ERF + technical justification memo. |
| **Above ₹500,000** | General Works Manager (GWM) | Executive sign-off required prior to order placement. | Capital/Emergency Board Memo + 3 competitive quotes. |

---

### 6. Automated Purchase Order Restrictions
To prevent systemic purchasing errors and unmonitored financial exposure, no purchase order valued above **₹200,000 (Two Hundred Thousand Indian Rupees)** may be raised automatically by the Enterprise Resource Planning (ERP) or Computerized Maintenance Management System (CMMS), regardless of inventory depletion levels or pre-set ROP parameters.

*   Any system-generated requirement exceeding ₹200,000 shall be routed to a "Pending Manual Review" queue.
*   Release from this queue requires the dual digital sign-off of the Procurement Officer and the Maintenance Engineering Lead.
*   *Exception:* Direct raw material stock-outs declared under a plant-wide emergency disaster protocol by the General Works Manager are exempt from this restriction for a maximum duration of 24 hours.

---

### 7. Obsolescence Review Cadence
To prevent capital lockup in dead inventory and ensure compatibility with active machinery, formal obsolescence reviews shall be conducted according to the following cadence:

*   **Cadence:** Every **180 days** (biannually), ending on the final working day of June and December.
*   **Review Committee:** Comprising the Maintenance Engineering Lead, Stores Manager, and Plant Financial Controller.
*   **Triggers for Obsolescence:** 
    1. Zero inventory transactions (neither issue nor receipt) for 730 consecutive days.
    2. Associated parent machine or production line decommissioned and removed from the active plant asset register.
    3. Formal vendor notification of component phase-out or obsolescence.
*   **Disposal Workflow:** Parts identified as obsolete shall be quarantined for 30 days, offered for inter-plant transfer to sister facilities within the Vindhya group for 15 days, and subsequently authorized for scrap disposal or auction by the Plant Financial Controller.

---
**Document Authentication:**

*Authorised by:*  
R. K. Sharma  
General Works Manager  
Vindhya Precision Works  

*Issued by:*  
A. P. Deshmukh  
Maintenance Engineering Lead  
Vindhya Precision Works
