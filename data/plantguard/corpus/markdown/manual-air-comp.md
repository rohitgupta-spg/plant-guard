# Rotary Screw Air Compressor (AIR-COMP) Equipment Manual and SOP

# STANDARD OPERATING PROCEDURE: ROTARY SCREW AIR COMPRESSOR
**Document ID:** SOP-MNT-AIR-042  
**Asset Class:** AIR-COMP  
**Plant Location:** Vindhya Precision Works, Plant Floor Building 3  
**Applicability:** Maintenance Technicians, Reliability Engineers, Utility Operators  
**Effective Date:** January 15, 2026  
**Revision:** 4.1  

---

## 1. PURPOSE AND SCOPE

This standard operating procedure defines the operational baselines, preventive maintenance schedules, fault diagnostics, parts inventory, and safety-critical interventions for all rotary screw air compressors (Asset Class AIR-COMP) installed at Vindhya Precision Works. Compliance with these clauses is mandatory for all maintenance personnel.

---

## 2. NORMAL OPERATING RANGES AND ALARM SETPOINTS

All AIR-COMP units shall operate within the strict parameter thresholds defined in Table 2.1. Any excursion outside the warning threshold requires logged notification to the Maintenance Lead within 1 shift (8 hours). Excursion past the trip setpoint shall immediately shut down the compressor via the PLC safety interlock.

### Table 2.1: Operating Parameters and Alarm Thresholds

| Parameter | Normal Operating Range | Warning Setpoint | Trip Setpoint |
| :--- | :--- | :--- | :--- |
| **Air Discharge Pressure** | 7.2 bar to 8.1 bar | 8.4 bar | 8.8 bar |
| **Airend Discharge Temperature** | 78°C to 92°C | 98°C | 105°C |
| **Sump Tank Pressure (Loaded)** | 7.0 bar to 7.9 bar | 8.2 bar | 8.7 bar |
| **Main Drive Motor Current (415V)** | 110 A to 135 A | 148 A | 160 A |
| **Vibration (Airend Drive End - Velocity)** | 0.8 mm/s to 2.2 mm/s RMS | 3.5 mm/s RMS | 4.8 mm/s RMS |
| **Vibration (Airend Non-Drive End - Velocity)**| 0.6 mm/s to 1.8 mm/s RMS | 3.0 mm/s RMS | 4.2 mm/s RMS |
| **Oil Injection Temperature** | 55°C to 68°C | 72°C | 78°C |

*Exception 2.1.1:* During cold-start sequences in ambient temperatures below 12°C, oil injection temperature warning setpoints are temporarily bypassed for the first 300 seconds of operation.

---

## 3. PREVENTIVE MAINTENANCE SCHEDULE

Preventive maintenance (PM) is dictated by cumulative running hours recorded by the plant SCADA system. Technicians shall execute PM routines in accordance with Table 3.1.

### Table 3.1: Running Hour PM Intervals

| Interval | Task Identifier | Required Actions |
| :--- | :--- | :--- |
| **Every 50 Hours** | PM-50 | Inspect condensate auto-drains on air receiver and moisture separator. Clean filter media on electrical cabinet cooling fans. Check oil level in sight glass. |
| **Every 500 Hours** | PM-500 | Take compressor oil sample for laboratory spectrographic analysis. Grease main motor bearings with 25 grams of VPW-Polyrex EM grease. Inspect drive coupling alignment and elastomeric insert wear. |
| **Every 2,000 Hours** | PM-2000 | Replace air intake filter element (Part No. VPW-AF-8821). Replace oil filter element (Part No. VPW-OF-4410). Inspect minimum pressure check valve seals. Clean oil cooler external fins with compressed air at max 2.0 bar. |
| **Every 4,000 Hours** | PM-4000 | Replace air/oil separator element (Part No. VPW-OS-9930). Flush and refill compressor lubricant (VPW-Lube-Syn 46). Replace thermal valve element. Calibrate pressure transducers and temperature probes against certified secondary standards. |
| **Every 16,000 Hours**| PM-16000| Complete overhaul of airend assembly by certified technician. Replace shaft seals, main rotor bearings, and inlet control valve actuation diaphragms. Inspect gears/coupling for backlash tolerances. |

---

## 4. FAULT-CODE TABLE AND TROUBLESHOOTING

When the compressor controller displays a fault code, technicians shall reference Table 4.1 to determine the probable cause and execute the prescribed corrective action.

### Table 4.1: Fault Code Diagnostics

| Fault Code | Display Text | Probable Cause | Corrective Action |
| :--- | :--- | :--- | :--- |
| **F-101** | *HIGH AIREND TEMP* | Low oil level in receiver tank; blocked oil cooler core; failing thermal valve wax element stuck closed. | Check oil sight glass and top up with VPW-Lube-Syn 46 if below 50%. Clean external oil cooler fins. Verify thermal valve opens at 65°C; replace element if defective. |
| **F-102** | *MOTOR OVERLOAD* | High discharge pressure setting; mechanical binding in airend bearings; low voltage supply phase imbalance exceeding 3%. | Inspect pressure switch settings. Rotate airend shaft manually (power off, locked out) to check for binding. Measure running current across all three phases; report supply imbalance to electrical utility team. |
| **F-103** | *LOW OIL PRESSURE* | Restricted oil filter; faulty oil pump bypass valve; collapsed internal oil line hose. | Replace oil filter element (VPW-OF-4410). Inspect oil stop valve and bypass valve for debris or stuck plungers. Replace any oil line showing internal delamination. |
| **F-104** | *HIGH DISCHARGE PRESS* | Pressure regulator failing; inlet unloader valve stuck open during unload cycle; PLC output relay latched. | Inspect and rebuild unloader valve assembly (Part No. VPW-UV-1102). Verify solenoid valve 3-way exhaust port is clear. Test PLC output channels. |
| **F-105** | *PHASE SEQ / LOSS* | Incorrect incoming phase rotation from motor control center; blown line fuse on control transformer. | Verify phase rotation using meter at main breaker (must be clockwise L1-L2-L3). Replace blown primary control fuses with 3A slow-blow type. |
| **F-106** | *SEPARATOR DP HIGH* | Air/oil separator element saturated with varnish or particulate contaminants; operating consistently below oil injection temperature dew point. | Replace air/oil separator element (VPW-OS-9930). Check that thermostatic valve maintains operating oil temperature above 65°C to prevent moisture condensation in sump. |

---

## 5. CONSUMABLE AND SPARE PARTS LIST

Maintenance stockroom clerks shall maintain minimum stock quantities of the proprietary parts listed in Table 5.1. No substitutions are permitted without written sign-off by the Reliability Engineering Manager.

### Table 5.1: Bill of Materials (BOM)

| Description | Part Number | Stock Qty Threshold |
| :--- | :--- | :--- |
| Air Intake Filter Element | VPW-AF-8821 | 4 units |
| Spin-On Oil Filter Element | VPW-OF-4410 | 6 units |
| Air/Oil Separator Element | VPW-OS-9930 | 2 units |
| Synthetic Compressor Fluid (20L Pail) | VPW-Lube-Syn 46 | 3 pails |
| Thermal Valve Kit (65°C) | VPW-TV-6500 | 1 unit |
| Unloader Valve Repair Kit | VPW-UV-1102 | 1 unit |
| Minimum Pressure Valve Service Kit | VPW-MP-3320 | 1 unit |
| Airend Shaft Seal Kit | VPW-SS-5540 | 1 unit |
| Drive Coupling Elastomer Spider | VPW-DC-2210 | 2 units |

---

## 6. TORQUE SPECIFICATIONS

All mechanical fasteners associated with the AIR-COMP asset class must be tightened using a calibrated torque wrench in accordance with Table 6.1. Thread-locking compound (Loctite 243 medium strength) shall be applied to steel-into-cast-iron fasteners unless otherwise noted.

### Table 6.1: Fastener Torque Matrix

| Application / Fastener Location | Thread Size | Target Torque |
| :--- | :--- | :--- |
| Airend Discharge Flange Bolts | M12 (Grade 8.8) | 85 Nm |
| Main Drive Motor Mounting Bolts | M16 (Grade 8.8) | 210 Nm |
| Oil Injected Manifold Pipe Flanges | M10 (Grade 8.8) | 45 Nm |
| Minimum Pressure Check Valve Cover | M8 (Grade 8.8) | 25 Nm |
| Air/Oil Separator Cover Fasteners | M10 (Grade 8.8) | 50 Nm (Star pattern sequence) |
| Electrical Terminal Block Power Lugs | M8 Brass Studs | 15 Nm |

---

## 7. SAFETY-CRITICAL CORRECTIVE ACTIONS AND LOTO REQUIREMENTS

Certain maintenance interventions on Asset Class AIR-COMP involve extreme stored energy hazards, including high-pressure pneumatic air (up to 8.8 bar), elevated thermal energy (surfaces exceeding 100°C), and high-voltage electrical power (415V AC 3-phase). 

### 7.1 Explicit List of Safety-Critical Actions
The following corrective actions are strictly classified as **Safety-Critical**. Technicians are prohibited from initiating these tasks without executing an official Work Permit and applying Lockout/Tagout (LOTO) protocols per Vindhya Precision Works Safety Policy EHS-09:

1. **Air/Oil Separator Element Replacement:** Involves opening a pressure vessel containing residual pneumatic pressure and hot oil. Requires complete system blowdown, zero-pressure verification on gauge PI-02, and LOTO of the main electrical supply disconnect.
2. **Airend Overhaul or Replacement:** Involves uncoupling heavy rotating machinery, breaking flanged high-pressure lines, and handling heavy castings (>50 kg). Requires crane lift plan, mechanical LOTO, and electrical LOTO.
3. **Thermal Valve or Minimum Pressure Valve Maintenance:** Involves disassembly of housings connected directly to the oil receiver tank. Requires verified zero system pressure and thermal cool-down period below 40°C.
4. **Main Drive Motor Maintenance or Alignment:** Involves working near exposed rotating drive shafts and high-voltage terminals. Requires electrical LOTO at the Motor Control Center (MCC) bucket with personal padlock applied.
5. **Oil Cooler Chemical Flushing or Core Replacement:** Involves breaking hydraulic/oil circuits under residual head pressure. Requires closed-loop drainage, thermal isolation, and LOTO of the auxiliary scavenger pump circuit.

### 7.2 LOTO Verification Sequence
Before any safety-critical task begins, the technician of record must:
* Open the local isolator switch and apply a red padlock and danger tag.
* Verify zero electrical voltage using a calibrated multimeter at the motor starter terminals.
* Open the manual blowdown valve (V-99) to vent all receiver tank pressure to atmosphere.
* Visually confirm that pressure gauge PI-01 reads exactly 0.0 bar before unbolting any piping flange or filter lid.
