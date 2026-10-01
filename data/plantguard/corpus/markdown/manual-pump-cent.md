# Centrifugal Process Pump (PUMP-CENT) Equipment Manual and SOP

**STANDARD OPERATING PROCEDURE AND MAINTENANCE MANUAL**
**ASSET CLASS:** PUMP-CENT (Centrifugal Process Pump)
**DOCUMENT ID:** VPW-SOP-PC-402
**EFFECTIVE DATE:** 14 January 2026
**OWNER:** Maintenance Engineering, Vindhya Precision Works

---

### 1.0 PURPOSE AND APPLICABILITY

This document defines the operating limits, preventive maintenance schedules, diagnostic procedures, torque specifications, and safety-critical interventions for all asset class PUMP-CENT installations within Vindhya Precision Works Plant No. 3. Compliance with this procedure is mandatory for all mechanical technicians and operations personnel.

---

### 2.0 NORMAL OPERATING RANGES AND ALARM SETPOINTS

PUMP-CENT units shall be operated strictly within the parameters detailed in Table 2.1. Exceeding warning thresholds requires logging in the shift supervisor report; reaching alarm thresholds initiates automated interlocks or mandatory manual shutdown as specified.

**Table 2.1: Operating Limits and Alarm Thresholds for PUMP-CENT**

| Parameter | Normal Operating Range | Warning Threshold (Action) | Alarm / Trip Threshold (Immediate Action) |
| :--- | :--- | :--- | :--- |
| **Bearing Temperature (DE / NDE)** | $42^\circ\text{C} - 68^\circ\text{C}$ | $78^\circ\text{C}$ (Inspect lubrication) | $88^\circ\text{C}$ (Trip pump) |
| **Casing Vibration (Overall Velocity)** | $0.8\text{ mm/s RMS} - 2.8\text{ mm/s RMS}$ | $4.2\text{ mm/s RMS}$ (Vibration analysis required) | $6.5\text{ mm/s RMS}$ (Trip pump) |
| **Discharge Pressure** | $3.2\text{ bar} - 4.8\text{ bar}$ | $< 2.8\text{ bar}$ or $> 5.2\text{ bar}$ | $< 2.2\text{ bar}$ or $> 5.8\text{ bar}$ (Trip pump) |
| **Suction Pressure** | $1.2\text{ bar} - 1.8\text{ bar}$ | $< 0.9\text{ bar}$ | $< 0.5\text{ bar}$ (Cavitation risk trip) |
| **Motor Current (Full Load Amps)** | $38\text{ A} - 52\text{ A}$ | $> 58\text{ A}$ | $> 64\text{ A}$ (Overload trip) |
| **Mechanical Seal Flush Flow** | $4.0\text{ L/min} - 6.0\text{ L/min}$ | $< 3.0\text{ L/min}$ | $< 2.0\text{ L/min}$ (Interlock trip) |

---

### 3.0 PREVENTIVE MAINTENANCE SCHEDULE

Maintenance intervals are determined by cumulative running hours as tracked by the Vindhya Plant Maintenance Management System (VPMMS). 

**3.1 Level 1 (PM-100): Every 750 Running Hours**
*   Grease motor and pump bearings using exactly 15 grams of Vindhya Grade-V Synthetic Polyurea grease (Part No. VPW-LUB-8821). Never mix grease types.
*   Inspect mechanical seal flush line rotameter to verify flow remains within the 4.0 L/min to 6.0 L/min window.
*   Check coupling guard alignment and security.

**3.2 Level 2 (PM-500): Every 3,000 Running Hours**
*   Perform laser shaft alignment check across the flexible disc coupling. Maximum allowable parallel offset: $0.05\text{ mm}$; maximum angular misalignment: $0.03^\circ$.
*   Measure vibration spectra using route-based analyzer; verify overall velocity remains below $2.8\text{ mm/s RMS}$.
*   Inspect external casing bolts and foundation anchor bolts for corrosion or loosening.

**3.3 Level 3 (PM-2000): Every 12,000 Running Hours**
*   Complete overhaul of rotating assembly.
*   Replace mechanical seal assembly, radial and thrust bearings, and casing wear rings.
*   Nondestructive testing (NDT) dye penetrant inspection of the impeller hub and vanes for cavitation pitting or cracking.

---

### 4.0 FAULT-CODE TABLE AND CORRECTIVE ACTIONS

When a fault condition manifests on PUMP-CENT assets, technicians shall reference Table 4.1 to execute diagnostic and corrective protocols.

**Table 4.1: Fault Conditions and Corrective Actions**

| Fault Condition Identifier | Symptom Description | Probable Cause | Corrective Action |
| :--- | :--- | :--- | :--- |
| **FC-PC-01** | High bearing temperature ($>88^\circ\text{C}$) accompanied by high-frequency acoustic emission. | Insufficient lubrication, contaminated grease, or bearing cage degradation. | Stop unit, execute LOTO (Section 6.0). Inspect bearing housing, clean out old grease, replace bearings (Part No. VPW-BRG-4412) if raceway pitting is present, and repack with fresh VPW-LUB-8821. |
| **FC-PC-02** | Excessive vibration ($>6.5\text{ mm/s RMS}$) predominantly at $1\times$ running speed. | Rotor dynamic unbalance due to product solids buildup on impeller or impeller vane loss. | Shut down unit via interlock or manual trip. Isolate, drain casing, remove suction spool, and inspect impeller. Clean deposits or balance/replace impeller (Part No. VPW-IMP-9032). |
| **FC-PC-03** | Low discharge pressure ($<2.2\text{ bar}$) with normal motor speed and unstable current draw. | Suction line starvation, vortexing in storage tank, or severe internal recirculation from worn wear rings. | Check suction strainer for blockages. Verify tank level. If level and strainer are normal, measure internal wear ring clearance; replace wear rings (Part No. VPW-WR-1104) if diametrical clearance exceeds $0.65\text{ mm}$. |
| **FC-PC-04** | Continuous mechanical seal leakage exceeding $10\text{ drops per minute}$. | Carbon face thermal shock, dry running, or chemical attack on elastomer secondary seals. | Shut down unit and execute LOTO. Disassemble seal housing, inspect seal faces for heat checking or grooving. Replace mechanical seal cartridge (Part No. VPW-MSL-6022) and verify quench/flush supply before restart. |
| **FC-PC-05** | Motor current spike ($>64\text{ A}$) coupled with elevated pump casing temperature. | Process fluid specific gravity or viscosity has exceeded design limits ($>1.25\text{ SG}$), or mechanical rub within wet end. | Verify process batch density via laboratory sample. If fluid is within spec, perform manual shaft rotation check (must turn freely with hand tool). If binding occurs, disassemble casing to clear internal rub. |
| **FC-PC-06** | Severe cavitation noise (sounding like gravel passing through volute) with drop in flow rate. | NPSH available ($NPSHa$) is less than NPSH required ($NPSHr$), caused by restricted suction piping or high fluid temperature. | Inspect suction isolation valve to confirm 100% open position. Check suction filter differential pressure. Lower process fluid temperature if vapor pressure is approaching saturation limit. |

---

### 5.0 CONSUMABLE AND SPARE PARTS LIST

All replacement items used on asset class PUMP-CENT must match the exact part numbers listed in Table 5.1. Substitution of unapproved manufacturer components is strictly prohibited.

**Table 5.1: Approved Spare Parts and Consumables**

| Item Description | Vindhya Part Number | Standard Stock Quantity |
| :--- | :--- | :--- |
| Mechanical Seal Cartridge Assembly (Tungsten Carbide/Silicon Carbide) | VPW-MSL-6022 | 2 units per plant |
| Radial Ball Bearing (Deep Groove, C3 Clearance) | VPW-BRG-4412 | 4 units per plant |
| Thrust Roller Bearing (Double Row) | VPW-BRG-4415 | 2 units per plant |
| Impeller Casting (Cast Stainless Steel CF8M, Dynamically Balanced) | VPW-IMP-9032 | 1 unit per plant |
| Casing Wear Ring Set (Front and Rear) | VPW-WR-1104 | 3 sets per plant |
| Casing Gasket Set (Spiral Wound Graphite/SS316) | VPW-GST-3309 | 6 sets per plant |
| Synthetic Polyurea Grease (400g Cartridge) | VPW-LUB-8821 | 24 cartridges |
| Flexible Disc Coupling Element | VPW-CPL-7710 | 3 units per plant |

---

### 6.0 TORQUE SPECIFICATIONS

Fasteners on PUMP-CENT units must be tightened using a calibrated torque wrench in a criss-cross (star) pattern to ensure uniform gasket compression and casing sealing.

*   **Casing Studs / Bolts (M16 Gr. 8.8):** $110\text{ Nm} \pm 5\text{ Nm}$
*   **Bearing Housing Retaining Bolts (M10 Gr. 8.8):** $45\text{ Nm} \pm 2\text{ Nm}$
*   **Impeller Locking Nut (M24 Fine Thread):** $210\text{ Nm} \pm 10\text{ Nm}$ (Apply Loctite 243 threadlocker)
*   **Coupling Hub Clamp Bolts (M12 Gr. 12.9):** $85\text{ Nm} \pm 3\text{ Nm}$
*   **Baseplate Foundation Anchor Bolts (M20):** $180\text{ Nm} \pm 10\text{ Nm}$

---

### 7.0 SAFETY-CRITICAL CORRECTIVE ACTIONS AND LOTO MANDATE

**7.1 Safety-Critical Scope**
The following corrective actions involve high-energy release hazards (hydraulic pressure, rotational kinetic energy, high temperature, and hazardous chemical process media). They are classified as **Safety-Critical**:
1.  Opening the pump casing or suction/discharge spool pieces (FC-PC-02, FC-PC-03, FC-PC-05).
2.  Replacing or servicing the mechanical seal or shaft assembly (FC-PC-01, FC-PC-04).
3.  Disconnecting or adjusting the flexible disc coupling alignment.

**7.2 Lockout/Tagout (LOTO) and Permit Requirements**
Before initiating any safety-critical corrective action on asset class PUMP-CENT, the technician in charge must execute the following protocol without exception:
1.  Obtain a signed **Class-1 Mechanical Hot/Cold Work Permit** from the Vindhya Safety Department.
2.  Apply personal Lockout/Tagout (LOTO) padlocks to the local motor control center (MCC) breaker for the pump drive motor, isolating electrical energy under VPW-SOP-LOTO-01.
3.  Close upstream and downstream process isolation valves and apply chain-and-padlock isolation tags to prevent back-pressure or chemical ingress.
4.  Depressurize and drain the pump casing completely via the drain plug port, verifying zero pressure via the local gauge. If process fluid is hazardous or caustic, execute a full chemical flush of the volute before breaking any bolted joint.
5.  Verify zero energy state at the motor shaft before commencing mechanical disassembly.
