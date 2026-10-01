# 400-Tonne Hydraulic Press (HYD-PRESS) Equipment Manual and SOP

# VINDHYA PRECISION WORKS
## EQUIPMENT MANUAL & MAINTENANCE SOP: 400-TONNE HYDRAULIC PRESS
### ASSET CLASS: HYD-PRESS (SERIAL RANGE: VPW-HP-400-010 through 045)
**Document ID:** SOP-MNT-HYD-400-Rev04  
**Effective Date:** 15 January 2025  
**Owner:** Maintenance Engineering Lead, Vindhya Precision Works  

---

## 1. OPERATING PARAMETERS, THRESHOLDS, AND ALARM SETPOINTS

All technicians operating or servicing asset class HYD-PRESS shall adhere strictly to the operational limits defined in Table 1.1. Operation outside these parameters without a signed variance from the Engineering Lead will result in immediate shutdown under Interlock Code E-99.

### Table 1.1: Operating Limits for HYD-PRESS Asset Class

| Parameter | Normal Operating Range | Warning / Pre-Alarm Setpoint | Critical Alarm / Trip Setpoint | Action on Trip |
| :--- | :--- | :--- | :--- | :--- |
| **Hydraulic Oil Temperature** | 38.0°C – 52.0°C | $\ge 58.0^{\circ}\text{C}$ (sustained 120s) | $\ge 65.0^{\circ}\text{C}$ (instantaneous) | Pump motor unloads; heat exchanger forced mode; locks out cycle start. |
| **Main System Pressure (Tonage Circuit)** | 0 – 28.5 MPa | $\ge 29.2\text{ MPa}$ | $\ge 31.5\text{ MPa}$ | Dump valve opens instantaneously; proportional relief vents to tank. |
| **Vibration Velocity (Main Axial Piston Pump)** | $0.8\text{ mm/s} – 3.2\text{ mm/s}$ RMS | $\ge 4.5\text{ mm/s}$ RMS | $\ge 7.1\text{ mm/s}$ RMS | Halts current stroke at top dead center (TDC); flags pump bearing wear. |
| **Main Drive Motor Current (415V AC)** | $75\text{ A} – 110\text{ A}$ | $\ge 125\text{ A}$ (duration > 5s) | $\ge 142\text{ A}$ (duration > 500ms) | Thermal overload trip; cuts main breaker MCB-04. |
| **Counterbalance Pressure Circuit** | $4.2\text{ MPa} – 5.0\text{ MPa}$ | $\le 3.8\text{ MPa}$ or $\ge 5.5\text{ MPa}$ | $\le 3.2\text{ MPa}$ or $\ge 6.0\text{ MPa}$ | Prevents ram descent; hydraulic brake applied. |
| **Die Cushion Pressure** | $8.0\text{ MPa} – 12.0\text{ MPa}$ | $\pm 10\text{%}$ of set recipe | $\pm 18\text{%}$ of set recipe | Pauses stroke at contact point; holds pressure for diagnostic review. |

---

## 2. PREVENTIVE MAINTENANCE SCHEDULE BY RUNNING HOURS

Maintenance intervals are dictated strictly by the Allen-Bradley PLC running-hour register `HMI_RUN_HRS_HYD400`. No grace periods are permitted. Running hours exceeding schedule triggers an unresettable PLC lockout.

### 2.1 Interval Classifications
* **PM-250 (Every 250 Running Hours ± 10 hrs):**
  1. Inspect primary hydraulic reservoir fluid level via sight glass; top up with Vindhya Grade ISO VG 46 anti-wear oil only if level drops below 60% of mark.
  2. Inspect main column guide bronze bushings for grease film continuity; apply NLGI Grade 2 lithium complex grease via central auto-lube injector manual override port (3 strokes per point).
  3. Clean optical safety light curtains (SICK C4000 series) with isopropyl alcohol and verify muting sensor alignment.
  4. Inspect proportional pressure relief valve subplate for weeping seals.

* **PM-1000 (Every 1,000 Running Hours ± 25 hrs):**
  1. Execute all PM-250 tasks.
  2. Replace return line filter elements (Part No. VPW-FLT-RET-400); record differential pressure gauge reading (must not exceed 0.15 MPa clean).
  3. Take 250ml hydraulic oil sample from lower reservoir drain port for third-party spectrometric and particle count analysis (Target: ISO 4406 cleanliness code 16/14/11 max).
  4. Verify mechanical ram fall-back check valves for seat leakage. Test drop must not exceed $0.5\text{ mm}$ over 15 minutes at 400 tonnes static load.
  5. Inspect electrical cabinet terminal blocks for thermal discoloration using FLIR thermal imager (maximum allowable delta T over ambient is 15.0°C).

* **PM-4000 (Every 4,000 Running Hours ± 50 hrs):**
  1. Execute all PM-250 and PM-1000 tasks.
  2. Drain complete hydraulic reservoir (Capacity: 1,200 Litres); flush tank floor with lint-free wipes; inspect and clean magnetic chip collectors.
  3. Replace main high-pressure circuit micron elements (Part No. VPW-FLT-HP-400).
  4. Calibrate tonnage load cells (4x shear beam under bolster plate) using certified hydraulic dead-weight tester reference standards.
  5. Check main frame tie-rod elongation and retorque nuts to engineering specification (Section 5).
  6. Replace proportional valve pilot filter cartridges (Part No. VPW-FLT-PV-02).

---

## 3. FAULT-CODE TROUBLESHOOTING MATRIX

When a fault code is registered on the Siemens HMI, technicians shall reference Table 3.1. Diagnosis must follow the causal chain and corrective action sequentially.

### Table 3.1: Fault-Code Table for HYD-PRESS

| Fault Code | Display Text | Probable Cause | Corrective Action | Safety Critical? (Lockout Required) |
| :--- | :--- | :--- | :--- | :--- |
| **F-101** | `MAIN_PUMP_FAIL_TO_PRIME` | Air trapped in suction line; closed ball valve V-02; blocked suction strainer element. | 1. Verify manual ball valve V-02 downstream of reservoir is 100% open.<br>2. Check suction line strainer for particulate blockage.<br>3. Bleed pump casing via high-point bleed screw until solid oil flow is achieved. | **YES** (LOTO / PTW Required) |
| **F-204** | `RAM_SKEW_EXCEEDED` | LVDT feedback discrepancy between left (LVDT-01) and right (LVDT-02) master cylinders > $0.75\text{ mm}$. Mechanical binding in gib guides. | 1. Inspect bronze gib plates for scoring or debris.<br>2. Re-zero LVDT sensors via HMI service screen after checking mechanical level.<br>3. Verify proportional synchronization valve spool freedom of movement. | **YES** (LOTO / PTW Required) |
| **F-312** | `OIL_TEMP_HIGH_TRIP` | Cooler water flow restriction; ambient temperature $>42^{\circ}\text{C}$; proportional valve leakage generating excessive heat input. | 1. Check shell-and-tube heat exchanger cooling water inlet pressure (min $0.3\text{ MPa}$).<br>2. Clean cooling water strainer.<br>3. Inspect proportional valve zero-offset settings for internal bypassing. | **NO** (Visual check / valve adjust permitted without LOTO if electrical panel closed) |
| **F-418** | `TONNAGE_OVERLOAD_ESTOP` | Closed-die flashing; incorrect recipe input (setting target > 400 tonnes); scrap piece left in die cavity. | 1. Initiate hydraulic emergency return via manual pendant.<br>2. Inspect die cavity for foreign objects and flashing buildup.<br>3. Review PLC recipe parameters against engineering drawing limits. | **YES** (LOTO / PTW Required) |
| **F-520** | `COUNTERBALANCE_LOSS` | Nitrogen pre-charge pressure loss in accumulators ACC-01 through ACC-04; internal seal failure in counterbalance cylinder. | 1. Isolate accumulator gas circuit; check charging pressure with nitrogen kit (nominal: $4.5\text{ MPa}$).<br>2. Recharge or replace Bladder Assembly (Part No. VPW-ACC-BL-400).<br>3. Check cylinder rod seals for external leakage. | **YES** (LOTO / PTW Required) |
| **F-635** | `FILTER_DP_HIGH` | Contaminated return filter media; fluid viscosity too high due to cold start below 20.0°C. | 1. If oil temp $<25^{\circ}\text{C}$, run electric immersion heater until operating range reached.<br>2. If temp normal, replace filter element Part No. VPW-FLT-RET-400 immediately.<br>3. Check condition of oil via patch test. | **NO** (Filter change under dead-line bleed procedure) |

---

## 4. CONSUMABLE AND SPARE PARTS LIST

All replacements must utilize genuine Vindhya Precision Works part numbers listed in Table 4.1. Substitution of unapproved seals, filters, or hydraulic components voids plant insurance and manufacturer liability.

### Table 4.1: Consumables and Spares Inventory

| Item Description | Vindhya Part Number | Specification / Rating | Minimum Stock Threshold |
| :--- | :--- | :--- | :--- |
| **Return Line Filter Element** | VPW-FLT-RET-400 | Beta 10 $\ge$ 200, Cellulose/Glass Microfiber, 10-micron | 6 units |
| **High-Pressure Circuit Element** | VPW-FLT-HP-400 | Beta 5 $\ge$ 1000, Collapse rating 21.0 MPa, 5-micron | 4 units |
| **Proportional Pilot Filter** | VPW-FLT-PV-02 | Stainless Steel Mesh, 3-micron absolute | 8 units |
| **Main Cylinder Primary Seal Kit** | VPW-SEAL-CYL-400 | PTFE Bronze-filled slide rings + NBR O-rings (Bore: 350mm) | 2 sets |
| **Hydraulic Oil (Anti-Wear)** | VPW-OIL-VG46-200L | ISO VG 46, Zinc-free, Viscosity Index min 95 (200L Drum) | 3 drums |
| **Accumulator Bladder Kit** | VPW-ACC-BL-400 | Nitrile (NBR) elastomer, 50 Litre capacity standard | 2 units |
| **Proportional Valve (Main Axis)** | VPW-VALV-PR-400 | Rexroth-compatible direct-operated 4/3 way, NG25 | 1 unit |
| **Proximity Sensor (TDC/BDC)** | VPW-SEN-PRX-18 | M18 inductive, shielded, Sn=8mm, 24V DC PNP | 4 units |

---

## 5. TORQUE SPECIFICATIONS AND FASTENER CONTROLS

Correct torque application is mandatory to prevent structural fatigue failure of the 400-tonne frame under cyclic loading. All bolts must be tightened using calibrated hydraulic torque wrenches or tensioners with Molybdenum Disulfide ($MoS_2$) thread lubricant applied unless specified dry.

### Table 5.1: Critical Fastener Torques

| Fastener Location | Thread Size & Grade | Torque / Tension Specification | Lubrication Requirement |
| :--- | :--- | :--- | :--- |
| **Tie Rod Main Nuts (4 corners)** | M90 x 6.0 Grade 10.9 | Hydraulic Tensioning to **3,400 kN** per rod (Micrometer elongation check: $1.82\text{ mm} \pm 0.05\text{ mm}$) | Anti-seize compound on threads; clean mating faces dry. |
| **Bolster Plate Clamping Bolts** | M36 x 4.0 Grade 12.9 | **2,450 Nm** (Staged tightening: 30% -> 70% -> 100%) | $MoS_2$ paste applied to threads and under head. |
| **Main Pump Flange Mountings** | M16 x 2.0 Grade 10.9 | **210 Nm** (Cross-pattern sequence) | Clean, dry threads. |
| **Cylinder Mounting Head Flange** | M30 x 3.5 Grade 12.9 | **1,650 Nm** (Star pattern tightening) | $MoS_2$ thread lubricant. |
| **Manifold Subplate Mounting Bolts** | M12 x 1.75 Grade 10.9 | **85 Nm** (Torque wrench calibrated annually) | Light hydraulic oil film on threads. |

---

## 6. SAFETY-CRITICAL CORRECTIVE ACTIONS, LOCKOUT, AND PERMIT REQUIREMENTS

### 6.1 Mandatory Lockout/Tagout (LOTO) & Permit Scope
Any corrective action or maintenance task designated as **"Safety-Critical (YES)"** in Table 3.1, or any task requiring entry into the die space, access to the hydraulic manifold pressure chambers, or electrical cabinet work upstream of the main breaker, requires:
1. **The issuance of a Confined Space & Hot/Mechanical Permit-to-Work (PTW)** authorized by the Shift Maintenance Supervisor.
2. **Execution of Standard LOTO Procedure SOP-SAF-01:**
   * Open Main Circuit Breaker MCB-04 and apply Plant Padlock (Red Series A) and Danger Tag.
   * Depressurize Main Hydraulic Circuit by manually opening dump valve V-01 and verifying pressure gauge PI-01 drops to **0.0 MPa** within 30 seconds.
   * Lock mechanical safety safety-drop bar (Mechanical Ram Safety Wedge, Part No. VPW-WEDGE-400) in position beneath the slide bolster before any technician places hands or tools within the die zone.
   * Discharge all nitrogen accumulators ACC-01 through ACC-04 to safe holding tanks via isolation ball valves.

### 6.2 Resumption of Service
Following completion of any safety-critical intervention, reinstatement requires:
1. Removal of all personnel, tools, and temporary locking devices.
2. Withdrawal of safety wedge and confirmation of optical curtain integrity.
3. Countersignature on the PTW log by both the executing technician and the Engineering Lead before PLC interlock reset is authorized.
