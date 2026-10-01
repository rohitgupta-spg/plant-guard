# Continuous Curing Oven (IND-OVEN) Equipment Manual and SOP

# STANDARD OPERATING PROCEDURE & MAINTENANCE MANUAL
**ASSET CLASS:** Continuous Curing Oven (IND-OVEN)  
**DOCUMENT ID:** SOP-MNT-IND-OVEN-042  
**ISSUING AUTHORITY:** Vindhya Precision Works Engineering Division  
**EFFECTIVE DATE:** 14 January 2026  
**APPLICABILITY:** Mandatory for all certified mechanical and electrical maintenance technicians  

---

## 1. SECTION 1: OPERATING PARAMETERS AND ALARM THRESHOLDS

**1.1** The IND-OVEN asset class shall be operated strictly within the designated parameter bounds defined in Table 1.0. Exceeding these parameters outside the prescribed tolerance windows shall initiate automatic interlock triggers as specified.

**Table 1.0: Operating Parameters & Alarm Limits**

| Parameter | Normal Operating Range | Warning Alarm Setpoint | Critical Interlock / Trip Setpoint | Action on Trip |
| :--- | :--- | :--- | :--- | :--- |
| **Zone 1–4 Temperature** | $185.0^\circ\text{C}$ – $215.0^\circ\text{C}$ | $\pm 3.5^\circ\text{C}$ from setpoint | $\pm 7.0^\circ\text{C}$ from setpoint | Cut main heating contactor; run exhaust fans at 100% for 30 min. |
| **Conveyor Drive Vibration (RMS)**| $0.4\text{ mm/s}$ – $1.8\text{ mm/s}$ | $2.5\text{ mm/s}$ | $4.2\text{ mm/s}$ | Immediate halt of conveyor variable frequency drive (VFD). |
| **Exhaust Duct Static Pressure** | $-120\text{ Pa}$ to $-180\text{ Pa}$ | $-95\text{ Pa}$ | $-60\text{ Pa}$ | Prevent burner ignition sequence / lock fuel gas solenoid valves. |
| **Recirculation Fan Motor Current**| $24.5\text{ A}$ – $31.0\text{ A}$ | $34.5\text{ A}$ | $39.0\text{ A}$ | Tripping of thermal overload relay; alarm to SCADA. |

---

## 2. SECTION 2: PREVENTIVE MAINTENANCE SCHEDULE

**2.1** Preventive maintenance (PM) for IND-OVEN units shall be executed strictly by accumulated running hours recorded via the PLC-104 runtime register.

*   **Level 1 PM (Every 250 Running Hours $\pm 10$ Hours):**
    *   Inspect silicone door perimeter seals (Part VPW-SL-099) for splitting or compression set. Replace if clearance gap exceeds $2.0\text{ mm}$.
    *   Grease conveyor roller bearings (Pillow Block Type VPW-BR-402) using high-temperature synthetic grease (VPW-GR-888); apply precisely 4 strokes per fitting using a manual grease gun.
    *   Clean optical safety curtain lenses (Model VPW-OP-12) with isopropyl alcohol wipe.

*   **Level 2 PM (Every 1,000 Running Hours $\pm 25$ Hours):**
    *   Verify calibration of all four Type-K thermocouples in Zones 1 through 4 using a certified dry-block calibrator. Replace any sensor showing deviation $> 1.5^\circ\text{C}$.
    *   Inspect internal circulating fan impeller blades (VPW-BL-771) for particulate build-up and dynamic balance. Remove carbon deposits using a non-metallic scraper.
    *   Check electrical terminal torque inside the main power distribution panel (Cabinet VPW-PNL-02). Retorque all busbar and contactor connections to specifications in Section 5.

*   **Level 3 PM (Every 5,000 Running Hours $\pm 50$ Hours):**
    *   Overhaul main exhaust gas damper actuator linkage (VPW-ACT-303). Inspect pivot pins for galling and replace nylon bushings.
    *   Perform insulation resistance (Megger) test on recirculation fan drive motors (VPW-MOT-55). Minimum acceptable insulation resistance is $100\text{ M}\Omega$ at $500\text{ V DC}$.
    *   Replace internal combustion chamber igniter electrodes and flame scanners.

---

## 3. SECTION 3: FAULT-CODE TROUBLESHOOTING TABLE

**3.1** When an IND-OVEN fault code appears on the HMI terminal, technicians shall reference Table 2.0 to determine the probable cause and execute the required corrective action.

**Table 2.0: Fault-Code Resolution Matrix**

| Fault Code & Description | Probable Cause | Corrective Action |
| :--- | :--- | :--- |
| **E-101: Zone Thermal Runaway** | Solid-state relay (SSR) failure fused in the closed state, supplying continuous power to heating elements. | Isolate power at main breaker. Test SSR leakage current; replace failed SSR (Part VPW-SSR-21). Verify PID controller output. |
| **E-104: Conveyor Stalls / Over-torque** | Mechanical jamming of the wire-mesh belt due to product edge-curl or track misalignment. | Lockout drive (LOTO). Clear jammed product manually. Inspect track guide rollers; adjust tensioner bolts to achieve $15\text{ mm}$ sag at mid-span. |
| **E-202: Low Exhaust Draft Pressure** | Accumulation of volatiles and tar in the exhaust ductwork or failure of the exhaust blower motor. | Inspect exhaust stack internal diameter. Scrape out condensates. Check blower belt tension; if slipping, replace belt (Part VPW-BLT-505). |
| **E-305: Burner Flame Failure** | Partial blockage of the natural gas pilot orifice or degradation of the UV flame scanner tube. | Clean gas pilot jet with brass wire broach. Clean glass envelope of UV scanner. If fault persists, replace scanner assembly (Part VPW-FLM-88). |
| **E-410: Recirculation Fan Overload** | Bearing seizure on the internal circulation fan shaft or choked inlet louvers. | Manually rotate fan shaft (with power locked out). If shaft is bound, replace pillow block bearings (Part VPW-BR-402) and check motor winding balance. |
| **E-520: Safety Interlock Chain Open** | Emergency stop button depressed, access door safety switch tripped, or air pressure switch failing. | Inspect safety circuit diagnostic screen on HMI to isolate open contact. Reset or replace faulty microswitch (Part VPW-SW-11); verify door alignment. |

---

## 4. SECTION 4: CONSUMABLE AND SPARE PARTS LIST

**4.1** Technicians shall only use genuine Vindhya Precision Works-approved part numbers listed in Table 3.0 when performing corrective or preventive maintenance on IND-OVEN systems.

**Table 3.0: Approved Spares & Consumables**

| Description | OEM Part Number | Replacement Interval / Stock Unit |
| :--- | :--- | :--- |
| High-Temp Silicone Door Seal | VPW-SL-099 | Every 1,000 hours / Per Meter |
| Type-K Thermocouple Assembly | VPW-TC-204 | Every 5,000 hours / Unit |
| Solid-State Relay (50A, 480VAC) | VPW-SSR-21 | As needed / Unit |
| Conveyor Drive V-Belt Set | VPW-BLT-505 | Every 2,000 hours / Set of 2 |
| Recirculation Fan Pillow Block Bearing | VPW-BR-402 | Every 5,000 hours / Unit |
| Natural Gas Pilot Igniter Assembly | VPW-IGN-90 | Every 2,500 hours / Unit |
| UV Flame Scanner Tube | VPW-FLM-88 | Every 3,000 hours / Unit |
| High-Temperature Synthetic Grease | VPW-GR-888 | Continuous consumable / 400g Cartridge |
| Exhaust Blower Motor (3.7 kW) | VPW-MOT-55 | As needed / Unit |
| Air Intake HEPA Filter Panel | VPW-FLT-102 | Every 500 hours / Unit |

---

## 5. SECTION 5: TORQUE SPECIFICATIONS

**5.1** All threaded fasteners secured during maintenance procedures on the IND-OVEN shall be tightened using a calibrated torque wrench in accordance with Table 4.0.

**Table 4.0: Fastener Torque Requirements**

| Fastener Location / Application | Thread Size & Grade | Target Torque Value |
| :--- | :--- | :--- |
| Main Electrical Busbar Connections | M8, Grade 8.8 Brass/Cu | $14.5\text{ Nm}$ ($\pm 0.5\text{ Nm}$) |
| Recirculation Fan Impeller Hub Locking Bolt | M16, Grade 10.9 Steel | $125.0\text{ Nm}$ ($\pm 5.0\text{ Nm}$) |
| Conveyor Drive Sprocket Set Screws | M10, Grade 12.9 Steel | $38.0\text{ Nm}$ ($\pm 1.5\text{ Nm}$) |
| Combustion Chamber Flange Bolts | M12, Grade 8.8 Steel | $65.0\text{ Nm}$ ($\pm 2.0\text{ Nm}$) |
| Oven Casing Access Panel Fasteners | M6, Stainless A2-70 | $8.5\text{ Nm}$ ($\pm 0.5\text{ Nm}$) |

---

## 6. SECTION 6: SAFETY-CRITICAL CORRECTIVE ACTIONS AND LOTO MANDATE

**6.1** The following corrective actions involve hazardous energy sources (electrical, thermal, pneumatic, or mechanical) and are classified as **Safety-Critical**.

**6.2** Execution of any safety-critical corrective action requires:
1. Full execution of the Vindhya Precision Works Lockout/Tagout (LOTO) procedure per corporate standard SOP-SAF-001.
2. Issuance of a verified Hot Work or Confined Space Entry Permit by the shift safety officer where applicable.
3. Verification of zero energy state using a calibrated multi-meter (CAT IV rated) before physical intervention.

**6.3 Explicit List of Safety-Critical Corrective Actions:**
*   **SC-01:** Replacement, wiring inspection, or internal adjustment of any Solid-State Relay (SSR) or main heating element contactor. (*Hazard: High Voltage / Electrocution*).
*   **SC-02:** Servicing, alignment, or tensioning of the internal conveyor drive chain and mechanical mesh assembly while access doors are open. (*Hazard: Mechanical Entanglement / Crush*).
*   **SC-03:** Maintenance, cleaning, or replacement of the natural gas burner manifold, pilot assembly, and automatic fuel gas shut-off valves. (*Hazard: Gas Leak / Explosion / Asphyxiation*).
*   **SC-04:** Entry into the oven chamber for internal duct cleaning or impeller maintenance prior to the internal ambient temperature dropping below $35.0^\circ\text{C}$ and issuance of a confined space entry permit. (*Hazard: Severe Thermal Burns / Heat Stress*).
*   **SC-05:** Replacement of the recirculation fan motor (VPW-MOT-55) or servicing of its electrical supply leads. (*Hazard: Arc Flash / High Voltage*).

---
**END OF PROCEDURE**
