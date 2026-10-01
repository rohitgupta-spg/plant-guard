# Lockout/Tagout and Energy Isolation Standard

**STANDARD OPERATING PROCEDURE: CONTROL OF HAZARDOUS ENERGY (LOCKOUT/TAGOUT)**
**Document ID:** VPW-SOP-EHS-042
**Revision:** 4.1
**Effective Date:** 14 January 2025
**Applies To:** All Production, Maintenance, and Contractor Personnel at Vindhya Precision Works Plant No. 2

---

### 1. PURPOSE AND SCOPE

1.1 This document establishes the mandatory minimum requirements for the isolation of hazardous energy sources during installation, maintenance, service, or repair work on machinery and equipment within Vindhya Precision Works (VPW) facilities.

1.2 Compliance with this Standard is mandatory for all direct employees, agency workers, and contracted service providers.

1.3 No maintenance task involving energy isolation may be performed on the basis of a recommendation from an automated system (including predictive maintenance algorithms, SCADA advisory triggers, or PLC-generated service flags) without a physical inspection and written sign-off by a designated competent person.

---

### 2. DEFINITIONS

2.1 **Authorised Person:** A maintenance technician, engineer, or supervisor who has completed VPW Lockout/Tagout (LOTO) Level 2 certification and is explicitly authorized to apply isolation devices and locks.

2.2 **Affected Employee:** An operator whose job requires them to operate or use equipment on which servicing or maintenance is being performed under LOTO.

2.3 **Isolation Device:** A mechanical or electrical device that physically prevents the transmission or release of energy, including but not limited to manual circuit breakers, disconnect switches, line valves, and mechanical slip blinds.

2.4 **Lockout Device:** A red padlock bearing a unique serial number, individual employee identification tag, and the legend "DANGER - DO NOT OPERATE."

---

### 3. THE SIX-STEP ISOLATION SEQUENCE

All energy-isolating activities must strictly follow the sequential order defined below. Skipping or reordering steps is a critical safety violation.

3.1 **Step 1: Notification.** The Authorised Person shall notify all affected equipment operators and area supervisors of the impending shutdown at least ten (10) minutes prior to energy isolation.

3.2 **Step 2: Machine or Equipment Shutdown.** The equipment shall be shut down using standard stopping controls (e.g., control panel stop buttons, cycle finish commands). Do not use an emergency stop or a main circuit breaker as a routine operational shutdown method unless specified in the equipment-specific LOTO sheet.

3.3 **Step 3: Machine or Equipment Isolation.** All primary energy sources (electrical, hydraulic, pneumatic, thermal, chemical, and gravitational) shall be located and operated to isolate the equipment from its energy source(s). Isolation devices must be moved to the "OFF" or "OPEN" position.

3.4 **Step 4: LOTO Device Application.** The Authorised Person shall affix their individually keyed red lockout device and completed hazard tag to each energy-isolating device. Hasps must be used when more than one person services the equipment. Each person must apply their own lock.

3.5 **Step 5: Stored-Energy Dissipation and Verification.** All residual, stored, or trapped energy must be relieved, disconnected, restrained, or otherwise rendered safe in accordance with Section 5 of this Standard.

3.6 **Step 6: Isolation Verification (Zero-Energy State).** The Authorised Person shall test machine operation (e.g., pressing start buttons, cycling joysticks) and use calibrated test instruments to verify that isolation is effective and that a complete zero-energy state has been achieved. All controls must be returned to the "OFF" or "NEUTRAL" position following the test.

---

### 4. APPLICATION AND REMOVAL AUTHORITY

4.1 **Application:** Only an Authorised Person who has completed VPW LOTO certification within the preceding twelve (12) months may apply lockout devices.

4.2 **Removal Rule:** Each lockout device shall be removed *only* by the specific Authorised Person who installed it. 

4.3 **Single Named Exception to Removal Rule:** A lock applied by an Authorised Person may be removed by another individual *only* under the following cumulative conditions:
   a) The original Authorised Person is off-site and cannot be reached within two (2) hours, or is medically incapacitated.
   b) A physical verification has been conducted jointly by the Plant Engineering Manager (Marcus Vance) and the EHS Manager (Priya Sharma) confirming that the equipment is safe to energize and that no personnel are exposed.
   c) Formal authorization has been executed via Form VPW-LOTO-EXC-02, signed in person by both Marcus Vance and Priya Sharma.
   d) The affected employee and area supervisor are directly notified before re-energization.

---

### 5. STORED-ENERGY VERIFICATION PROCEDURES

5.1 **Electrical Systems:**
   a) Open the primary circuit breaker or disconnect switch.
   b) Apply lockout/tagout.
   c) Using a CAT III 1000V / CAT IV 600V digital multimeter verified against a known live source immediately before and after the test, measure voltage across all phase-to-phase and phase-to-ground terminals.
   d) Confirm zero voltage reads across all circuits.
   e) Where capacitors are present within variable frequency drives (VFDs) or servo controllers, wait the mandatory discharge duration specified on the equipment housing (minimum five [5] minutes) and verify voltage bleed-down at the DC bus terminals reads below 10 volts DC prior to contact.

5.2 **Pneumatic Systems:**
   a) Close the main supply line isolation valve (ball valve or lockable slide valve).
   b) Apply lockout/tagout to the valve handle.
   c) Open the downstream bleed/exhaust valve to vent trapped pressure.
   d) Verify downstream pressure gauge reads 0.0 bar (0.0 psi) within forty-five (45) seconds of opening the exhaust valve.
   e) Disconnect quick-release pneumatic couplings if pressure persists.

5.3 **Hydraulic Systems:**
   a) Stop the hydraulic power unit (HPU) motor and lock out the electrical supply.
   b) Close the pump discharge isolation valve and apply lockout/tagout.
   c) Open the manifold pressure relief valve to tank return.
   d) Verify accumulator pressure gauges (both circuit and pre-charge sides) read 0.0 bar. If an accumulator cannot be isolated and drained via valve, it must be discharged via hydraulic bleed block under the direct supervision of a certified hydraulic specialist (Level 3 or higher).
   e) Lower all suspended mechanical loads (platens, cylinders, robotic arms) to the lowest mechanical resting position or install rated mechanical lock pins/safety blocks capable of supporting 150% of the maximum suspended load before breaking the hydraulic circuit.

---

### 6. GROUP LOCKOUT PROCEDURE

6.1 When servicing is performed by a maintenance crew, shift rotation team, or multi-craft contractors, a Group Lockout procedure must be implemented by the designated Lead Authorised Person (LAP).

6.2 The LAP shall ensure all primary energy-isolating devices are locked out using a group lockbox (lockout station box) in accordance with Steps 1 through 5 of Section 3.

6.3 The LAP shall place the keys to the primary isolation locks inside the group lockbox.

6.4 Each participating crew member (maintenance technician, electrician, or contractor) shall apply their personal red lockout device and tag to the designated latch of the group lockbox.

6.5 While an individual's personal lock remains on the group lockbox, that individual is protected against accidental re-energization, regardless of shift changes.

6.6 Individual crew members shall remove their personal locks from the group lockbox immediately upon completing their assigned task or at the end of their shift, provided they are not returning to the same task. The LAP shall remove the primary isolation locks only after all crew members have removed their personal locks from the box and the equipment is fully reassembled and verified safe.

---

### 7. REVISION HISTORY

* **Rev 4.0:** 10 January 2024 - Initial release under VPW Master Management System.
* **Rev 4.1:** 14 January 2025 - Updated Section 1.3 to explicitly prohibit reliance on automated system recommendations without manual competent person sign-off. Added Marcus Vance and Priya Sharma as named exception signatories in Section 4.3.
