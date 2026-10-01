# Water-Cooled Process Chiller (CHILLER) Equipment Manual and SOP

**DOCUMENT REFERENCE:** VPW-SOP-MCH-041  
**ASSET CLASS:** CHILLER (Water-Cooled Process Chiller, 150-Ton Screw Compressor System)  
**EFFECTIVE DATE:** 14 January 2026  
**ISSUING AUTHORITY:** Maintenance Engineering Directorate, Vindhya Precision Works  
**SUPERSEDES:** Revision 3.2  

---

### 1.0 PURPOSE AND SCOPE

This standard operating procedure defines the operational baselines, preventive maintenance intervals, fault response protocols, torque specifications, and safety-critical isolation requirements for all water-cooled process chillers (Asset Class CHILLER) installed within the Vindhya Precision Works facility. Adherence to these clauses is mandatory for all maintenance technicians, mechanical supervisors, and operations personnel.

---

### 2.0 NORMAL OPERATING RANGES AND ALARM SETPOINTS

2.1 **Operating Parameters:** Technicians shall record operating parameters via the local Programmable Logic Controller (PLC) interface every four hours. Any reading exceeding the warning threshold for a continuous duration of 180 seconds shall trigger an automated engineering inquiry.

| Parameter | Normal Operating Range | Warning Threshold | Critical Trip Setpoint |
| :--- | :--- | :--- | :--- |
| **Evaporator Refrigerant Pressure** | 4.2 bar – 4.8 bar | < 3.8 bar or > 5.2 bar | $\le$ 3.1 bar |
| **Condenser Refrigerant Pressure** | 11.5 bar – 14.2 bar | > 15.8 bar | $\ge$ 17.5 bar |
| **Chilled Water Supply Temperature** | 6.5°C – 7.5°C | < 5.5°C or > 8.5°C | $\le$ 4.0°C |
| **Chilled Water Return Temperature** | 11.0°C – 13.0°C | > 14.5°C | N/A |
| **Condenser Water Inlet Temperature** | 29.0°C – 32.0°C | > 35.0°C | $\ge$ 38.5°C |
| **Compressor Motor Current (FLA)** | 185 A – 210 A | > 235 A | $\ge$ 255 A |
| **Compressor Vibration Velocity** | 1.1 mm/s – 2.8 mm/s | > 4.5 mm/s | $\ge$ 7.1 mm/s |
| **Oil Sump Temperature** | 45.0°C – 55.0°C | > 62.0°C | $\ge$ 70.0°C |

2.2 **Vibration Measurement Points:** Vibration velocity shall be measured tri-axially at the compressor inboard motor bearing, compressor outboard screw housing, and the refrigerant pump discharge flange using a calibrated handheld accelerometer.

---

### 3.0 PREVENTIVE MAINTENANCE SCHEDULE

3.1 **Running Hours Tracking:** Maintenance intervals are governed by cumulative compressor running hours as logged by the PLC. If running hours do not accrue to the threshold within the maximum calendar window, the time-based limit shall take precedence.

| Interval (Running Hours / Calendar) | Maintenance Task Description | Execution Role |
| :--- | :--- | :--- |
| **250 Hours / Monthly** | Inspect refrigerant sight glass for moisture indicators and bubble formation; record compressor oil level; verify strainer differential pressure across chilled and condenser water loops. | Level 1 Technician |
| **1,000 Hours / Quarterly** | Clean condenser tube bundles via mechanical tube brushing; analyze compressor lubricating oil sample for acid content and moisture; test safety interlock flow switches. | Level 2 Technician |
| **4,000 Hours / Semi-Annually** | Replace liquid line filter-driers (Part VPW-CH-901); calibrate electronic expansion valve (EEV) positioning feedback; measure motor winding insulation resistance (Megger test at 1000V DC). | Senior Technician |
| **8,000 Hours / Annually** | Perform Eddy Current testing on condenser and evaporator titanium tubes; service oil separator coalescing elements (Part VPW-CH-905); overhaul compressor slide valve actuator linkage. | Specialist Contractor / Lead Tech |
| **24,000 Hours / Tri-Annually** | Complete compressor major overhaul: replace rotor bearings, mechanical shaft seals, internal o-rings, and check valve assemblies. | Original Equipment Manufacturer Certified Team |

---

### 4.0 FAULT-CODE TABLE AND CORRECTIVE ACTIONS

4.1 **Fault Response:** When the chiller control panel registers an active fault code, operators shall not perform a blind reset. Technicians shall execute the diagnostics outlined below.

| Fault Code & Name | Probable Cause | Corrective Action |
| :--- | :--- | :--- |
| **F-CH-101: Low Evaporator Pressure Trip** | Restricted water flow through evaporator barrel, fouled tubes, or low refrigerant charge due to a micro-leak. | 1. Verify chilled water pump operation and strainer cleanliness.<br>2. Measure approach temperature (Refrigerant Saturation Temp vs. Chilled Water Leaving Temp). If approach > 5.5°C, chemically clean evaporator tubes.<br>3. Check for oil migration and bubble presence in sight glass. Perform electronic leak test if charge is depleted. |
| **F-CH-102: High Condenser Head Pressure** | Scaling on condenser tubes, non-condensable gases trapped in the refrigerant circuit, or insufficient cooling tower water flow. | 1. Verify cooling tower fan operation and bypass valve positioning.<br>2. Purge non-condensable gases using the automated purge unit.<br>3. Isolate condenser water box and mechanically brush copper-nickel tubes. |
| **F-CH-103: Compressor Motor Overload** | Excessive refrigerant discharge pressure, low supply voltage, phase imbalance exceeding 2%, or internal mechanical binding. | 1. Check incoming line voltages across phases L1, L2, and L3 at the starter terminals.<br>2. Measure running current per phase under load.<br>3. Inspect contactor tips for pitting or welding; replace contactor block if contact resistance > 0.5 ohms. |
| **F-CH-104: Low Oil Level / Low Differential Pressure** | Blocked oil return line, saturated oil separator filter element, or failing oil pump. | 1. Verify oil separator heater is operational (minimum oil temperature 40°C prior to start).<br>2. Replace oil filter cartridge (Part VPW-CH-903) and differential pressure transducer.<br>3. Inspect oil pump internal gear clearances if pressure differential remains < 1.5 bar above suction. |
| **F-CH-105: High Discharge Gas Temperature** | Insufficient liquid injection cooling, restricted expansion valve, or operating with a high compression ratio (low suction / high discharge). | 1. Verify superheat setpoint and operation of the electronic expansion valve (EEV).<br>2. Calibrate discharge temperature thermistor probe (RTD PT100).<br>3. Check for subcooling deficiency indicating undercharge. |
| **F-CH-106: Flow Switch Interlock Failure** | Mechanical paddle stuck in housing, air pocket in water piping, or differential pressure switch out of calibration. | 1. Isolate flow switch assembly; remove paddle and inspect for mineral scaling or debris entanglement.<br>2. Bleed air from the highest point vent cock on the condenser and evaporator water headers.<br>3. Verify switch trip point against differential pressure gauge across the inlet and outlet taps. |

---

### 5.0 CONSUMABLE AND SPARE PARTS LIST

5.1 Technicians shall procure replacement items exclusively from the internal stores quoting the following Vindhya Precision Works part numbers. Substitution of unapproved equivalents is prohibited.

| Item Description | VPW Part Number | Replacement Specification |
| :--- | :--- | :--- |
| **Filter-Drier Core (Liquid Line)** | VPW-CH-901 | Solid core, 100% molecular sieve, 48 cu. in. capacity |
| **Compressor Oil Filter** | VPW-CH-903 | Spin-on micro-glass media, 10-micron absolute rating |
| **Oil Separator Coalescing Element** | VPW-CH-905 | Multi-layer borosilicate microfiber matrix |
| **Synthetic Compressor Lubricant** | VPW-CH-910 | Polyolester (POE) ISO VG 68, 5-litre container |
| **Compressor Shaft Seal Kit** | VPW-CH-922 | Carbon-ceramic mechanical face seal with Viton elastomers |
| **Evaporator Flow Switch Assembly** | VPW-CH-940 | SPDT snap-action switch with adjustable paddle |
| **Discharge Temperature Sensor** | VPW-CH-955 | PT100 Platinum RTD, 3-wire configuration, -50°C to +150°C |

---

### 6.0 TORQUE SPECIFICATIONS

6.1 All threaded fasteners opened during maintenance interventions shall be tightened using a calibrated torque wrench in a criss-cross pattern. Dry torque values apply unless specified otherwise.

| Application | Fastener Size / Grade | Target Torque Value |
| :--- | :--- | :--- |
| **Compressor Discharge Flange Bolts** | M16 / Grade 8.8 | 175 Nm ($\pm$ 5 Nm) |
| **Refrigerant Liquid Line Flange Bolts** | M10 / Grade 8.8 | 45 Nm ($\pm$ 2 Nm) |
| **Condenser Water Box Cover Nuts** | M20 / Grade 10.9 | 310 Nm ($\pm$ 10 Nm) |
| **Compressor Terminal Stud Nuts** | M8 / Brass | 12 Nm ($\pm$ 1 Nm) |
| **Oil Pump Mounting Bolts** | M12 / Grade 8.8 | 85 Nm ($\pm$ 3 Nm) |
| **EEV Stepper Motor Securing Screws** | M5 / Grade A2-70 | 5.5 Nm ($\pm$ 0.2 Nm) |

---

### 7.0 SAFETY-CRITICAL CORRECTIVE ACTIONS AND LOCKOUT/TAGOUT (LOTO) MANDATES

7.1 **Mandatory Isolation:** The corrective actions listed below involve high-voltage electricity, high-pressure refrigerant vessels, or rotating mechanical assemblies. They are classified as **Safety-Critical**.

7.2 **Permit Requirement:** No technician shall initiate work on any safety-critical action without first securing:
1. An approved Safe Work Permit (SWP) issued by the Plant Safety Department.
2. A verified Equipment Isolation Certificate (EIC).
3. Personal application of a personal red padlock and danger tag at all designated isolation points in accordance with VPW-EHS-SOP-012.

7.3 **Explicit List of Safety-Critical Corrective Actions:**
* **SC-01:** Replacement of compressor motor terminal wiring, contactors, or soft-start electronic modules (Requires Electrical LOTO at 415V AC main distribution board).
* **SC-02:** Overhaul or replacement of the screw compressor assembly, including internal rotors, bearings, and shaft seals (Requires Mechanical LOTO, depressurization of refrigerant circuit to $< 0.2\text{ bar}$, and recovery of R-134a refrigerant charge).
* **SC-03:** Opening of condenser or evaporator water boxes for tube cleaning or eddy current testing (Requires Hydraulic LOTO: closure of manual isolation valves on inlet and outlet water headers, locking of chilled and condenser water pump breakers).
* **SC-04:** Replacement of high-pressure safety relief valves (PRVs) located on the refrigerant liquid receiver or oil separator (Requires total system pump-down and isolation via dual-outlet stop valves).
* **SC-05:** Servicing of the internal oil separator coalescing elements or oil pump removal (Requires isolation of oil circuit heaters, pressure relief of the oil sump, and capture of residual POE oil to prevent slip hazards).

7.4 **Post-Maintenance Sign-Off:** Upon completion of any safety-critical action, the maintenance lead and the shift safety officer shall jointly inspect the asset, remove all isolation devices, and execute the pre-start checklist before returning the CHILLER asset class unit to operational service.
