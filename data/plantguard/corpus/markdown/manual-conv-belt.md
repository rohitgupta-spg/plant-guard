# Main Line Belt Conveyor (CONV-BELT) Equipment Manual and SOP

**VINDHYA PRECISION WORKS**
**TECHNICAL MANUAL AND STANDARD OPERATING PROCEDURE**
**Asset Class:** CONV-BELT (Main Line Belt Conveyor)
**Document ID:** VPW-SOP-CONV-BELT-042
**Revision:** 4.2
**Effective Date:** January 15, 2026

---

### 1. SCOPE AND APPLICABILITY
This document defines the mandatory operating parameters, preventive maintenance schedules, diagnostic fault codes, torque specifications, spare parts inventories, and safety interlocks for all Main Line Belt Conveyors (Asset Class CONV-BELT) installed at Vindhya Precision Works. Compliance is mandatory for all mechanical technicians, electrical technicians, and shift engineers.

---

### 2. NORMAL OPERATING RANGES AND ALARM SETPOINTS
CONV-BELT units shall be operated strictly within the parameters defined in Table 2.1. Any excursion beyond the Warning threshold requires logging in the shift maintenance ledger. Excursion beyond the Trip threshold initiates an immediate automated emergency stop (E-stop) via the plant safety PLC.

**Table 2.1: Operating Limits for CONV-BELT**
| Parameter | Minimum | Normal Operating Range | Warning Setpoint | Trip Setpoint |
| :--- | :--- | :--- | :--- | :--- |
| **Drive Motor Winding Temp (PT100)** | 15 °C | 45.0 °C – 78.0 °C | 85.0 °C | 92.0 °C |
| **Drive Pulley Bearing Temp** | 10 °C | 35.0 °C – 65.0 °C | 72.0 °C | 80.0 °C |
| **Tail Pulley Bearing Temp** | 10 °C | 30.0 °C – 60.0 °C | 68.0 °C | 75.0 °C |
| **Gearbox Sump Temp** | 15 °C | 50.0 °C – 72.0 °C | 82.0 °C | 90.0 °C |
| **Vibration Velocity (Drive Motor, RMS)**| 0.2 mm/s | 0.5 mm/s – 2.8 mm/s | 4.0 mm/s | 5.5 mm/s |
| **Vibration Velocity (Drive Pulley, RMS)**| 0.3 mm/s | 0.8 mm/s – 3.2 mm/s | 4.5 mm/s | 6.0 mm/s |
| **Pneumatic Take-Up Cylinder Pressure** | 4.2 bar | 5.0 bar – 5.8 bar | 4.5 bar | 4.0 bar |
| **Drive Motor Operating Current (FLA = 48A)**| 12.0 A | 22.0 A – 42.0 A | 45.5 A | 48.5 A (for > 5 sec) |
| **Belt Slip Monitoring Threshold** | N/A | 0.0% – 2.0% slip | 4.0% slip | 6.5% slip |

*Exception 2.1.1:* During cold-start ambient conditions where plant ambient temperature drops below 10 °C, the Gearbox Sump Temperature warning threshold is temporarily adjusted to 88.0 °C for the first 45 minutes of operation under authorization from Lead Mechanical Engineer Rajesh Verma.

---

### 3. PREVENTIVE MAINTENANCE SCHEDULE
Maintenance intervals are dictated by cumulative running hours recorded by the plant SCADA system. 

*   **3.1 Daily (Every 8 Operating Hours - Shift Technicians):**
    *   Inspect belt tracking across all idler stations; confirm tracking deviation does not exceed ±15 mm from center.
    *   Walk the length of the conveyor to check for abnormal scraping noises, structural rubbing, or material spillage at transfer points.
    *   Verify pneumatic take-up regulator gauge reads between 5.0 bar and 5.8 bar.
    *   Test pull-cord emergency stop switches (LS-PC-01 through LS-PC-06) manually; verify latching and PLC trip response.

*   **3.2 Level 1 PM (Every 500 Operating Hours ± 24 Hours):**
    *   Grease drive pulley and tail pulley pillow-block bearings using Lithium Complex EP2 grease (exact quantity: 25 grams per bearing point via manual grease gun).
    *   Inspect primary and secondary polyurethane belt scrapers for wear; adjust tensioners until blade-to-belt contact pressure is even across the full 1200 mm belt width.
    *   Check gearbox oil sight glass; verify oil level is between 50% and 70% of sight glass height. Add ISO VG 220 synthetic gear oil if level is below 50%.
    *   Clean accumulated dust and fines from the tail pulley snub roller housing and gravity/pneumatic take-up slide rails.

*   **3.3 Level 2 PM (Every 2,000 Operating Hours ± 72 Hours):**
    *   Perform complete alignment check of drive motor, fluid coupling, and gearbox output shafts using laser alignment tooling. Maximum allowable parallel offset: 0.05 mm; angular offset: 0.03 degrees.
    *   Inspect all troughing idlers and return idlers for bearing seizure, shell wear, or flat spots. Replace any idler exhibiting rotational resistance or abnormal acoustic signature.
    *   Measure belt thickness at three designated wear zones (Infeed, Center, Discharge) using ultrasonic thickness gauge VPW-UT-09. Minimum allowable belt carcass thickness is 12.5 mm (nominal new thickness is 16.0 mm).
    *   Inspect electrical control panel cabinet air filters; clean or replace if static pressure drop exceeds 25 Pa. Perform thermographic scan of all motor starter contactors and terminal blocks.

*   **3.4 Level 3 PM (Every 8,000 Operating Hours ± 168 Hours):**
    *   Drain, flush, and refill gearbox with fresh ISO VG 220 synthetic gear oil.
    *   Perform non-destructive testing (NDT) dye penetrant inspection on drive pulley shaft keyways and locking assemblies for micro-fractures.
    *   Inspect belt vulcanized splices for separation, cracking, or cord exposure.
    *   Recalibrate all inline instrumentation (PT100 sensors, accelerometer pods, pneumatic pressure transducers, and zero-speed proximity switches).

---

### 4. FAULT-CODE TABLE AND TROUBLESHOOTING
When a fault occurs, the local operator interface terminal (OIT-CONV-04) displays a specific alphanumeric code. Technicians shall execute the corrective actions detailed in Table 4.1.

**Table 4.1: CONV-BELT Fault Codes**
| Fault Code | Condition Name | Probable Cause | Corrective Action |
| :--- | :--- | :--- | :--- |
| **F-CB-101** | Drive Motor Overcurrent | 1. Material overload on belt.<br>2. Mechanical binding in drive pulley bearings.<br>3. Gearbox internal seizure. | 1. Inspect belt feed rate; clear localized material jam at infeed hopper.<br>2. Isolate power, apply LOTO (Procedure LOTO-09), rotate drive shaft manually to check for binding.<br>3. Check gearbox oil level and quality for metal shavings. |
| **F-CB-102** | Belt Slip Fault | 1. Drive pulley lagging worn or glazed.<br>2. Insufficient pneumatic take-up pressure causing slack belt.<br>3. Material moisture accumulation on pulley face. | 1. Inspect ceramic/rubber pulley lagging; replace if groove depth is < 2.0 mm.<br>2. Check pneumatic supply pressure to take-up cylinder; verify regulator is set to 5.4 bar.<br>3. Clean pulley face with industrial solvent and dry thoroughly. |
| **F-CB-103** | Excessive Bearing Temp | 1. Inadequate lubrication (grease dryout).<br>2. Excessive radial load from misadjusted belt tension.<br>3. Bearing raceway micro-spalling. | 1. Purge old grease with 35g of Lithium Complex EP2 via grease nipple while running at low speed.<br>2. Check belt take-up pressure and reduce if exceeding 5.8 bar.<br>3. Replace pillow-block bearing assembly. |
| **F-CB-104** | Belt Mistacking Out-of-Bounds | 1. Accumulation of material on return idlers.<br>2. Structural shifting of idler support brackets.<br>3. Uneven loading from upstream chute. | 1. Power down, apply LOTO, and scrape hardened material off affected return idlers.<br>2. Check idler mounting bolts with torque wrench; realign bracket to square with frame.<br>3. Adjust infeed deflector plates to center material feed. |
| **F-CB-105** | Zero-Speed Switch Fault | 1. Proximity sensor misaligned from tail pulley target disc.<br>2. Air gap between sensor and target exceeds tolerance.<br>3. Internal sensor electronic failure. | 1. Inspect sensor mounting bracket for physical impact damage.<br>2. Adjust sensor-to-target air gap to exactly 2.5 mm ± 0.5 mm using feeler gauge.<br>3. Replace proximity sensor module. |
| **F-CB-106** | Take-Up Pressure Low | 1. Plant compressed air header pressure drop.<br>2. Leakage in pneumatic take-up cylinder seals.<br>3. Pressure regulator failure. | 1. Check main header gauge at sector manifold 4; verify supply is above 6.0 bar.<br>2. Spray soapy water on cylinder rod seals and pneumatic fittings to locate air leaks.<br>3. Replace faulty pressure regulator assembly. |

---

### 5. TORQUE SPECIFICATIONS
All fasteners on the CONV-BELT assembly shall be tightened to the torque values specified in Table 5.1 using calibrated torque wrenches (calibration interval: 6 months).

**Table 5.1: Torque Requirements**
| Fastener Location / Application | Thread Size | Strength Class | Target Torque (Nm) |
| :--- | :--- | :--- | :--- |
| Drive Motor Foot Mounting Bolts | M16 | 8.8 | 195 Nm |
| Gearbox Torque Arm Anchor Bolts | M20 | 10.9 | 390 Nm |
| Drive Pulley Pillow-Block Base Bolts | M24 | 10.9 | 670 Nm |
| Snub and Tail Pulley Bearing Bolts | M16 | 8.8 | 195 Nm |
| Troughing Idler Frame Clamp Bolts | M12 | 8.8 | 85 Nm |
| Splice Compression Bolts (Mechanical Fasteners) | M10 | 8.8 | 48 Nm |
| Pulley Locking Assembly Screws (Ringfedder) | M12 | 12.9 | 120 Nm (in star pattern) |

---

### 6. CONSUMABLE AND SPARE PARTS LIST
Technicians shall source replacement items exclusively from the Vindhya Precision Works central stores using the part numbers defined in Table 6.1. Substitution of unapproved parts voids equipment warranty and safety certification.

**Table 6.1: Consumable and Spare Parts Inventory**
| Item Description | VPW Part Number | Specification / Dimensions | Min. Stock Level |
| :--- | :--- | :--- | :--- |
| **Conveyor Belt Roll** | CONV-BLT-1200-EP500 | EP500/3 Ply, 1200 mm width, 16 mm total thickness (per 100m) | 1 roll |
| **Drive Pulley Pillow-Block Bearing** | BRG-SNV-22224K | Self-aligning spherical roller bearing with adapter sleeve | 2 sets |
| **Tail Pulley Pillow-Block Bearing** | BRG-UCF-215 | Flanged cast-iron housing unit, 75 mm bore | 2 sets |
| **Primary Polyurethane Scraper Blade** | SCRP-BLD-1200P | 1200 mm width, orange polyurethane, 12mm thick | 4 pieces |
| **Synthetic Gear Oil (ISO VG 220)**| LUB-SYN-ISO220 | Polyalphaolefin (PAO) base, 20-liter container | 6 containers |
| **Grease (Lithium Complex EP2)** | LUB-GRS-EP2 | NLGI Grade 2, high-load extreme pressure, 400g cartridge | 24 cartridges |
| **Troughing Idler Assembly** | IDL-TRG-1200-127 | 3-roll troughed set, roll diam 127 mm, belt width 1200 mm | 10 sets |
| **Return Idler Roll** | IDL-RTN-1200-108 | Flat return roll, diam 108 mm, face width 1400 mm | 8 pieces |
| **Proximity Sensor (Zero Speed)** | ELE-SEN-PRX18 | M18 inductive proximity switch, 10-30 VDC, sensing dist 8 mm | 2 pieces |
| **Pneumatic Take-Up Cylinder** | PNE-CYL-100X500 | Bore 100 mm, Stroke 500 mm, double acting with magnetic piston | 1 piece |

---

### 7. SAFETY-CRITICAL CORRECTIVE ACTIONS AND LOTO REQUIREMENTS
Execution of any corrective action involving the handling, tensioning, or mechanical disconnection of the conveyor belt system presents severe hazards relating to stored mechanical energy, gravitational energy from elevated take-ups, and sudden rotational release.

**7.1 Explicit List of Safety-Critical Corrective Actions**
The following maintenance tasks are classified as **Safety-Critical**. They cannot be performed without an approved Lockout/Tagout (LOTO) procedure execution under Permit-to-Work (PTW) Form VPW-PTW-08:
1.  **Belt Splice Replacement or Repair:** Cutting, pulling, or clamping conveyor belting.
2.  **Pulley Replacement or Alignment:** Disconnection or adjustment of drive, tail, snub, or take-up pulleys.
3.  **Gearbox and Motor Coupling Intervention:** Disassembly of fluid couplings, gearboxes, or drive motors.
4.  **Take-Up System Servicing:** Working on pneumatic cylinders, counterweight cables, or slide mechanisms associated with belt tensioning.
5.  **Idler Changeout Under Tension:** Replacement of troughing or return idlers situated within 15 meters of the drive or tail tension zones.

**7.2 Mandatory LOTO Sequence**
For all tasks listed in Section 7.1, technicians shall enforce the following sequence prior to initiating work:
1.  Notify Shift Controller to halt material feed upstream of CONV-BELT. Run conveyor empty for 3 minutes to clear all material.
2.  Isolate the main electrical supply at MCC feeder breaker MCC-04-CB12. Apply personal padlock and danger tag (VPW-LOTO-009).
3.  Isolate the pneumatic take-up air supply at ball valve V-PNEU-42; lock valve in CLOSED position and open downstream bleed valve to vent stored pneumatic pressure to 0.0 bar. Verify gauge reading reads zero.
4.  Apply mechanical belt clamp (VPW-TOOL-BC04) on both sides of the working zone to prevent rotational runback or stored elastic energy release from the tensioned belt.
5.  Verify zero energy state at the local control station using calibrated multimeter (Cat III 1000V). Sign Section 3 of PTW-08 before commencing physical work.
