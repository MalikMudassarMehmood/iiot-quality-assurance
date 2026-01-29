# Development of an Automated Quality Assurance System for the Beverage Industry Using IIoT Technologies

**Author:** Mudassar Mehmood  
**Affiliation:** National Textile University, Faisalabad, Pakistan  
**Corresponding Author:** malikmudassar0197@gmail.com  

---

## Table of Contents
1. [Description](#description)
2. [Dataset Information](#dataset-information)
3. [Code Information](#code-information)
4. [Usage Instructions](#usage-instructions)
5. [Requirements](#requirements)
6. [Methodology](#methodology)
7. [Figures](#figures)
8. [License & Usage](#license--usage)

---

## Description
This project presents the design and implementation of an **Industrial Internet of Things (IIoT)-enabled automated quality assurance system** for beverage production lines. The system measures the weight of empty bottles, filled bottles, and final packaged products using load cells and Arduino-based acquisition, and automatically accepts or rejects bottles based on predefined thresholds. Real-time logging ensures traceability and supports continuous quality improvement.

This README communicates:
- What the project does  
- Why the project is useful  
- How users can get started with the project  
- Where users can get help  
- Who maintains and created the project  

---

## Dataset Information
The dataset consists of weight readings for PET bottles at three production stages: empty, filled, and final packaged.  

- **Real samples:** 1,000 per category (empty, filled, final)  
- **Synthetic samples:** 9,000 per category generated using uniform random distribution within realistic weight ranges  
- **Total samples:** 10,000 per category  

**Weight ranges used for synthetic data generation:**
- Empty bottles: 14–20 g  
- Filled bottles: 516–529 g  
- Final packaged bottles: 520–530 g  

Data is labeled with the corresponding inspection stage for classification and analysis.

---

## Code Information
The repository includes the following main components:

- **Arduino Scripts:** Reads load cell data via HX711 and transmits weights to the host computer over USB serial.
- **Python Scripts:** Receives serial data, applies threshold checks for underfilling, overfilling, or defective caps, logs inspection results, and generates reports.

---

## Usage Instructions
1. **Hardware Setup:**  
   - Connect three IIoT-enabled load cells with HX711 modules to an Arduino UNO.  
   - Place the conveyor system or testing platform for bottle inspection.  

2. **Software Setup:**  
   - Connect Arduino to the workstation via USB.  
   - Run the Arduino sketch to start weight acquisition.  
   - On the host computer, run the Python scripts to receive data, process thresholds, and log results.

3. **Data Logging:**  
   - The Python scripts save CSV files containing weight values, inspection stage labels, acceptance/rejection decisions, and timestamps.  

4. **Analysis & Visualization:**  
   - Use the generated CSV files for further analysis, plotting, or machine learning experiments.

---

## Requirements
- **Hardware:**  
  - Arduino UNO (ATmega328P, 16 MHz)  
  - 3 × Load Cells (5 kg capacity)  
  - 3 × HX711 modules  
  - USB power supply and connecting wires  
  - PET bottles (500 ml)

- **Software / Libraries:**  
  - Python 3.x  
  - `pyserial` (for serial communication)  
  - `pandas` (for CSV logging and data manipulation)  
  - `matplotlib` or `seaborn` (optional, for plotting)  

---

## Methodology
1. **Sensor Integration:** Load cells and HX711 modules capture weights at three stages: empty, post-filling, and final capping.  
2. **Data Acquisition:** Arduino UNO collects sensor data and transmits it to a workstation via USB serial.  
3. **Real-Time Data Processing:** Python scripts compare readings against predefined thresholds to detect anomalies.  
4. **Decision-Making:** Bottles are automatically accepted or rejected based on the sensor readings.  
5. **Logging & Traceability:** Each stage logs outcomes, timestamps, and weight values for auditability.  
6. **Synthetic Data Generation:** Uniform random data within realistic weight ranges is used to augment the real dataset to 10,000 samples per category.  
7. **Performance Evaluation:** The system was tested for average processing times per stage and compared against traditional automated inspection methods.



## License & Usage
This project and dataset are created by Mudassar Mehmood for research purposes. You are free to use, modify, or reference this work in your own projects, provided you credit the author.  

- **Author:** Mudassar Mehmood  
- **Affiliation:** National Textile University, Faisalabad, Pakistan  
- **Email:** malikmudassar0197@gmail.com  

> Note: This is original work and part of my first research project. No external datasets or third-party code are included.
