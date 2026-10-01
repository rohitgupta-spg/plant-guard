# Vertical CNC Machining Centre (CNC-MILL) Equipment Manual and SOP

**DOCUMENT ID:** SOP-MNT-CNC-MILL-014  
**EFFECTIVE DATE:** 14 MARCH 2024  
**REVISION:** 4.2  
**ASSET CLASS:** Vertical CNC Machining Centre (Asset Tag Prefix: CNC-MILL)  
**AUTHOR:** Marcus Vance, Maintenance Engineering Lead, Vindhya Precision Works  

---

### 1. OPERATING PARAMETERS AND ALARM THRESHOLDS

Technicians and operators shall verify that all live telemetry from the CNC-MILL asset class remains within the operational ranges defined in Table 1.1. Operation outside these limits without an active work order constitutes a safety and asset integrity violation.

#### Table 1.1: Operational Limits and Alarm Setpoints (CNC-MILL)

| Parameter | Normal Operating Range | Warning Threshold (Operator Notice) | Critical Trip Setpoint (Immediate Estop) |
| :--- | :--- | :--- | :--- |
| **Spindle Bearing Temp (Front/Rear)** | $22\text{°C} - 55\text{°C}$ | $68\text{°C}$ sustained for $>30\text{s}$ | $\ge 78\text{°C}$ |
| **Spindle Vibration Velocity (RMS)** | $0.4\text{ mm/s} - 2.1\text{ mm/s}$ | $3.5\text{ mm/s}$ | $\ge 5.0\text{ mm/s}$ |
| **Hydraulic System Pressure** | $4.8\text{ MPa} - 5.2\text{ MPa}$ | $< 4.4\text{ MPa}$ or $> 5.6\text{ MPa}$ | $\le 3.8\text{ MPa}$ or $\ge 6.2\text{ MPa}$ |
| **Pneumatic Supply Pressure** | $0.62\text{ MPa} - 0.68\text{ MPa}$ | $< 0.58\text{ MPa}$ | $\le 0.50\text{ MPa}$ |
| **Spindle Drive Current (No-Load)** | $12\text{ A} - 28\text{ A}$ | N/A | $\ge 65\text{ A}$ (Continuous for $>2\text{s}$) |
| **Axis Servo Motor Current (X/Y/Z)**| $8\text{ A} - 22\text{ A}$ | N/A | $\ge 42\text{ A}$ |
| **Coolant Flow Rate** | $18\text{ L/min} - 25\text{ L/min}$ | $< 14\text{ L/min}$ | $\le 10\text{ L/min}$ |

---

### 2. PREVENTIVE MAINTENANCE SCHEDULE

All maintenance intervals for asset class CNC-MILL are calculated by integrated spindle running hours ($H$), tracked via the machine Programmable Logic Controller (PLC) register $R[204]$. 

#### 2.1 Interval: 250 Running Hours ($\pm 10$ Hours) [Level PM-1]
1. Inspect and clean optical glass scales for X, Y, and Z axes using anhydrous isopropyl alcohol and lint-free optics cloth.
2. Verify automatic lubrication reservoir level (VPW Part No. LUB-8821); top up with synthetic slideway oil if level is below 40%.
3. Clean chip conveyor trough and flush coolant sump primary settling tank.
4. Check pneumatic FRL (Filter-Regulator-Lubricator) unit; drain water separator bowl manually.

#### 2.2 Interval: 1,000 Running Hours ($\pm 25$ Hours) [Level PM-2]
1. Perform PM-1 tasks.
2. Grease Z-axis ballscrew support bearings using high-temperature lithium complex grease (VPW Part No. LUB-9042, exactly 4 strokes per grease nipple via calibrated manual grease gun).
3. Inspect flexible cable carrier tracks on X and Y axes for mechanical binding, abrasion, or cracked links.
4. Clean spindle taper (BT40) using a brass brush arbor cleaner and check drawbar clamping force using dynamic tension gauge (Acceptance threshold: $\ge 8.5\text{ kN}$).
5. Replace hydraulic return line filter element.

#### 2.3 Interval: 4,000 Running Hours ($\pm 50$ Hours) [Level PM-3]
1. Perform PM-1 and PM-2 tasks.
2. Complete backlash measurement audit on X, Y, and Z axes using laser interferometer; adjust software compensation parameters if backlash exceeds $0.012\text{ mm}$.
3. Drain, flush, and refill the main hydraulic power unit with ISO VG 46 anti-wear hydraulic oil.
4. Calibrate axis linear scales and inspect resolver couplings for angular slippage.
5. Perform thermal growth verification test per VPW Engineering Standard ES-CNC-09.

---

### 3. FAULT-CODE TROUBLESHOOTING TABLE

When the CNC-MILL controller flags an alarm, technicians shall cross-reference Table 3.1 for probable root causes and mandated corrective procedures.

#### Table 3.1: Fault Codes and Corrective Actions

| Fault Code | Description | Probable Cause | Corrective Action |
| :--- | :--- | :--- | :--- |
| **ERR-101** | Spindle Overload Current | Excessive cutting feed rate, dull tooling, or mechanical seizure in spindle cartridge bearings. | Stop execution immediately. Inspect cutting tool for insert chipping. Rotate spindle manually via hand wrench (power off) to check for binding. If mechanical resistance is detected, isolate asset and execute corrective overhaul of spindle cartridge. |
| **ERR-204** | Lube Pressure Fault | Drop in centralized lubrication distribution pressure; blocked metering cartridge or ruptured nylon feed line. | Check reservoir level. Execute manual lube cycle via MDI mode ($M33$). Inspect distribution manifold pressure gauges. If pressure fails to reach $2.5\text{ MPa}$, trace lines for leaks or replace clogged progressive distributor blocks (VPW Part No. LUB-M504). |
| **ERR-312** | Axis Servo Lag (Following Error) | Mechanical binding on slideway, failing axis servo motor, or broken ballscrew pre-load nut. | Perform drag-torque test on axis ballscrew with motor uncoupled. Inspect linear guideway carriage wipers for foreign debris. Verify servo drive tuning parameters in parameter group $N1000$. |
| **ERR-405** | Hydraulic Pressure Low | Internal pump wear, bypassed proportional pressure relief valve, or suction strainer blockage. | Verify pump intake pressure. Clean suction strainer element. Adjust pressure relief valve back to $5.0\text{ MPa}$. If pressure decay recurs, replace hydraulic pump assembly. |
| **ERR-518** | Coolant Flow Failure | Low coolant level in tank, airlock in coolant pump impeller, or clogged delivery nozzles. | Top up soluble oil coolant concentration to $8\%$. Bleed pump housing via bleed screw. Clean chip basket and flush coolant intake strainer. Replace submersible pump if thermal overload trips. |
| **ERR-622** | Tool Changer Position Error | Mechanical index cam misalignment, proximity sensor failure on Geneva drive, or low pneumatic pressure. | Check pneumatic line pressure (must be $>0.62\text{ MPa}$). Inspect magnetic proximity sensor alignment on tool magazine carousel. Manually index magazine using auxiliary hand crank to clear mechanical jam. |

---

### 4. CONSUMABLE AND SPARE PARTS LIST

Technicians shall procure replacement items exclusively through the Vindhya Precision Works stores inventory utilizing the part numbers specified in Table 4.1.

#### Table 4.1: Approved Consumables and Spares

| Item Description | VPW Part Number | Replacement Interval / Quantity |
| :--- | :--- | :--- |
| Spindle Air Purge Regulator Filter Element | FLT-SP-402 | Every 2,000 Hours / Qty: 1 |
| Hydraulic Return Line Filter Element | FLT-HYD-881 | Every 1,000 Hours / Qty: 1 |
| Automatic Lubrication Cartridge Grease (Slideway) | LUB-8821 | Refill per PM-1 / Qty: 2.5 L canister |
| High-Temp Ball Screw Bearing Grease | LUB-9042 | Refill per PM-2 / Qty: 400 g cartridge |
| Coolant Sump Biocide Additive | CHM-BIO-11 | Monthly / Qty: 1 L dose |
| Axis Slideway Wiper Blade Assembly (X/Y Axis) | WPR-CNC-X2 | Every 8,000 Hours / Qty: Set of 4 |
| Spindle Drawbar Gripper Fingers (BT40) | SPU-GRP-40 | Every 6,000 Hours / Qty: Set of 3 |
| Main Electrical Cabinet Cooling Fan Filter | FLT-FAN-220 | Every 500 Hours / Qty: Set of 2 |

---

### 5. TORQUE SPECIFICATIONS

All mechanical fasteners on asset class CNC-MILL must be tightened using a calibrated torque wrench. Fasteners tightened outside $\pm 5\%$ of the specified torque values listed in Table 5.1 shall be loosened and retorqued.

#### Table 5.1: Fastener Torque Limits

| Application | Fastener Grade | Thread Size | Target Torque ($N\cdot m$) |
| :--- | :--- | :--- | :--- |
| Spindle Cartridge Mounting Bolts | ISO 898-1 Gr. 12.9 | M12 | $115\text{ N}\cdot\text{m}$ |
| Axis Ballscrew Bearing Locknuts | ISO 898-1 Gr. 10.9 | M20x1.5 | $145\text{ N}\cdot\text{m}$ |
| Tool Changer Arm Clamp Bolts | ISO 898-1 Gr. 12.9 | M8 | $34\text{ N}\cdot\text{m}$ |
| Slideway Linear Guide Rail Mounting Screws | ISO 898-1 Gr. 12.9 | M10 | $72\text{ N}\cdot\text{m}$ |
| Hydraulic Manifold Sandwich Valves | ISO 898-1 Gr. 10.9 | M6 | $12\text{ N}\cdot\text{m}$ |
| Table T-Slot Clamping Studs (Fixture plate) | ISO 898-1 Gr. 8.8 | M16 | $160\text{ N}\cdot\text{m}$ |

---

### 6. SAFETY-CRITICAL CORRECTIVE ACTIONS AND LOCKOUT/TAGOUT (LOTO) MANDATES

Under Vindhya Precision Works Safety Policy SP-09, corrective actions involving physical intrusion into the dynamic envelope, power transmission pathways, or fluid power circuits of asset class CNC-MILL are designated as **Safety-Critical**. 

#### 6.1 Mandatory LOTO and Permit Requirements
Before executing any of the corrective actions listed in Section 6.2, technicians must:
1. Issue an active **Maintenance Work Permit (MWP)** countersigned by the Plant Safety Officer, Arthur Pendelton.
2. Apply physical Lockout/Tagout (LOTO) devices in accordance with VPW Standard Procedure LOTO-GEN-01.
3. Verify zero energy state across electrical, pneumatic, and hydraulic domains at the machine isolation panel (Isolation Breaker ID: *ISO-CNC-MILL-01*).

#### 6.2 Explicit List of Safety-Critical Corrective Actions
The following specific procedures **strictly require** an issued MWP, zero-energy LOTO verification, and the attachment of personal padlocks prior to commencement:

1. **Spindle Cartridge Replacement or Internal Bearing Overhaul:** Involves unbolting heavy mechanical sub-assemblies overhead and handling precision pre-loaded bearings. Isolation of electrical supply to the spindle inverter drive and mechanical blocking of the Z-axis ram using rated safety support struts is mandatory.
2. **Axis Ballscrew and Linear Guide Replacement:** Involves releasing mechanical pre-loads on axes under gravity influence (Z-axis) or spring tension. Z-axis mechanical drop-arrestor pin must be engaged prior to uncoupling the ballscrew nut.
3. **Hydraulic Power Unit Pump or Proportional Valve Replacement:** Involves breaking high-pressure hydraulic lines ($5.0\text{ MPa}$). System must be depressurized via the manual bleed valve, and accumulator pressure dumped to $0\text{ MPa}$ before flange separation.
4. **Tool Magazine Geneva Drive and Cam Gearbox Maintenance:** Involves working within the mechanical tool changer interlock boundary. The pneumatic supply valve to the ATC must be locked out in the closed position, and the pneumatic dump valve opened to exhaust stored cylinder pressure.
5. **Main Spindle Drawbar Uncoupling and Gripper Finger Replacement:** Involves releasing high-tension spring packs capable of sudden mechanical energy release. Technicians must utilize the VPW-approved mechanical drawbar compression fixture (Tool ID: *TOL-DB-40*) to contain spring energy before pin extraction.
